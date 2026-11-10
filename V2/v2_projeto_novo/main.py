from flask import Flask, render_template, url_for

formula = Flask(__name__)

@formula.route('/')
def home():
    return render_template('home.html')

@formula.route('/sobre')
def sobre():
    return render_template('sobre.html')

@formula.route('/contatos')
def contatos():
    return render_template('contato.html')

@formula.route('/calendario')
def calendario():
    return render_template('calendario.html') 

@formula.route('/pilotos_e_equipes')
def pilotos_equipes():
    return render_template('pilotos_equipes.html')

if __name__ == '__main__':
    formula.run(debug=True, port=5001)
