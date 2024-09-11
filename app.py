from calculadora import Calculadora

# Biblioteca Python
from flask import Flask, render_template, request

class App:
    """
    Classe que configura e executa o aplicativo Flask.
    
    @autor: Florensa Dimer
    @data: 2023-10-05
    """
    
    def __init__(self):
        """
        Inicializa a classe App, criando uma instância do Flask e configurando as rotas.
        """
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        """
        Configura as rotas do aplicativo Flask.
        """
        @self.app.route('/')
        def index():
            """
            Rota para a página inicial que renderiza o template 'calculadora.html'.
            """
            return render_template('calculadora.html')

        @self.app.route('/calcular', methods=['POST'])
        def calcular():
            """
            Rota para calcular o resultado com base nos números e operação fornecidos pelo usuário.
            """
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operacao = request.form['operacao']

            calculadora = Calculadora(num1, num2)
            resultado = None

            if operacao == 'soma':
                resultado = calculadora.soma()
            elif operacao == 'subtracao':
                resultado = calculadora.subtracao()
            elif operacao == 'multiplicacao':
                resultado = calculadora.multiplicacao()
            elif operacao == 'divisao':
                resultado = calculadora.divisao()

            return render_template('calculadora.html', resultado=resultado)

    def run(self):
        """
        Executa o aplicativo Flask em modo debug.
        """
        self.app.run(debug=True)