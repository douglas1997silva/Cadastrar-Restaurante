
import os

x = int(input('Digite o valor do x:'))
y = int(input('Digite o valor do y :'))


def primeiro_quadrante():
    print(f'O ponto está no Primeiro Quadrante.{x} e {y}')


def segundo_quadrante():
    print(f'O ponto está no Segundo Quadrante.{x}e {y}')


def terceiro_quadrante():
    print(f'O ponto está no Terceiro Quadrante. {x} e {y}')

def quarto_quatrante():
    print(f'O ponto está no Quarto Quadrante.{x} e {y}')

def localizado_no_eixo_origem():
   print(f'O ponto está localizado no eixo ou na origem.{x} e {y}')

def finalizar_programa():
   
   os.system('cls')

   print('Programa Finalizado ')
    

 
def escolher_eixo(x,y):
   try:

      if x > 0 and y > 0:
        primeiro_quadrante()
      elif x < 0 and y > 0:
       segundo_quadrante()
      elif x < 0 and y <0 :
        terceiro_quadrante()
      elif x > 0 and y < 0 :
        quarto_quatrante()     
      else:
        localizado_no_eixo_origem()
   except:
       finalizar_programa()



def main():
    os.system('cls')
    escolher_eixo(x,y)

if __name__ == "__main__":
    main()
numero = int(input('Escolha um numero:'))


if numero % 2 == 0:
    print('Seu numero é Par')
else:
    print('Seu numero e Impar ')