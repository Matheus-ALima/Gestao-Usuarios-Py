from flask import Blueprint

#inicia o blueprint
cliente_route = Blueprint('cliente', __name__)

#definindo as rotas
@cliente_route.route('/')
def lista_clientes():
    pass

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    pass

@cliente_route.route('/new')
def form_cliente():
    pass

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_editaCliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualiza_dadoCliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deleta_cliente(cliente_id):
    pass