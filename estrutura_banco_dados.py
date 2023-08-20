from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar uma API com flask
app = Flask(__name__)

# Criar uma instancia de SQLAlchemy
app.config['SECRET_KEY'] = '#Asdf1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
db: SQLAlchemy


# Definir a estrutura da tabela Postagem
# id_postagem, titulo, autor
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))


# Definir a estrutura da tabela Autor
# id_autor, nome, email, senha, admin, postagem
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem', backref='autor')


def inicializar_banco():
    # Executar o comando para criar o banco de dados

    db.drop_all()
    db.create_all()

    # Criar usuarios administradores
    autor = Autor(nome='admin', email='admin@admin.com.br', senha='123456',
                  admin=True)
    db.session.add(autor)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        inicializar_banco()
