from flask import Flask
# Importando a biblioteca
# importando instância da classe Flask


app = Flask(__name__) #Instancia da classe Flask


@app.route("/") #Decorador sempre antes de função
#aplica o metodo antes da função
#faz a rota da pagina
def index():
	return "Hello World"


#verifica se está executando
if __name__ == "__main__":
	app.run()


