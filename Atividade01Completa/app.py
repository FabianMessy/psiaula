from flask import Flask, render_template,redirect,request,make_response

app = Flask(__name__)

#dicionario gerado por ia
RECOMENDACOES = {
    'acao': ['Missão Impossível', 'Mad Max', 'John Wick'],
    'comedia': ['Se Beber, Não Case', 'Gente Grande', 'As Branquelas'],
    'drama': ['Clube da Luta', 'A Procura da Felicidade', 'O Quarto de Jack'],
    'ficcao': ['Interestelar', 'Matrix', 'Duna'],
    'terror': ['Invocação do Mal', 'O Iluminado', 'Hereditário']
}

#Homee
@app.route("/")
def home():
    return render_template("index.html")

#pagina de cadastro das preferencias
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        nome=request.form["nm"] #pega o nome do usuario
        genero=request.form["genero"] #pega o genero de filme que ele escolheu
        #verifica e altera o "notificacoes" baseado na checkbox
        if request.form.get('notificacoes'):
            notificacoes = 'sim' 
        else:
            notificacoes = 'nao'

        #So da pra usar o set_cookie dps de fazer uma make_response e no caso essa ai redireciona para a pagina de preferencias
        resposta=make_response(redirect("preferencias")) #Cria uma resposta HTTP de redirecionamento para preferencias, o make response permite que você modifique a resposta assim eu adiciono os cookies.
        resposta.set_cookie("nome",nome,max_age=604800) #cria um cookie com nome de nome q pega o valor da variavel usuario e dura 7 dias
        resposta.set_cookie("genero",genero,max_age=604800)
        return resposta #retorna o redirecionamento com os cookies
    return render_template("login.html")



@app.route("/preferencias")
def preferencias():
    nome=request.cookies.get("nome")
    genero=request.cookies.get("genero")
    
    if not nome or not genero:
        return render_template("preferencias.html")
    return render_template("preferencias.html", nome=nome, genero=genero)


@app.route('/recomendar')
def recomendar():
    genero = request.args.get('genero', '').lower() #isso aq pega a url dps da "?" ou seja ?genero=acao fica genero = acao
    filmes = RECOMENDACOES.get(genero)

    return render_template('recomendar.html', genero=genero, filmes=filmes)
if __name__ == "__main__":
    app.run(debug=True)