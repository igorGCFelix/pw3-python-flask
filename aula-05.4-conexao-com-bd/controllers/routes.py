from flask import render_template, request, redirect, url_for
from models.database import Game, db

# Lista de jogadores
jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']

# Array de objetos - Lista de games
gamelist = [{'Título': 'CS-GO',
            'Ano': 2012,
             'Categoria': 'FPS Online'}]

consolelist = [{'Nome': '',
                'Preço': '',
                'País': ''}]


def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no Python
    def home():
        return render_template('index.html')

    # Rota de games
    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # Verificar se o campo 'jogador' existe
            if request.form.get('jogador'):
                # O append adiciona o item a lista
                jogadores.append(request.form.get('jogador'))
            return redirect(url_for('games'))

        jogos = ['Jogo 1', 'Jogo 2', 'Jogo 3', 'Jogo 4', 'Jogo 5', 'Jogo 6']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)
    
    # Rota de cadastro de jogos (em dicionário)
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               gamelist=gamelist)
        
    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        console = consolelist[0]
        if request.method == 'POST':
            if request.form.get('nomeConsole') and request.form.get('precoConsole') and request.form.get('paisConsole'):
                consolelist.append({'Nome': request.form.get('nomeConsole'),
                                    'Preço': request.form.get('precoConsole'),
                                    'País': request.form.get('paisConsole')})
        return render_template('consoles.html', consolelist=consolelist, console=console)


    # Rota do CRUD (Estoque de jogos)
    @app.route('/estoque', methods=['GET','POST'])
    @app.route('/estoque/<int:id>')
    def estoque(id=None):
        # Se o id for passado, então é para excluir o jogo
        if id:
            game = Game.query.get(id)
            # Deleta o jogo do banco
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))
        
        if request.method == 'POST':
            #Cadastrando o jogo no banco de dados:
            newgame = Game(request.form['titulo'], request.form['ano'], request.form['categoria'], request.form['plataforma'], request.form['preco'])
            db.session.add (newgame)
            db.session.commit()
            return redirect(url_for('estoque'))
            
        # ORM que estamos usando é a SQLAlchemy
        # O método query.all = SELECT * from...
        gamesEmEstoque = Game.query.all()
        return render_template('estoque.html', gamesEmEstoque=gamesEmEstoque)