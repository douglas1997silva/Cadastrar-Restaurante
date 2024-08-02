#print('Dados')

#id = input('Id:')
#nome = input('Qual e seu Nome?')
#idade = input('Quantos Anos voçes tem ?')
#email = input('Qual e seu E-mail?')

#print(f'Nome: {nome}',f'Idade:{idade}',f'E-mail:{email}', sep='\n')

pessoa = int(input('Sua idade para idetificar se voce pode votar : '))



if pessoa <= 15:
    print('Voce e de Menor Infelizmente Complete 16 anos para a votação ')
elif pessoa >= 16 and pessoa < 18:
    print('Não e Obrigatorio Votar! ')
else:
    print('Voce deve votar ')





numero = int(input('Insira um numero : '))

if numero % 2 == 0:
    print(f'o {numero} é par')
else:
    print(f'o {numero} ´e impar')

    

classificacao = int(input('Vamos verificar sua idade ? '))

if classificacao >= 0 and classificacao <= 12 :
    print(f'Sua classificação e de Criança entre 0 a 12 Anos ')
elif classificacao >= 13 and classificacao <= 18 :
    print(f'Sua classificação e de Adolescente entre 13 a 18 Anos ')
else:
    print('Sua classificação e de Adulto acima de 18 Anos ')

usuario = 'douglas'
passoword = 'passatempo12'
loguin = input('Insira um o Loguin:')
senha = input('Insira sua senha:')

if loguin == usuario and senha == passoword:
    print('Bem vindo ao APP')
else:
    print('Tente novamente ')



