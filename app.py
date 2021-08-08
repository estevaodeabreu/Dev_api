from flask import Flask, jsonify,request
import json


app = Flask(__name__)

desenvolvedores = [
    {'id':'0','nome':'Estevão',
     'habilidades':['python','Flask','Linux','Git e GITHUB','MySQL']},
    {'id':'1','nome': 'Andre',
     'habilidades':['Python','Ciência de dados','Engenharia de dados','Automação','Pesquisa']}
]
# devolve um desenvolvedor pelo id, também altera e deleta um desenvolvedor.

@app.route('/dev/<int:id>/',methods=['GET','PUT',   'DELETE'])

def desenvolvedor(id):
    if request.method == 'GET':
        try:
             response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = ({'status':'erro', 'mensagem':mensagem })
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador da API'
            response = ({'status': 'erro', 'mensagem': mensagem})
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE' :
        desenvolvedores.pop(id)
        return ({'status':'sucesso','mensagem': 'registro excluido'})


# Lista todos os desenvolvedores e permite o registro de novos desenvolvedores.

@app.route('/dev/',methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posisao = len(desenvolvedores)
        dados['id'] = posisao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posisao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)




if __name__ == '__main__':
    app.run(debug=False)