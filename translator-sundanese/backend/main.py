from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from Hasil import hasil


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/sundanese-translator', methods=["POST"])
@cross_origin()
def main():
    data = request.get_json()
    menu = data['menu']
    kalimat = data['kalimat']
    hasilTranslate = hasil(menu, kalimat)
    return jsonify({'data': hasilTranslate}), 200
