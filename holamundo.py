from flask import Flask
from flask import request

app = Flask(__name__) # nuevo objeto 

#indicar a que ruta usamos un decorador 

@app.route('/') #decorador le indica las rutas 
def index():
    return "Hola Mundo" #regresa un string 

@app.route('/saludo')
def saludo():
    return "Saludos"

#Pasar parametros 
#http://127.0.0.1:5000/params?params1=g
@app.route('/params')
def params():
    param = request.args.get('params1', 'no tiene parametros')
    return f"El paramentro es {param}"   # o puede ser con format    'El parametro es {}'.format(param)

@app.route('/hola/')
@app.route('/hola/<string:nombre>')
def hola(nombre =  'valor por default'):
    return f"<h1>Hola {nombre}</h1>"   # o puede ser con format    'El parametro es {}'.format(param)   o "Hola" + nombre


if __name__ == '__main__':
    app.run(debug=True)  #ejecuta el servidor por default en el puerto 5000 