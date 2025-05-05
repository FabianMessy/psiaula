from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

# Dicionário fixo de recomendações
RECOMENDACOES = {
    'acao': ['Missão Impossível', 'Mad Max', 'John Wick'],
    'comedia': ['Se Beber, Não Case', 'Gente Grande', 'As Branquelas'],
    'drama': ['Clube da Luta', 'A Procura da Felicidade', 'O Quarto de Jack'],
    'ficcao': ['Interestelar', 'Matrix', 'Duna'],
    'terror': ['Invocação do Mal', 'O Iluminado', 'Hereditário']
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        genero = request.form.get('genero')
        notificacoes = 'sim' if request.form.get('notificacoes') else 'nao'

        resp = make_response(redirect('/preferencias'))
        resp.set_cookie('nome', nome, max_age=7*24*60*60)
        resp.set_cookie('genero', genero, max_age=7*24*60*60)
        resp.set_cookie('notificacoes', notificacoes, max_age=7*24*60*60)
        return resp

    return render_template('cadastro.html')

@app.route('/preferencias')
def preferencias():
    nome = request.cookies.get('nome')
    genero = request.cookies.get('genero')
    notificacoes = request.cookies.get('notificacoes')

    if not nome or not genero:
        return render_template('preferencias.html', dados=None)

    dados = {
        'nome': nome,
        'genero': genero,
        'notificacoes': notificacoes
    }
    return render_template('preferencias.html', dados=dados)

@app.route('/recomendar')
def recomendar():
    genero = request.args.get('genero', '').lower()
    filmes = RECOMENDACOES.get(genero)

    return render_template('recomendar.html', genero=genero, filmes=filmes)
