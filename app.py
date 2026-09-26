from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clientes.sqlite3"
app.secret_key = "key_clientes"
db = SQLAlchemy(app)

#CRIAÇÃO DA TABELA

class Clientes(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(40), nullable=False)
    cargo_cliente = db.Column(db.String(40), nullable=False)
    salario_cliente = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

    def __init__(self, nome_cliente, cargo_cliente,salario_cliente):
        self.nome_cliente = nome_cliente
        self.cargo_cliente = cargo_cliente
        self.salario_cliente = salario_cliente
        
#ROTA HOME

@app.route("/")
def home():
    return render_template("index.html")

#ROTA CADASTRO

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():

    if request.method =='POST':

        nome = request.form.get("nome_cliente")
        cargo = request.form.get("cargo_cliente")
        salario = request.form.get("salario_cliente")

        try:
            salario = float(salario)

            novo_cliente = Clientes(nome,cargo,salario)
            db.session.add(novo_cliente)
            db.session.commit()
            flash("Cliente cadastrado com sucesso!", "success")

            # Redireciona para evitar re-envio do formulário ao dar F5
            return redirect(url_for("cadastrar"))

        except Exception as e:
            db.session.rollback()
            flash(f"Ocorreu um erro ao cadastrar o cliente: {e}", "danger")

    return render_template("cadastrar.html")

#ROTA LISTAR

@app.route('/listar',)
def listar():
    clientes = Clientes.query.all()
    return render_template("listar.html", clientes=clientes)

#ROTA EDITAR

@app.route('/editar', methods=["GET","POST"])
def editar():
    return render_template("editar.html")

#DEBUGGING AND DATABASE CREATION

if __name__ ==  "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)