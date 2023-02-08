contador = 0
frase = 0

while frase !=('O relógio descarregou!') and frase !=('Por hoje já deu'):
    frase = input()
    contador += 1

if frase == ('O relógio descarregou!'):
    contador -= 1
    print(f'Corra Ben! Você já derrotou {contador} aliens')
    
elif frase == ('Por hoje já deu'):
    contador -= 1
    print(f'Muito Ben Ben! hehe você derrotou {contador} aliens hoje')