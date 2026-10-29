from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/usuarios/listar')
def listar_usuarios():
    return render_template('usuarios/usuarios-listar.html')

if __name__ == '__main__':
    app.run(debug=True)

