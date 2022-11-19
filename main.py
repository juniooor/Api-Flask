from flask import Flask
from database import db
from flask_migrate import Migrate

app = Flask(__name__)
db.init_app(app)
conexao = "sqlite:///mybd.sqlite" 


app.config['SECRET_KEY'] = 'senha'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

Migrate = Migrate(app, db)



@app.route('/')
def index():
    return 'Hello World'



app.run()