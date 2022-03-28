// on input/text enter--------------------------------------------------------------------------------------
$('.usrInput').on('keyup keypress', function (e) {
	var keyCode = e.keyCode || e.which;
	var text = $(".usrInput").val();

	if (keyCode === 13) {

		if (text == "" || $.trim(text) == '') {
			e.preventDefault();
			return false;
		} else {
			$(".usrInput").blur();
			setUserResponse(text);
			const url = 'http://localhost:8989/trans?text='+text+'&lang=en';
            fetch(url)
            .then(response => {
                response.text()
                .then(text => {
                    send(text);
                    console.log(text);
                })
                .catch(err => {
                    console.log(err);
                })
            })
            .catch(err => {
                console.log(err);
            })

			e.preventDefault();
			return false;
		}
	}
});


//------------------------------------- Set user response------------------------------------
function setUserResponse(val) {
	var UserResponse = '<img class="userAvatar" src=' + "./static/img/userAvatar.jpg" + '><p class="userMsg">' + val + ' </p><div class="clearfix"></div>';
	$(UserResponse).appendTo('.chats').show('slow');
	$(".usrInput").val('');
	scrollToBottomOfResults();
	$('.suggestions').remove();
}

//---------------------------------- Scroll to the bottom of the chats-------------------------------
function scrollToBottomOfResults() {
	var terminalResultsDiv = document.getElementById('chats');
	terminalResultsDiv.scrollTop = terminalResultsDiv.scrollHeight;
}

function send(message) {
	
	//---------------------------------- Response wait message -------------------------------

	var waitAnime = '<div class="botWaitMsg botMsg" > <span class="resWait"></span><span class="resWait"></span><span class="resWait"></span></div>';
	var UserResponse = '<div class="waiting" ><img class="botAvatar" src="./static/img/avatar.png">'
						+ waitAnime + 
						'<div class="clearfix"></div></div>';
	$(UserResponse).appendTo('.chats').show('slow');
	$(".usrInput").val('');
	scrollToBottomOfResults();

	console.log("User Message:", message)
	$.ajax({
		url: 'http://localhost:5005/webhooks/rest/webhook',
		type: 'POST',
		contentType: 'application/json',
		data: JSON.stringify({
			"message": message,
			"sender": "Me"
		}),
		success: function (data, textStatus) {
			$("div.waiting").remove();
			if(data != null){
					setBotResponse(data);
			}
			console.log("Rasa Response: ", data, "\n Status:", textStatus)
		},
		error: function (errorMessage) {
			setBotResponse("");
			console.log('Error' + errorMessage);
			$("div.waiting").remove();
		}
	});
}

//------------------------------------ Set bot response -------------------------------------
function setBotResponse(val) {
	setTimeout(function () {
		if (val.length < 1) {
			//if there is no response from Rasa
			msg = 'I couldn\'t get that. Let\'s try something else!';
            const url = 'http://localhost:8989/translate?text='+msg;
            fetch(url)
            .then(response => {
                response.text()
                .then(text => {
                    console.log(text);
                    var BotResponse = '<img class="botAvatar" src="./static/img/avatar.png"><p class="botMsg">' + text + '</p><div class="clearfix"></div>';
			        $(BotResponse).appendTo('.chats').hide().fadeIn(1000);
                })
                .catch(err => {
                    console.log(err);
                })
            })
            .catch(err => {
                console.log(err);
            })


		} else {
			//if we get response from Rasa
			for (i = 0; i < val.length; i++) {
				//check if there is text message
				if (val[i].hasOwnProperty("text")) {
				    var res = val[i].text
				    res = res.replace("<p>","")
				    res = res.replace("</p>","")
				    console.log(res);
				    const url = 'http://localhost:8989/translate?text='+res;
                    fetch(url)
                    .then(response => {
                        response.text()
                        .then(text => {
                            console.log(text);
                            var BotResponse = '<img class="botAvatar" src="./static/img/avatar.png"><p class="botMsg">' + text + '</p><div class="clearfix"></div>';
                            $(BotResponse).appendTo('.chats').hide().fadeIn(1000);
                        })
                        .catch(err => {
                            console.log(err);
                        })
                    })
                    .catch(err => {
                        console.log(err);
                    })

				}

				//check if there is image
				if (val[i].hasOwnProperty("image")) {
					var BotResponse = '<div class="singleCard">' +
						'<img class="imgcard" src="' + val[i].image + '">' +
						'</div><div class="clearfix">'
					$(BotResponse).appendTo('.chats').hide().fadeIn(1000);
				}

				//check if there is  button message
				if (val[i].hasOwnProperty("buttons")) {
					addSuggestion(val[i].buttons);
				}

			}
			scrollToBottomOfResults();
		}

	}, 500);
}


// ------------------------------------------ Toggle chatbot -----------------------------------------------
$('#profile_div').click(function () {
	$('.profile_div').toggle();
	$('.widget').toggle();
	scrollToBottomOfResults();
});

$('#close').click(function () {
	$('.profile_div').toggle();
	$('.widget').toggle();
});


// ------------------------------------------ Suggestions -----------------------------------------------

function addSuggestion(textToAdd) {
	setTimeout(function () {
		var suggestions = textToAdd;
		var suggLength = textToAdd.length;
		$(' <div class="singleCard"> <div class="suggestions"><div class="menu"></div></div></diV>').appendTo('.chats').hide().fadeIn(1000);
		// Loop through suggestions
		for (i = 0; i < suggLength; i++) {
			$('<div class="menuChips" data-payload=\''+(suggestions[i].payload)+'\'>' + suggestions[i].title + "</div>").appendTo(".menu");
		}
		scrollToBottomOfResults();
	}, 1000);
}


// on click of suggestions, get the value and send to rasa
$(document).on("click", ".menu .menuChips", function () {
	var text = this.innerText;
	var payload= this.getAttribute('data-payload');
	console.log("button payload: ",this.getAttribute('data-payload'))
	setUserResponse(text);
	send(payload);
	$('.suggestions').remove(); //delete the suggestions 
});
