from flask import Flask, jsonify, request
#from (flask- biblioteca) import Flask, (jsonify- formato do arquivo), (request- acesar os dados dentro das requisições)
app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'As Crônicas de Gelo e Fogo',
        'autor': 'George R. R. Martin',
        'ano': 1997

    },
    {
        'id': 2,
        'título': 'Capitão America',
        'autor': 'George R. R. Martin',
        'ano': 1997


    },
    {
        'id': 3,
        'título': 'O Senhor dos Aneis',
        'autor': 'J. R. R. Tolkien',
        'ano': 1954
    }


]
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
def obter_livros_por_id(id):
    for l in livros:
        if l['id'] == id:
            return jsonify(l)

app.run(port=5000,host='localhost',debug=True)