from flask import Flask, render_template,url_for,redirect,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content=['fabas','bafas','chabas'], r=2)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        usuario=request.form["nm"]
        genero=request.form["genero"]
        return redirect(url_for("user",usuario=usuario, genre=genero))
    else:
        return render_template("login.html")

@app.route("/<usuario>/<genre>")
def user(usuario,genre):
    return f"<h1>{usuario} e {genre}</h1>"

if __name__ == "__main__":
    app.run(debug=True)