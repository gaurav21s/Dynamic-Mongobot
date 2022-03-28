from flask import Flask, request
from flask_cors import CORS

from googletrans import Translator

app = Flask(__name__)
CORS(app)


@app.route('/trans', methods=['GET', 'POST'])
def trans():
    text1 = request.args['text']
    lang = request.args['lang']
    translator = Translator(service_urls=['translate.googleapis.com'])
    res = translator.translate(text1, dest=lang)
    global src
    src = res.src
    # ans = {"status": res.text}
    return res.text


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    text1 = request.args['text']
    # lang = request.args['lang']
    translator = Translator(service_urls=['translate.googleapis.com'])
    res = translator.translate(text1, dest=src)

    # ans = {"status": res.text}
    return res.text


if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=8989)
