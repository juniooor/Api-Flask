from flask import Blueprint
from flask import render_template, request

bp_usuarios = Blueprint("usuarios", __name__, template_folder= 'templates')

@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=='GET ':
        return render_template('usuarios_create.html')
    
    if request.method=='POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')
        return f'Dados recebidos \n Nome = {nome} \n Email = {email} \n Senha: {senha} \n Confirmação: {csenha}'