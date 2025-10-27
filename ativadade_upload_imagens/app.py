from flask import Flask, render_template
from controllers import routes
from models.database import db

app = Flask(__name__, template_folder='views')
routes.init_app(app)

# Configuração da chave secreta para sessões
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui_123456789'

# Usando SQLite em vez de MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///upload_imagens.db'

# UPLOAD de Imagem
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(host='localhost', port=5000, debug=True)
