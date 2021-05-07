import os
from flask import Flask, request, render_template, send_file, url_for, redirect
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from io import BytesIO


app = Flask(__name__, template_folder ='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trabalhos.sqlite3'

db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column (db.String, unique=True, nullable=False)
    autores = db.Column(db.String)
    orientadores = db.Column(db.String)
    instituicao = db.Column(db.String)
    tipo = db.Column(db.String)
    palavras_chave = db.Column(db.String)
    resumo = db.Column(db.String)
    data = db.Column (db.LargeBinary)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column (db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    tipo = db.Column(db.String)
    senha = db.Column(db.String)
    departamento = db.Column(db.String)


@app.route('/upload', methods=['POST'])
def upload():
    trabalho = Item(name=request.form['name'], autores=request.form['autores'],
                    orientadores=request.form['orientadores'], instituicao=request.form['instituicao'],
                    tipo=request.form['tipo'], palavras_chave=request.form['palavras_chave'],
                    resumo=request.form['resumo'], data=request.files['file'].read())
    db.session.add(trabalho)
    db.session.commit()
    return '<h3>Upload feito com sucesso<h3> <br> <br> <li><a href="/index">Pagina Inicial</a></li><li><a href="/cadastrarTrabalho ">Novo Cadastro</a></li>'


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    coord = User(nome=request.form['nome'], email=request.form['email'],
                 senha=request.form['senha'], departamento=request.form['departamento'],
                 tipo='Coordenador')
    db.session.add(coord)
    db.session.commit()
    return '<h3>Coordenador cadastrado com sucesso<h3> <br> <br> <li><a href="/index">Pagina Inicial</a></li><li><a href="/cadastrarTrabalho ">Novo Cadastro</a></li>'



@app.route('/', methods=['GET'])
def index():
    items = Item().query.all()
    return render_template('index.html', items= items)

@app.route('/index', methods=['GET'])
def ind():
    items = Item().query.all()
    return render_template('index.html', items= items)


@app.route('/download/<int:id>', methods=['GET'])
def download(id):
    item = Item().query.filter_by(id=id).first()
    return send_file(BytesIO(item.data), as_attachment=True, attachment_filename=item.name, cache_timeout=0)


@app.route('/extract/<int:id>', methods=['GET'])
def extract(id):
    item = Item().query.filter_by(id=id).first()
    return render_template('dados.html', item= item)


@app.route('/cadastrarTrabalho')
def cadastrarTrabalho():
    return render_template('cadastrarTrabalho.html')


@app.route('/loginAdmin', methods=['POST'])
def loginAdmin():
    user = User().query.filter_by(nome=request.form['username'],senha=request.form['password'],tipo='Administrador').first()
    if(user or (request.form['username']=='Admin' and request.form['password']=='1234')):
        return render_template('administrador.html')
    return render_template('loginAdministrador.html')


@app.route('/loginCoord', methods=['POST'])
def loginCoord():
    user = User().query.filter_by(nome=request.form['username'],senha=request.form['password'],tipo='Coordenador').first()
    if(user):
        return render_template('coordenador.html')
    return render_template('loginCoordenador.html')


@app.route('/administrador')
def administrador():
    return render_template('administrador.html')


@app.route('/cadastrarCoordenador')
def cadastrarCoordenador():
    return render_template('cadastrarCoordenador.html')


@app.route('/coordenador')
def coordenador():
    return render_template('coordenador.html')


@app.route('/loginAdministrador')
def loginAdministrador():
    return render_template('loginAdministrador.html')


@app.route('/loginCoordenador')
def loginCoordenador():
    return render_template('loginCoordenador.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)