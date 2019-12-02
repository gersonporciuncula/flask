from app import app


@app.route("/") #Decorador sempre antes de função
#aplica o metodo antes da função
#faz a rota da pagina
def index():
	return "Hello World"

@app.route("/teste", defaults={'nome': None})
@app.route("/teste/<nome>")
def teste(nome):
	if nome:
		return "Ola, %s!" % nome
	else:
		return "Olá, usuário!"