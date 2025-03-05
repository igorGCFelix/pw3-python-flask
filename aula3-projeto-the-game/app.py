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
