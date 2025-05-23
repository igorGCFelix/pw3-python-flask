<<<<<<< HEAD
# comentario em python #
# Importando o pacote do Flask
from flask import Flask, render_template

# Carregando o Flask na variável app
# template_folder diz onde estará a a pasta páginas html
# render_template biblioteca para renderizar a página
app = Flask(__name__, template_folder='views')

# Criando a rota principal do site


@app.route('/')
# Criando a função no Python
# View function - Função de visualização
def home():
    return render_template('index.html')


@app.route('/games')
def games():
    game = {
        'Título': 'CS-GO',
        'Ano': 2012,
        'Categoria': 'FPS Online'
    }

    jogadores = ['iruah', 'davi_lambari', 'edsongf',
                 'kioto', 'black.butterfly', 'jujudopix']
    outrosJogos = ['Elden Ring', 'Subnautica', 'Rainbow Six Siege',
                   'Rocket League', 'Cuphead', 'Hollow Knight', 'Red Dead Redemption 2']
    return render_template('games.html', game=game, jogadores=jogadores, outrosJogos=outrosJogos)
# titulo = titulo, pega o titulo do python e declara no html


# Rodando o servidor no localhost, porta 5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
=======
# comentario em python #
# Importando o pacote do Flask
from flask import Flask, render_template

# Carregando o Flask na variável app
# template_folder diz onde estará a a pasta páginas html
# render_template biblioteca para renderizar a página
app = Flask(__name__, template_folder='views')

# Criando a rota principal do site


@app.route('/')
# Criando a função no Python
# View function - Função de visualização
def home():
    return render_template('index.html')


@app.route('/games')
def games():
    game = {
        'Título': 'CS-GO',
        'Ano': 2012,
        'Categoria': 'FPS Online'
    }

    jogadores = ['iruah', 'davi_lambari', 'edsongf',
                 'kioto', 'black.butterfly', 'jujudopix']
    outrosJogos = ['Elden Ring', 'Subnautica', 'Rainbow Six Siege',
                   'Rocket League', 'Cuphead', 'Hollow Knight', 'Red Dead Redemption 2']
    return render_template('games.html', game=game, jogadores=jogadores, outrosJogos=outrosJogos)
# titulo = titulo, pega o titulo do python e declara no html


# Rodando o servidor no localhost, porta 5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
>>>>>>> 59e748e6d2df57b0eedac1d8f3e262ff4a2e343c
