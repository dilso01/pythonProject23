'''A empresa JONASREITER PRODUCTIONS vende cursos da área da educação. Após a mudança de sistema,
o cadastro de clientes ficou embaralhado, onde acabou ficando em 2 arquivos .txt. Crie um programa que importe 2 arquivos .txt que contenham CNPJs. Ao final,
diga quantos itens estão duplicados

>Diga quantos CNPJs devem ser removidos para não ter mais CNPJs repetidos.
>quais são os CNPJS que estavam duplicados?
>Quantos CNPJs únicos realmente existem.
'''

#importar os arquivos e dizer quantos estao dupicados

arquivoantiga = open('clientes sistema antigo.txt','r').read().splitlines()
arquivoanovo = open('clientes sistema novo.txt', 'r').read().splitlines()

lista_completa = arquivoantiga + arquivoanovo
# >Diga quantos CNPJs devem ser removidos para não ter mais CNPJs repetidos.
print(len(lista_completa))
# Quantos CNPJs únicos realmente existem.
print(len(set(lista_completa)))
duplicados = set()
for i in lista_completa:
    if lista_completa.count(i) > 1:
        duplicados.add(i)
print(len(duplicados))
# >Quantos CNPJs únicos realmente existem.