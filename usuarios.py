from flask import Blueprint
from flask import render_template, request
from models import Usuario
from database import db

bp_usuarios = Blueprint("usuarios", __name__, template_folder= 'templates')

@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=='GET':
        return render_template('usuarios_create.html')
    
    if request.method=='POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')
        
        u = Usuario(nome, email, senha)
        db.session.add(u)
        db.session.commit()
        return 'dados cadastrados com sucesso'
    
@bp_usuarios.route('/recovery')
def recovery():
    usuarios = Usuario.query.all()
    return render_template('usuarios_recovery.html', usuarios=usuarios )


@bp_usuarios.route('/update/<int:id>')
def update(id):
    u = Usuario.query.get(id)
    return render_template('usuarios_update.html', u = u)