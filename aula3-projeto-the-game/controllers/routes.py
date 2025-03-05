from flask import render_template, request

jogadores = ['iruah', 'davi_lambari', 'edsongf',
                 'kioto', 'black.butterfly', 'jujudopix']

def init_app(app):
    # Criando a rota principal do site


    @app.route('/')
    # Criando a função no Python
    # View function - Função de visualização
    def home():
        return render_template('index.html')


    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = {
            'Título': 'CS-GO',
            'Ano': 2012,
            'Categoria': 'FPS Online'
        }

        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
            # jogador = name do input
        
        outrosJogos = ['Elden Ring', 'Subnautica', 'Rainbow Six Siege',
                   'Rocket League', 'Cuphead', 'Hollow Knight', 'Red Dead Redemption 2']
        return render_template('games.html', game=game, jogadores=jogadores, outrosJogos=outrosJogos)
# jogadores = jogadores, pega o jogadores do python e declara no html
