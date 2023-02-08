quantidade = int(input())
contador_lugares = 0
somatorio_notas_atual = 0

destino = None
melhor_lugar = 0
pior_lugar = 0
empate_lugar = 0
auxiliar_empate = ''

melhor_notas = 0
pior_notas = None
empate_notas = 0
destino = 0

while contador_lugares < quantidade: # Neste loop: enquanto contador não for igual a quantidade ele continua chamando.

    destino = input() # Recebe o nome do lugar!
    
    somatorio_notas_atual = 0
    nota_input = 0

    while nota_input >= 0: # Se o usuário digitar valor abaixo de 0 sai do loop.
        somatorio_notas_atual = nota_input + somatorio_notas_atual
        nota_input = int(input())
      
    if contador_lugares == 0: # Se for o primeiro lugar!
        pior_notas = somatorio_notas_atual
        pior_lugar = destino

    if somatorio_notas_atual == melhor_notas:
        empate_notas = somatorio_notas_atual
        empate_lugar = auxiliar_empate + ", " + destino
        auxiliar_empate = empate_lugar
        
    if somatorio_notas_atual > melhor_notas:
        melhor_notas = somatorio_notas_atual
        melhor_lugar = destino
        auxiliar_empate = ('')

    if somatorio_notas_atual < pior_notas :
        pior_notas = somatorio_notas_atual
        pior_lugar = destino
    
    contador_lugares = contador_lugares + 1

if not empate_notas or melhor_notas > empate_notas:
    print(f'{melhor_lugar} ganhou de lavada de {pior_lugar}, com {melhor_notas} vs {pior_notas}')
else:
    print(f'{melhor_lugar}{auxiliar_empate}')
    print('Tantas opções')