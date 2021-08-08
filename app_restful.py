from flask import Flask,request,json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':'0','nome':'Estevão',
     'habilidades':['python','Flask','Linux','Git e GITHUB','MySQL']},
    {'id':'1','nome': 'Andre',
     'habilidades':['Python','Ciência de dados','Engenharia de dados','Automação','Pesquisa']}
]

class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = ({'status': 'erro', 'mensagem': mensagem})
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador da API'
            response = ({'status': 'erro', 'mensagem': mensagem})
        return response

    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self,id):
        desenvolvedores.pop(id)
        dados = json.loads(request.data)
        return ({'status':'sucesso','mensagem': 'registro excluido'})


# Lista todos os desenvolvedores e permite o registro de novos desenvolvedores.
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posisao = len(desenvolvedores)
        dados['id'] = posisao
        desenvolvedores.append(dados)
        return desenvolvedores[posisao]


api.add_resource(Desenvolvedor,'/dev/<int:id>')
api.add_resource(ListaDesenvolvedores,'/dev')


if __name__ == '__main__':
    app.run(debug=True)
