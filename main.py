from app import App

import os
import subprocess
import sys
import webbrowser
import urllib.request

class Main:
    """
    Classe Principal que gerencia a verificação, instalação do Flask e execução do aplicativo em Python.

    @autor: Florensa Dimer
    @data: 2023-10-05
    """
    def __init__(self):
        """
        Inicializa a classe Principal, verificando e instalando o Flask se necessário,
        e criando uma instância da classe App.
        """
        self.verificar_e_instalar_python()
        self.verificar_e_instalar_flask()
        self.app = App()

    def verificar_e_instalar_python(self):
        """
        Verifica se a versão mais recente do Python está instalada. Se não estiver, baixa e instala.
        """
        try:
            version = sys.version_info
            if version < (3, 10):
                self.instalar_python()
        except Exception as e:
            print(f"Erro ao verificar a versão do Python: {e}")
            self.instalar_python()

    def instalar_python(self):
        """
        Baixa e instala a versão mais recente do Python.
        """
        try:
            url = "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe"
            instalador = "python_installer.exe"
            urllib.request.urlretrieve(url, instalador)
            subprocess.run([instalador, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
            os.remove(instalador)
        except Exception as e:
            print(f"Erro ao instalar o Python: {e}")

    def verificar_e_instalar_flask(self):
        """
        Verifica se o Flask está instalado. Se não estiver, chama o método para instalar o Flask.
        """
        try:
            import flask
        except ImportError:
            self.instalar_flask()

    def instalar_flask(self):
        """
        Instala o Flask usando o pip.
        """
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])

    def executar(self):
        """
        Abre o navegador padrão na URL do aplicativo Flask e executa o aplicativo.
        """
        webbrowser.open("http://127.0.0.1:5000")
        self.app.run()

if __name__ == "__main__":
    """
    Ponto de entrada do programa. Cria uma instância da classe Principal e chama o método executar.
    """
    principal = Main()
    principal.executar()