from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('contato.html')

@app.route('/contato')
def contato():
    return 'Pagina de contato'

if __name__ == '__main__':
    app.run()