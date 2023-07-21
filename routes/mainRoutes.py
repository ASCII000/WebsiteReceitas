from flask import Flask, Blueprint, render_template

postagens = [
    {
        'titulo': 'Receita de bolo de cenoura',
        'conteudo': 'Misture a cenoura com os ovos e óleo. Adicione os ingredientes secos e bata bem. Leve ao forno por aproximadamente 40 minutos. Cubra com calda de chocolate e sirva.',
        'imagem': '/static/img/bolo.png'
    },
    {
        'titulo': 'Receita de pizza caseira',
        'conteudo': 'Prepare a massa misturando farinha, água, fermento e sal. Deixe descansar por uma hora. Abra a massa, adicione molho de tomate, queijo e ingredientes de sua escolha. Asse em forno quente até dourar.',
        'imagem': '/static/img/pizza.png'
    },
    {
        'titulo': 'Sopa de legumes',
        'conteudo': 'Refogue cebola, alho e legumes de sua escolha em azeite. Adicione caldo de legumes e deixe cozinhar até que os legumes estejam macios. Bata a sopa no liquidificador até ficar cremosa. Sirva quente.',
        'imagem': '/static/img/sopa.png'
    },
    {
        'titulo': 'Salada de frutas',
        'conteudo': 'Corte diversas frutas em pedaços, como melão, melancia, morango, uva e manga. Misture tudo e adicione suco de limão e hortelã a gosto. Sirva gelado.',
        'imagem': '/static/img/salada.png'
    }
]

mainRoutes = Blueprint('main', __name__)

@mainRoutes.route('/')
def index():
    return render_template('index.jinja2', postagens=postagens)
