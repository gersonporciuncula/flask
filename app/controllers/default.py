from app import app


@app.route("/") #Decorador sempre antes de função
#aplica o metodo antes da função
#faz a rota da pagina
def index():
	return "Hello World"
