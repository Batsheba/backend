from flask import Flask


app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Bienvenido a mi API '

@app.route('/bienvenido')
def bienvenido():
    return 'Bienvenido a la API de Bat'

@app.route('/home')
def bienvenido_home():
    return 'Bienvenido al psicologo '

if __name__=='__main__':
        app.run(debug=True, port=3000)