from flask import Flask, render_template, request
import parseXml

app = Flask(__name__, template_folder='../templates')


@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('main.html')


@app.route('/puncte_vamale', methods=['POST', 'GET'])
def puncte_vamale():

    data = {}

    if request.method == "POST":
        searched_punct_vamal = request.form.get('punct_vamal')
        parser = parseXml.Parser()

        if searched_punct_vamal == "*":
            result = parser.get_puncte_vamale()
        else:
            result = parser.get_punct_vamal(str(searched_punct_vamal).lower())

        data = {
            'result': str(result)
        }

    return render_template('puncte_vamale.html', data=data)


@app.route('/punctVamalInControlSporit', methods=['POST', 'GET'])
def punctVamalInControlSporit():

    data = {}

    if request.method == "POST":
        punct_vamal_searched = request.form.get('punct_vamal_sporit')
        parser = parseXml.Parser()
        result = parser.check_punct_vamal_in_control_sporit(
            str(punct_vamal_searched))
        data = {
            'result': str(result)
        }

    return render_template('punctVamalInControlSporit.html', data=data)


@app.route('/persoane', methods=['POST', 'GET'])
def persoane():

    data = {}
    if request.method == "POST":
        persoana_searched = request.form.get('persoana')
        parser = parseXml.Parser()
        result = parser.get_persoana(str(persoana_searched).lower())
        data = {
            'result': str(result)
        }

    return render_template('persoane.html', data=data)


# @app.route('/ceaMaiScurtaCoada', methods=['POST', 'GET'])
# def ceaMaiScurtaCoada():

#     data = {}

#     if request.method == "POST":

#         supermarket_searched = request.form.get('supermarket')

#         parser = parseXml.Parser()

#         argin = {
#             'supermarket': str(supermarket_searched).lower()
#         }

#         result = parser.get_predicat('ceaMaiScurtaCoada', argin)

#         data = {
#             'result': str(result)
#         }

#     return render_template('ceaMaiScurtaCoada.html', data=data)


# @app.route('/ceaMaiLungaCoada', methods=['POST', 'GET'])
# def ceaMaiLungaCoada():

#     data = {}

#     if request.method == "POST":

#         supermarket_searched = request.form.get('supermarket')

#         parser = parseXml.Parser()

#         argin = {
#             'supermarket': str(supermarket_searched).lower()
#         }

#         result = parser.get_predicat('ceaMaiLungaCoada', argin)

#         data = {
#             'result': str(result)
#         }

#     return render_template('ceaMaiLungaCoada.html', data=data)


# @app.route('/existaCasaLibera', methods=['POST', 'GET'])
# def existaCasaLibera():

#     data = {}

#     if request.method == "POST":

#         supermarket_searched = request.form.get('supermarket')

#         parser = parseXml.Parser()

#         argin = {
#             'supermarket': str(supermarket_searched).lower()
#         }

#         result = parser.get_predicat('existaCasaLibera', argin)

#         data = {
#             'result': str(result)
#         }

#     return render_template('existaCasaLibera.html', data=data)
