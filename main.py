from flask import Flask
from database import db
from flask_migrate import Migrate
from usuarios import bp_usuarios

app = Flask(__name__)
conexao = "sqlite:///mybd.sqlite" 


app.config['SECRET_KEY'] = 'senha'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')

db.init_app(app)
Migrate = Migrate(app, db)



@app.route('/')
def index():
    return 'Hello World'



app.run()