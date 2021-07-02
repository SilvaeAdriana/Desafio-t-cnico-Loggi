codigo_barras = input('Leia o código: ')
#codigo_barras_lista = [codigo_barras]
#print(codigo_barras.split(';',4))
#print(list(codigo_barras))

#pensar num programa que tanto pode pegar uma lista pronta ou aceitar novas entradas


lista = list(codigo_barras)
lista_de_pacotes =[' 888555555123888', ' 333333555584333', ' 222333555124000', ' 000111555874555',
' 111888555654777', ' 111333555123333', ' 555555555123888', ' 888333555584333', ' 111333555124000', 
' 333888555584333', '555888555123000', ' 111888555123555', ' 888000555845333', '000111555874000',
' 111333555123555']
#   COM FOR MUDA TUDO
# for produto in lista_de_pacotes (0,16):
if len(lista_de_pacotes) != 15:
  print('Código de barras inválido!')
else:
  #   CONDIÇÕES DE VALIDADE
  # Centro Oeste e produto 'joias'
  if lista_de_pacotes[2] == '1' and lista_de_pacotes[-1] == '0':
    print('Não é possível enviar.Há restrições, verificar.')
    # Tipos de produtos
    elif lista_de_pacotes[14] != '0' and lista_de_pacotes[14] != '1' and lista_de_pacotes[14] != '3'  and lista_de_pacotes[14] != '5' and lista_de_pacotes[14] != '8':
      print('Produto inválido!')
      # Vendedor inativo
      elif lista_de_pacotes[9:12] == '584':
        print('Código inválido: Vendedor com CNPJ inativo.')
continue

# Destinos e origens
centro_oeste = '111'
nordeste = '333'
norte = '555'
sudeste ='888'
sul = '000'


# tipos de produtos
joias = '000'
livros = '111'
eletronicos ='333'
bebidas = '555'
brinquedos = '888'





# destino
if lista[3:6] == '111':
    print('O destino do pacote é Centro Oeste')
elif lista[3:6] == '333':
    print('O destino do pacote é Nordeste')
elif lista[3:6] == '555':
    print('O destino do pacote é Norte')
elif lista[3:6] == '888':
    print('O destino do pacote é Sudeste')
elif lista[3:6] == '000':
    print('O destino do pacote é Sul')



count_centro_oeste = 0
count_nordeste = 0
count_norte = 0
count_sudeste = 0
count_sul = 0

while pacotes > 0:
    if lista[3:6] == '111':
        count_centro_oeste = count+1
    elif lista[3:6] == '333':
        count_nordeste = count+1
    elif lista[3:6] == '555':
        count_norte = count+1
    elif lista[3:6] == '888':
        count_sudeste = count+1
    elif lista[3:6] == '000':
        count_sul = count+1
    print (' A quantidade de pacotes da região Centro Oeste é de {}'.format(count_centro_oeste))
    print (' A quantidade de pacotes da região Nordeste é de {}'.format(count_nordeste))
    print (' A quantidade de pacotes da região Norte é de {}'.format(count_norte))
    print (' A quantidade de pacotes da região Sudeste é de {}'.format(count_sudeste))
    print (' A quantidade de pacotes da região Sul é de {}'.format(count_sul))



# Códigos de vendedor
vendedor1 = '123'
vendedor2 = '124'
vendedor3 = '874'
vendedor4 = '654'
vendedor5 = '845'

count_vendedor1 = 0
count_vendedor2 = 0
count_vendedor3 = 0
count_vendedor4 = 0
count_vendedor5 = 0
if lista[9:12] == '123':
    count_vendedor1 = count_vendedor1+1
elif lista[9:12] == '124':
    count_vendedor2 = count_vendedor2+1
elif lista[9:12] == '874':
    count_vendedor3 = count_vendedor3+1
elif lista[9:12] == '654':
    count_vendedor4 = count_vendedor4+1
elif lista[9:12] == '845':
    count_vendedor5 = count_vendedor5+1
print (' A quantidade de vendas do vendedor 1 foi de {}'.format(count_vendedor1))
print (' A quantidade de vendas do vendedor 2 foi de {}'.format(count_vendedor2))
print (' A quantidade de vendas do vendedor 3 foi de {}'.format(count_vendedor3))
print (' A quantidade de vendas do vendedor 4 foi de {}'.format(count_vendedor4))
print (' A quantidade de vendas do vendedor 5 foi de {}'.format(count_vendedor5))


#saber se algum pacote tem como origem a região Sul e brinquedos em seu conteúdo
if lista[0:3] == '000' and lista[12:15]:
    print('Pacote com origem da região Sul com brinquedo no interior.')
