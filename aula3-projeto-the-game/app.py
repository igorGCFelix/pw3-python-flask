<<<<<<< HEAD
# Importando o Flask
from flask import Flask, render_template
# Importando as rotas que estão nos controllers
from controllers import routes

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Chamando as rotas
routes.init_app(app)

# Iniciando o servidor no localhost, porta 5000, modo de depuração ativado
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
=======
# comentario em python #
# Importando o pacote do Flask
from flask import Flask
from controllers import routes

# Carregando o Flask na variável app
# template_folder diz onde estará a a pasta páginas html
# render_template biblioteca para renderizar a página
app = Flask(__name__, template_folder='views')

# Enviando o Flask (app) para a função init_app do routes
routes.init_app(app)

# Rodando o servidor no localhost, porta 5000
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
>>>>>>> 59e748e6d2df57b0eedac1d8f3e262ff4a2e343c
