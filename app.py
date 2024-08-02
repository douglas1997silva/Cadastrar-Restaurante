
import os
restaurantes = [{'nome':'Barufrs','categoria':'Hamburgue','ativo':False},
                {'nome':'PizzaBurgue','categoria':'Restaurante','ativo':True},
                {'nome':'KFC','categoria':'Fest Food','ativo':True}]


def exibir_nome():
      print("""
      ╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
      ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
      ┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
      ╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
      ┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
      ╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
      ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
      ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
            
            """
            )
def exibir_opcao():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurantes')
      print('3. Alternar estado do restaurantes')
      print('4. Sair')
def exibir_limpar_programa(nome):
     '''Essa Função faz um Desing com * 1
     '''
     os.system("cls")
     linha = '*' * (len(nome))
     print(linha)
     print(f'{nome}')
     print(linha)
     print()
     

def finalizar_app():
    exibir_limpar_programa('Finalizar App')
    #os.system("clear") no mac
    
def voltar_ao_menu_principal():
     input('Precione Qualquer Tecla para voltar!')
     main()


def opcao_invalida():
     print('Opção Inválida!\n')
     voltar_ao_menu_principal()

def cadastrar_restaurante():

     '''Função Cadastrar Restaurante '''

     exibir_limpar_programa('Cadastar Restaurante')
    
     nome_restaurante =  input('Qual eo nome do seu Restaurante para cadastro ? ')
     categoria = input(' Qual e a categoria? ')
     dados_cadastrados = {'nome': nome_restaurante,'categoria':categoria,'ativo':False }
     restaurantes.append(dados_cadastrados)
     print(f'{nome_restaurante}  foi Cadastardo com Sucesso!\n')
     voltar_ao_menu_principal()

def lista_restaurante():

     '''Essa Função exibe os restaurante que foram cadastrado e se forram ativo ou não '''

     exibir_limpar_programa('Lista de Restaurantes')
     
     print(f'- {'Restaurante'.ljust(20)} - {'Categoria'.ljust(20)} - Status')
     for restaurante in restaurantes:
          restaurante_nome = restaurante['nome']
          categoria = restaurante['categoria']
          ativo = 'ativado' if  restaurante['ativo'] else 'Desativado'
          print(f'- {restaurante_nome.ljust(20)} - {categoria.ljust(20)} - {ativo.ljust(20)}')

     voltar_ao_menu_principal()

def escolher_estado_restaurante():

     '''Essa função Troca o ESTADO "Ativo " para "Desativado " ou Vice versa'''
     
     exibir_limpar_programa('Escolha o Estado do seu Restaurante: ')
     nome_restaurante = input('Digite o nome do Restaurante para Ativar ou Desativar: ')
     restaurante_encontrado = False

     for restaurante in restaurantes:
          if nome_restaurante == restaurante['nome']:
               restaurante_encontrado = True
               restaurante['ativo'] = not restaurante['ativo']
               menssagem = f'O restaurante {nome_restaurante} foi Ativado com Sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
               print(menssagem)

     if not restaurante_encontrado:
          print('Restaurante não encontrado')
     

     voltar_ao_menu_principal()

               


def escolher_opcao():
      '''Essa função escolhe a opção'''
      try:
          opacao_escolhida = int(input('Escolha uma Opção: '))

          # print(type(opacao_escolhida))
          match opacao_escolhida:
               case 1:
                    cadastrar_restaurante()
               case 2:
                    lista_restaurante()
               case 3:
                    escolher_estado_restaurante()
               case 4:
                    finalizar_app()
               
      except:
           opcao_invalida()

def main():
   os.system('cls')
   exibir_nome() 
   exibir_opcao()
   escolher_opcao()


if __name__ == '__main__':
    main()