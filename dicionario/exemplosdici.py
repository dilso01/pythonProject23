# dic = {'jonas': 'jonasreiter@hotmail.com',
#         'susan': 'susan.reiter@hotmail.com',
#          'professora': 'contato@reiter.page'}
# #
# # print(dic['susan'])
# #
# #
# # adicionar um item ao dicionario
# # dic['acesso'] = 'entra21@acesso.com.br'
# # dic['Adilson'] = 'dilso@gamil.com'
# #
# # print(dic.get('Adilson', 'não existe'))
# # print((dic))
# # atualizar o dicionario, nunca tera dois nomes iguas em um dicionario
# # dic['susan'] = 'susan@gmail.com'
# # print(dic)
# # #outra forma usar o update dessa forma você consegue atualizar mais de um iten por vez
# # dic.update({'jonas': 'jonas123@hotmail.com'})
# # # trocar o nome de uma chave dentro da lista
# # dic['professaura'] = dic.pop('professora')
# # print(dic)
# #
# #
# # dic['professora'] = dic['professaura']
# # del dic ['professaura']
# # print(dic)
# #
# # #para imprimir as chaves do dicionario
# # print(dic.keys())
# #
# # #para imprimir os valores do dicionario
# # print(dic.values())
# #
# # #para percorrer os itens do dicionario
# # for i in dic:
# #     print([i])
# # # para percorrer todos valores do dicionario
# # for i in dic:
# #     print(dic[i])
# #
# # # para percorrer o dicionario completo
# #
# # for k, v in dic.itens():
# #     print(f'{k} ------{v}')
# #
# # #deletar um iten especifico
# # dic.pop('susan')
# # print(dic.values())
# #
# # #para deletar o ultimo item do dicionario
# # dic.popitem()
# # print(dic.values())
# #
# # #verificar se um item esta nas chaves dicionario
# #
# # if 'casimiro' in dic:
# #     print('encontrei')
# # else:
# #     print('nops')
# #
# # #para saber se o item está no diconário
# #
# # if 'jonasreiter@hotmail.com' in dic.values():
# #     print('Encontrei')
# # else:
# #     print('nops')
# #
# # #criar um dicionario a partir de uma lista
# #
# # chaves = ['a', 'b', 'c']
# # valor = 0
# # novo_dic = dict.fromkeys((chaves, valor))
# # print(novo_dic)
#
# #dicionário que vem de duas listas
# lista1 = ['Jonas', 'raul', 'stefan']
# lista2 = [30, 30, 50]
# dic3 = {}
# for i in range(len(lista1)):
#     dic3[lista1[i]] = lista2[i]
#     print(dic3)
#
#
# # para juntar dois dicionários
# dic4 = {**dic, **dic3}
#
# #para limpar uma lista
# dic.clear() # para usar no meio do codigo usar o clear, pra ser mais facil de entender
# dic = {}  #limpa da mesma forma, só que nao é tao explicito no meio do codigo
# print(dic)
