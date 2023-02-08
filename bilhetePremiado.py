numero_binario = int(input())
leitor_binario = len(str(numero_binario)) # Retorna o comprimento da string.
decimal = 0
i = 0
palpite = 0
tentativas_palpite = 0
contador_paltite = 0
chances = 3

for i in range(leitor_binario): # Neste bloco converto o número binário para decimal. (linhas 10 a 15)
    resto = numero_binario % 10 
    decimal = decimal + (resto * (2 ** i))
    leitor_binario -= 1
    i += 1
    numero_binario = numero_binario // 10

while contador_paltite != 3: # Estrutura de repetição finalizando ao final de 3 tentativas.
    palpite = input()

    if palpite == str(decimal): # Daqui pra baixo, tudo envolve estrutura de condição. (linhas 20 até 75)
        print('Parabéns!! Você acertou!')

        if palpite == '1':
            print('Férias inesquecíveis estão te esperando!')
            print('Seu destino será Porto de Galinhas (BRA).')
            print('Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!')
            break

        elif palpite == '2':
            print('Férias inesquecíveis estão te esperando!')
            print('Seu destino será Fernando de Noronha (BRA).')
            print('Belíssimas praias estão por vir.')
            print('Não esqueça o protetor solar.')
            break

        elif palpite == '3':
            print('Férias inesquecíveis estão te esperando!')
            print('Seu destino será Gramado (BRA).')
            print('Aproveite passeios e paisagens espetaculares no sul do país!')
            break

        elif palpite == '4':
            print('Férias inesquecíveis estão te esperando!')
            print('Seu destino será Berlim (ALE).')
            print('Desfrute de muita cultura e de experiências incríveis!')
            print('Prepare os casacos de frio!')
            break

        elif palpite == '5':
            print('Férias inesquecíveis estão te esperando!')
            print('Seu destino será Tóquio (JPN).')
            print('Viva uma experiência inesquecível explorando um país do outro lado do mundo.')
            print('Prepare-se para muitas horas de voo!')
            break
    
        elif palpite != '1' or '2' or '3' or '4' or '5':
            print('Mas, infelizmente, hoje não é o seu dia de sorte.')
            print('Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.')
            print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')
            break

    if palpite != str(decimal) and chances != 1:
        chances -= 1
        print(f'Resposta incorreta. Mas não desista! Você ainda tem { chances } chance(s).')

    elif palpite != str(decimal) and chances == 1 and decimal <= 5:
        print('Infelizmente mais uma resposta incorreta.')
        print('Agradecemos sua participação!')
        print('Seu bilhete era premiado. Que pena!')

    elif palpite != str(decimal) and chances == 1 and decimal > 5:
        print('Infelizmente mais uma resposta incorreta.')
        print('Agradecemos sua participação!')
        print('Pelo menos seu bilhete não era premiado.')
        print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')

    contador_paltite += 1 # Contador do while. Referente aos palpites!

    # Foi um aprendizado imenso e pretendo continuar evoluindo!
    # Obrigado minha monitora s2

