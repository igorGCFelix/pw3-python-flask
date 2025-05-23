<<<<<<< HEAD
from flask import render_template, request, redirect, url_for

# Lista de jogadores
jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']

# Array de objetos - Lista de games
gamelist = [{'Título': 'CS-GO',
            'Ano': 2012,
             'Categoria': 'FPS Online'}]


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
=======
from flask import render_template, request

jogadores = ['iruah', 'davi_lambari', 'edsongf',
             'kioto', 'black.butterfly', 'jujudopix'
             ]

# Array de objetos
gameList = [{
        'Título': 'CS-GO',
        'Ano': 2012,
        'Categoria': 'FPS Online'}]

consoleList = [{
    'Nome' : 'Nintendo Wii',
    'Preço' : '950',
    'Ano' : '1999',
    'Empresa' : 'Nintendo'
}]

def init_app(app):
    # Criando a rota principal do site

    @app.route('/')
    # Criando a função no Python
    # View function - Função de visualização
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # Acessando o primeiro jogo da lista de jogos
        game = gameList[0]

        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
            # jogador = name do input

        outrosJogos = ['Elden Ring', 'Subnautica', 'Rainbow Six Siege',
                       'Rocket League', 'Cuphead', 'Hollow Knight', 'Red Dead Redemption 2']
        return render_template('games.html', game=game, jogadores=jogadores, outrosJogos=outrosJogos)
        # jogadores = jogadores, pega o jogadores do python e declara no html
    
    @app.route('/cadgames' , methods=['GET','POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gameList.append({'Título': request.form.get('titulo'),
                                 'Ano' : request.form.get('ano'),
                                 'Categoria' : request.form.get('categoria')})
                
        return render_template('cadgames.html', gameList=gameList)
    
    @app.route('/consoles' , methods=['GET','POST'])
    def cadconsoles():
        console = consoleList[0]

        
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('preco') and request.form.get('pais') and request.form.get('empresa'):
                consoleList.append({
                    'Nome' : request.form.get('nome'),
                    'Preço' : request.form.get('preco'),
                    'Ano' : request.form.get('ano'),
                    'Empresa' : request.form.get('empresa')
                })
                
        return render_template('consoles.html', consoleList=consoleList)
    
    

>>>>>>> 59e748e6d2df57b0eedac1d8f3e262ff4a2e343c
