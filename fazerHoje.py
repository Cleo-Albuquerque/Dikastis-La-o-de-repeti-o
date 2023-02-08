tentativas_falhas = 0
despesa_total = 0
etapas_realizadas = 0

custo_etapa = 0
status_etapa = ''
nome_etapa = 0

nome_invencao = input()

while nome_etapa != 'desistir' or nome_etapa != 'concluir':
    nome_etapa = input()
    
    if nome_etapa == 'dar um plus':
        custo_etapa = int(input())
        print(f'Agora o(a) {nome_invencao} ficou ainda mais legal! Pena que precisei gastar R${custo_etapa}')
        nome_etapa = input()
        despesa_total += custo_etapa # Armazena os valores de custo, para imprimir no final.

    if nome_etapa == 'desistir':
        print(f'A jornada da construção do(a) {nome_invencao} acaba aqui.')
        print(f'Infelizmente, o sonho do(a) {nome_invencao} foi interrompido e levou junto com ele R${despesa_total}')
        break

    if nome_etapa == 'concluir':
        print(f'A jornada da construção do(a) {nome_invencao} acaba aqui.')
        print(f'Uhuuu, finalmente o(a) {nome_invencao} tá pronto(a)! Esse projeto me custou R${despesa_total}')
        break

    custo_etapa = int(input())
    tentativas = int(input())
    contador_tentativas = 0
    
    while contador_tentativas < tentativas:
        status_etapa = input()

        if status_etapa == 'correto':
            etapas_realizadas += 1 # conta e armazena os valores para imprimir no print da linha 49.
            tentativas = 0
            print(f'Oba! consegui {nome_etapa}, o que me custou R${custo_etapa}')
                                 
        if status_etapa == 'incorreto':
            tentativas_falhas += 1 # conta e armazena os valores para imprimir no print da linha 49.     
            print(f'Ainda não consegui {nome_etapa} corretamente, e essa tentativa me custou R${custo_etapa}')
        
        despesa_total += custo_etapa # Armazena os valores de custo, para imprimir caso digite 'desistir' ou 'concluir'.
        contador_tentativas = contador_tentativas + 1 #Contador para comparar com tentativas no while mais interno.
    
    print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {tentativas_falhas}')    