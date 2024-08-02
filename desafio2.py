numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Douglas','Gabriella','Luiz','Davi','Clarice']
anos = ['1997','2024']

for numero in numeros:
    print(f'- {numero}')
soma = 0
c = 0
try:
    for numero in numeros:
        if numero % 2 == 1:
            soma += numero
            print(f'{soma}')
        
except: 
    if numero % 2 ==0:
       print(f'{numero}')


for numero in reversed(numeros):
    print(f'- {numero}')


 
 
 
 
print('Ola\n')

print('Vamos Aprender a Tabuada ?')


numero_tabuada = int(input('Escolha uma numero de 1 a 9 : '))


for multiplicado in numeros:
     tabuadas = numero_tabuada * multiplicado
     print(f'{numero_tabuada} x {multiplicado} = {tabuadas}')


try:
    for conta in numeros:
        c += conta
        print(f'{c}')

except: 
    print('Finalizar ')