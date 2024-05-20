from flask import Flask, url_for, render_template

#inicialização
app = Flask (__name__)

#rotas
@app.route('/')
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "João", "membro_ativo": False},
        {"nome": "Maria", "membro_ativo": False},
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return """
        <b>Acecsse o meu GitHub para mais informações: </b>
        <a href="https://github.com/Matheus-ALima">Matheus Alves Lima</a>
    """

#execução
app.run(debug=True)