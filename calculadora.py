class Calculadora:
    """
    Classe que representa uma calculadora simples com operações básicas.

    @autor: Florensa Dimer
    @data: 2023-10-05
    """
    def __init__(self, num1, num2):
        """
        Inicializa a calculadora com dois números.

        Args:
            num1 (float): O primeiro número.
            num2 (float): O segundo número.
        """
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        """
        Retorna a soma dos dois números.

        Returns:
            float: A soma de num1 e num2.
        """
        return self.num1 + self.num2

    def subtracao(self):
        """
        Retorna a subtração dos dois números.

        Returns:
            float: A diferença entre num1 e num2.
        """
        return self.num1 - self.num2

    def multiplicacao(self):
        """
        Retorna a multiplicação dos dois números.

        Returns:
            float: O produto de num1 e num2.
        """
        return self.num1 * self.num2

    def divisao(self):
        """
        Retorna a divisão dos dois números.

        Returns:
            float: O quociente de num1 e num2 se num2 não for zero.
            str: Mensagem de erro se num2 for zero.
        """
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return 'Erro: Divisão por zero'