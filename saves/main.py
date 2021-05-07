import os
from flask import Flask, request, render_template, send_file, url_for, redirect
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder ='templates')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///novabase.sqlite3'

db = SQLAlchemy(app)

class Trabalho(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100))
    autores = db.Column(db.String(100))
    orientadores = db.Column(db.String(100))
    instituicao = db.Column(db.String(100))
    tipo = db.Column(db.String(100))
    palavras_chave = db.Column(db.String(100))
    resumo = db.Column(db.String(300))

    def __init__(self, titulo, autores, orientadores, instituicao, tipo, palavras_chave, resumo):
        self.titulo = titulo
        self.autores = autores
        self.orientadores = orientadores
        self.instituicao = instituicao
        self.tipo = tipo
        self.palavras_chave = palavras_chave
        self.resumo = resumo


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    return '<h3>Upload feito com sucesso<h3> <br> <br> <li><a href="/public/index.html">Pagina Inicial</a></li><li><a href="/public/cadastrarTrabalho.html">Novo Cadastro</a></li>'


@app.route('/get-file/<filename>')
def getFile(filename):
    file = os.path.join(UPLOAD_FOLDER, filename + '.pdf')
    return send_file(file)

@app.route('/index')
def index():
    trabalhos = Trabalho.query.all()
    return render_template('index.html', trabalhos=trabalhos)

@app.route('/cadastrarTrabalho')
def cadastrarTrabalho():
    return render_template('cadastrarTrabalho.html')

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

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        trabalho = Trabalho(request.form['titulo'], request.form['autores'], request.form['orientadores'], request.form['instituicao'], request.form['tipo'], request.form['palavras_chave'], request.form['resumo'])
        db.session.add(trabalho)
        db.session.commit()
        return redirect(url_for('/index'))
    return render_template('cadastrarTrabalho.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)