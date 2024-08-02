
import os


usuario = [{'nome': 'Douglas','idade':26,'senha':1234,'ativo':True}]
def exibir_titulo():
 print('Bem vindo a J&C\n')

def exibir_menu():
    print('1. Cadastro')
    print('2. loguin')
    print('3. Usuario cadastrado\n')


def cadastrar_usuario():
   os.system('cls')
   print('Cadastro\n')
   nome = input('Digite seu Nome: \n')
   idade = int(input('Quantos anos você tem: \n'))
   senha = int(input('Escolha quatro Número'))
   dado_do_usuario= {'nome':nome,'idade':idade,'senha':senha,'ativo':True}
   usuario.append(dado_do_usuario)

   input('Digite Qualquer Tecla: ')
   
   main()

def loguin():
    os.system('cls')
    print('Loguin\n')
    nome = input('Nome: ')
    senha= int(input('Digite sua Senha: '))
    
    for loguin in usuario:
        if nome == loguin['nome'] and senha == loguin['senha']:
             print(f'Bem vindo {nome} ao Novo Sistema da J&c')
             

        else: 
            print(f'{nome} não existe !')
   
    input('Digite Qualquer Tecla: ')
    main()

def listar_usuario_cadastrado():
         os.system('cls')
         for cadastro in usuario:
           nome = cadastro['nome']
           idade = cadastro['idade']
           senha = cadastro['senha']
           print(f'- {nome} - {idade} - {senha}')

         input('Digite Qualquer Tecla: ')
         main()

def escolher_opcao():
    escolher_opcao = int(input('Qual Opção deseja Realizar: '))

    match escolher_opcao:
        case 1 :
            cadastrar_usuario()
        case 2 : 
            loguin()
        case 3 : 
            listar_usuario_cadastrado()
        case _: 
            print('Digite um Numero de 1 A 3:')
            main()

          

def main():
    os.system('cls')
    exibir_titulo()
    exibir_menu()
    escolher_opcao()


if __name__ == '__main__':
     main()