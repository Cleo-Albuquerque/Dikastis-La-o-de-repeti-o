acoes = 0
estiou = 1
chuvoso = 0
tempo = ''

separar_dinheiro=0
pouco_dinheiro = 0
muito_dinheiro = 0

passar_protetor = 0

while acoes != ('ir para a praia'): # Finaliza o loop ao digitar, "ir para a praia".
    acoes = input()

    if acoes == ('separar dinheiro'): # Vai adicionando a carteira.
        separar_dinheiro += float(input())
        
    if acoes == 'choveu':
        chuvoso = acoes
        tempo = 0

    if acoes =='parou de chover':
        estiou = acoes
        tempo = 1

    if acoes =='passar protetor':
        passar_protetor = acoes

if separar_dinheiro < 10:
    pouco_dinheiro = separar_dinheiro

if separar_dinheiro >= 10:
    muito_dinheiro = separar_dinheiro

if tempo == 0: # Caso, chova!
    print('Hoje não vai dar pra ir, chuvinha barrou')

if tempo == 1: # Caso pare de chover, em qualquer momento do dia!
    print('Hoje tem sol e mar!')
    if (not passar_protetor and pouco_dinheiro):
        print('Você não chegou muito bem, chame um médico!')
    if (not passar_protetor and muito_dinheiro):
        print('O novo camarão do CIn foi criado')
    if (passar_protetor and pouco_dinheiro):
        print('Só faltou uma aguinha de coco...')
    if (passar_protetor and muito_dinheiro):
        print('Aí sim! Hoje rendeu!')

elif not(chuvoso): # Se não chover!
    print('Hoje tem sol e mar!')
    if (not passar_protetor and pouco_dinheiro):
        print('Você não chegou muito bem, chame um médico!')
    if (not passar_protetor and muito_dinheiro):
        print('O novo camarão do CIn foi criado')
    if (passar_protetor and pouco_dinheiro):
        print('Só faltou uma aguinha de coco...')
    if (passar_protetor and muito_dinheiro):
        print('Aí sim! Hoje rendeu!')