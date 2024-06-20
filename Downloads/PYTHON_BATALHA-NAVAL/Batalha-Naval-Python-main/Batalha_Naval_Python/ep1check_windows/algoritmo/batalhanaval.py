import re

JOGADOR1 = open('./jogador1.txt', 'r')      # abre e lê o arquivo jogador1.txt
JOGADOR2 = open('./jogador2.txt', 'r')      # abre e lê o arquivo jogador2.txt
RESULTADO = open('./resultado.txt', 'w')    # abre e escreve no arquivo resultado.txt

POSICAO1, POSICAO2 = {}, {}
LISTA1, LISTA2 = [], []
TD_POSICAO_INICIAL1, TD_POSICAO_INICIAL2 = [], []
LETRA_TORPEDO1, LETRA_TORPEDO2 = [], []
NUMERO_TORPEDO1, NUMERO_TORPEDO2 = [], []

ENCOURACADO_J1, PORTA_AVIOES_J1, SUBMARINOS_J1, CRUZADORES_J1 = [],[],[],[]
ENCOURACADO_J2, PORTA_AVIOES_J2, SUBMARINOS_J2, CRUZADORES_J2 = [],[],[],[]

LETRAS_TABULEIRO = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P']
NUMEROS_TABULEIRO = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']


for linha in JOGADOR1.readlines():              
    valores = (re.split(r'[;|\n|]+', linha))
    for numero in valores:                  
        LISTA1.append(numero.upper())       

# print("Lista Jogador 1")
# print(LISTA1)
# print()

for linha in JOGADOR2.readlines():          
    valores = (re.split(r'[;|\n|]+', linha))
    for numero in valores:                  
        LISTA2.append(numero.upper())       

# print("Lista Jogador 2")
# print(LISTA2)
# print()

POSICAO1[1] = LISTA1[LISTA1.index('1')+1:LISTA1.index('2')-1]
POSICAO1[2] = LISTA1[LISTA1.index('2')+1:LISTA1.index('3')-1]
POSICAO1[3] = LISTA1[LISTA1.index('3')+1:LISTA1.index('4')-1]
POSICAO1[4] = LISTA1[LISTA1.index('4')+1:LISTA1.index("#JOGADA")-1]
TORPEDOSJ1 = LISTA1[LISTA1.index('#JOGADA')+3:len(LISTA1)]

# print("Posicao das peças do Jogador 1:")
# print(POSICAO1)
# print()
# print("Torpedos do Jogador 1:")
# print(TORPEDOSJ1)
# print()

POSICAO2[1] = LISTA2[LISTA2.index('1')+1:LISTA2.index('2')-1]
POSICAO2[2] = LISTA2[LISTA2.index('2')+1:LISTA2.index('3')-1]
POSICAO2[3] = LISTA2[LISTA2.index('3')+1:LISTA2.index('4')-1]
POSICAO2[4] = LISTA2[LISTA2.index('4')+1:LISTA2.index("#JOGADA")-1]
TORPEDOSJ2 = LISTA2[LISTA2.index('#JOGADA')+3:len(LISTA2)]

# print("Posicao das peças do Jogador 2:")
# print(POSICAO2)
# print()
# print("Torpedos do Jogador 2:")
# print(TORPEDOSJ2)
# print()

for i in POSICAO1:                   
    for x in POSICAO1[i]:            
        TD_POSICAO_INICIAL1.append(x)     
a = TD_POSICAO_INICIAL1

for i in POSICAO2:                   
    for x in POSICAO2[i]:            
        TD_POSICAO_INICIAL2.append(x)     
b = TD_POSICAO_INICIAL2


# print("Todas as posições iniciais das peças do Jogador 1")
# print(a)
# print()
# print("Todas as posições iniciais das peças do Jogador 2")
# print(b)
# print()

# ============================================================================================================

# POSIÇÕES DAS PEÇAS DO JOGADOR 1

# POSIÇÕES DO ENCOURAÇADO
for i in a[:5]:                  
    primeiraLetra = i[:1:]       
    numero = i[1::]                

    if len(i) == 4:                  
        numero = numero[:-1:]      
    else:
        numero = numero[0]

    # Direção da peça de for Horizontal   
    if i[-1] == 'H':                                         
        for cont in range(0,4):                              
            proximo = primeiraLetra + (str(int(numero)))     
            ENCOURACADO_J1.append(proximo)                            
            numero = int(numero) + 1                         

    # Direção da peça se for Vertical
    elif i[-1] == 'V':                                                    
        CONT = 0                                                          
        while (LETRAS_TABULEIRO[CONT] != primeiraLetra) == True:            
            CONT += 1
        for cont in range(0,4):                                              
            proximo =  LETRAS_TABULEIRO[CONT + cont] + (str(int(numero)))    
            ENCOURACADO_J1.append(proximo) 

# POSIÇÕES DO PORTA-AVIÕES
for i in a[5:7]:                    
    primeiraLetra = i[:1:]           
    numero = i[1::]                  

    if len(i) == 4:                 
        numero = numero[:-1:]     
    else:
        numero = numero[0]

    # Direção da peça de for Horizontal  
    if i[-1] == 'H':
        for cont in range(0,5):
            proximo = primeiraLetra+(str(int(numero)))
            PORTA_AVIOES_J1.append(proximo)
            numero = int(numero) + 1
    
    # Direção da peça de for Vertical
    elif i[-1] == 'V':
        CONT = 0
        while (LETRAS_TABULEIRO[CONT] != primeiraLetra) == True:
            CONT += 1
        for cont in range(0,5):
            proximo =  LETRAS_TABULEIRO[CONT + cont] + (str(int(numero)))
            PORTA_AVIOES_J1.append(proximo)

# POSIÇÃO DOS SUBMARINOS
SUBMARINOS_J1 = POSICAO1[3]

# POSIÇÃO DOS CRUZADORES
for i in a[17::]:
    primeiraLetra = i[:1:]
    numero = i[1::]

    if len(i) == 4:                  
        numero = numero[:-1:]      
    else:
        numero = numero[0]

    # Direção da peça de for Horizontal 
    if i[-1] == 'H':
        for cont in range(0,2):
            proximo = primeiraLetra+(str(int(numero)))
            CRUZADORES_J1.append(proximo)
            numero = int(numero) + 1

    # Direção da peça de for Vertical
    elif i[-1] == 'V':
        CONT = 0
        while (LETRAS_TABULEIRO[CONT] != primeiraLetra) == True:
            CONT += 1
        for cont in range(0,2):
            proximo =  LETRAS_TABULEIRO[CONT + cont] + (str(int(numero)))
            CRUZADORES_J1.append(proximo)

# print("JOGADAS DO JOGADOR 1")
# print("Encouraçados")
# print(ENCOURACADO_J1)
# print()
# print("Porta-Aviões")
# print(PORTA_AVIOES_J1)
# print()
# print("Submarinos")
# print(SUBMARINOS_J1)
# print()
# print("Cruzadores")
# print(CRUZADORES_J1)
# print()

LETRA_PECA1 = []
NUMERO_PECA1 = []

for i in a[:5]:                    
    primeiraLetra = i[:1:]         
    numero = i[1::]               

    if len(i) == 4:                  
        numero = numero[:-1:]      
    else:
        numero = numero[0]
    LETRA_PECA1.append(primeiraLetra)
    NUMERO_PECA1.append(numero)

for i in a[5:7]:                    
    primeiraLetra = i[:1:]          
    numero = i[1::]                 

    if len(i) == 4:                  
        numero = numero[:-1:]      
    else:
        numero = numero[0]
        LETRA_PECA1.append(primeiraLetra)
        NUMERO_PECA1.append(numero)

for i in SUBMARINOS_J1:
    primeiraLetra = i[:1:]
    numero = i[1::]
    LETRA_PECA1.append(primeiraLetra)
    NUMERO_PECA1.append(numero)

for i in a[17::]:
    primeiraLetra = i[:1:]
    numero = i[1::]

    if len(i) == 4:                  
        numero = numero[:-1:]      
    else:
        numero = numero[0]
    LETRA_PECA1.append(primeiraLetra)
    NUMERO_PECA1.append(numero)

# ============================================================================================================

# POSIÇÕES DAS PEÇAS DO JOGADOR 2

# POSIÇÕES DO ENCOURAÇADO
for i in b[:5]:                    
    primeiraLetra = i[:1:]        
    numero = i[1::]               

    if len(i) == 4:                  
        numero = numero[:-1:]      
    else:
        numero = numero[0]

    # Direção da peça de for Horizontal   
    if i[-1] == 'H':                                        
        for cont in range(0,4):                              
            proximo = primeiraLetra + (str(int(numero)))    
            ENCOURACADO_J2.append(proximo)                            
            numero = int(numero) + 1                         

    # Direção da peça se for Vertical
    elif i[-1] == 'V':                                                     
        CONT = 0                                                           
        while (LETRAS_TABULEIRO[CONT] != primeiraLetra) == True:             
            CONT += 1
        for cont in range(0,4):                                              
            proximo =  LETRAS_TABULEIRO[CONT + cont] + (str(int(numero)))    
            ENCOURACADO_J2.append(proximo) 

# POSIÇÕES DO PORTA-AVIÕES
for i in b[5:7]:                     
    primeiraLetra = i[:1:]           
    numero = i[1::]                  

    if len(i) == 4:                  
        numero = numero[:-1:]      
    else:
        numero = numero[0]

    # Direção da peça de for Horizontal  
    if i[-1] == 'H':
        for cont in range(0,5):
            proximo = primeiraLetra+(str(int(numero)))
            PORTA_AVIOES_J2.append(proximo)
            numero = int(numero) + 1
    
    # Direção da peça de for Vertical
    elif i[-1] == 'V':
        CONT = 0
        while (LETRAS_TABULEIRO[CONT] != primeiraLetra) == True:
            CONT += 1
        for cont in range(0,5):
            proximo =  LETRAS_TABULEIRO[CONT + cont] + (str(int(numero)))
            PORTA_AVIOES_J2.append(proximo)

# POSIÇÃO DOS SUBMARINOS
SUBMARINOS_J2 = POSICAO2[3]

# POSIÇÃO DOS CRUZADORES
for i in b[17::]:
    primeiraLetra = i[:1:]
    numero = i[1::]

    if len(i) == 4:                  
        numero = numero[:-1:]    
    else:
        numero = numero[0]

    # Direção da peça de for Horizontal 
    if i[-1] == 'H':
        for cont in range(0,2):
            proximo = primeiraLetra+(str(int(numero)))
            CRUZADORES_J2.append(proximo)
            numero = int(numero) + 1

    # Direção da peça se for Vertical
    elif i[-1] == 'V':
        CONT = 0
        while (LETRAS_TABULEIRO[CONT] != primeiraLetra) == True:
            CONT += 1
        for cont in range(0,2):
            proximo =  LETRAS_TABULEIRO[CONT + cont] + (str(int(numero)))
            CRUZADORES_J2.append(proximo)

# print("JOGADAS DO JOGADOR 2")
# print("Encouraçados")
# print(ENCOURACADO_J2)
# print()
# print("Porta-Aviões")
# print(PORTA_AVIOES_J2)
# print()
# print("Submarinos")
# print(SUBMARINOS_J2)
# print()
# print("Cruzadores")
# print(CRUZADORES_J2)
# print()


LETRA_PECA2 = []
NUMERO_PECA2 = []

for i in b[:5]:                    
    primeiraLetra = i[:1:]         
    numero = i[1::]               

    if len(i) == 4:                  
        numero = numero[:-1:]      
    else:
        numero = numero[0]
    LETRA_PECA2.append(primeiraLetra)
    NUMERO_PECA2.append(numero)

for i in b[5:7]:                    
    primeiraLetra = i[:1:]          
    numero = i[1::]                 

    if len(i) == 4:                  
        numero = numero[:-1:]      
    else:
        numero = numero[0]
        LETRA_PECA2.append(primeiraLetra)
        NUMERO_PECA2.append(numero)

for i in SUBMARINOS_J2:
    primeiraLetra = i[:1:]
    numero = i[1::]
    LETRA_PECA2.append(primeiraLetra)
    NUMERO_PECA2.append(numero)

for i in b[17::]:
    primeiraLetra = i[:1:]
    numero = i[1::]

    if len(i) == 4:                  
        numero = numero[:-1:]      
    else:
        numero = numero[0]
    LETRA_PECA2.append(primeiraLetra)
    NUMERO_PECA2.append(numero)

TODAS_POSICOES_JG1 = ENCOURACADO_J1 + PORTA_AVIOES_J1 + SUBMARINOS_J1 + CRUZADORES_J1
TODAS_POSICOES_JG2 = ENCOURACADO_J2 + PORTA_AVIOES_J2 + SUBMARINOS_J2 + CRUZADORES_J2

# print("Todas as posições das peças do jogador 1")
# print(TODAS_POSICOES_JG1)
# print()
# print("Todas as posições das peças do jogador 2")
# print(TODAS_POSICOES_JG2)
# print()

# ============================================================================================================

# print("Letras da peça Jogador 1")
# print(LETRA_PECA1)
# print()
# print("Números da peça Jogador 1")
# print(NUMERO_PECA1)
# print()

for i in (TORPEDOSJ1):            
    LETRA_TORPEDO1.append(i[:1])        
    NUMERO_TORPEDO1.append(i[1:])      

# print("Letras do torpedo Jogador 1")
# print(LETRA_TORPEDO1)
# print()
# print("Numeros do torpedo Jogador 1")
# print(NUMERO_TORPEDO1)
# print()

# print("Letras da peça Jogador 2")
# print(LETRA_PECA2)
# print()
# print("Números da peça Jogador 2")
# print(NUMERO_PECA2)
# print()

for i in (TORPEDOSJ2):            
    LETRA_TORPEDO2.append(i[:1])        
    NUMERO_TORPEDO2.append(i[1:])       

# print("Letra dos torpedos Jogador 2")
# print(LETRA_TORPEDO2)
# print()
# print("Numero dos torpedos Jogador 2")
# print(NUMERO_TORPEDO2)
# print()

# ============================================================================================================

def main():
    # VERIFICANDO ERRO DE VALIDAÇÃO DA QUANTIDADE DE PEÇAS:
    # ERROR_NR_PARTS_VALIDATION

    if len(POSICAO1[1]) != 5 or len(POSICAO1[2]) != 2 or len(POSICAO1[3]) != 10 or len(POSICAO1[4]) != 5 or len(TORPEDOSJ1) != 25:
        RESULTADO.write("J1 ERROR_NR_PARTS_VALIDATION")
        return
    elif len(POSICAO2[1]) != 5 or len(POSICAO2[2]) != 2 or len(POSICAO2[3]) != 10 or len(POSICAO2[4]) != 5 or len(TORPEDOSJ2) != 25:
        RESULTADO.write("J2 ERROR_NR_PARTS_VALIDATION")
        return
    
    # VERIFICANDO ERRO DE VALIDAÇÃO DAS PEÇAS REPETIDAS (DENTRO DO TABULEIRO)
    # ERROR_OVERWRITE_PIECES_VALIDATION

    for contagem1 in range(0,len(TODAS_POSICOES_JG1)):
        if TODAS_POSICOES_JG1.count(TODAS_POSICOES_JG1[contagem1]) > 1:
            RESULTADO.write('J1 ERROR_OVERWRITE_PIECES_VALIDATION')
            return
        
    for contagem2 in range(0,len(TODAS_POSICOES_JG2)):
        if TODAS_POSICOES_JG2.count(TODAS_POSICOES_JG2[contagem2]) > 1:
            RESULTADO.write('J2 ERROR_OVERWRITE_PIECES_VALIDATION')
            return

    # VERIFICANDO ERRO DE VALIDAÇÃO DA POSIÇÃO DAS PEÇAS (FORA DO TABULEIRO)
    #  ERROR_POSITION_NONEXISTENT_VALIDATION

    # JOGADOR 1
    for letra1 in range(0,len(LETRA_TORPEDO1)):
        erro = (LETRA_TORPEDO1[letra1]) in LETRAS_TABULEIRO
        if  erro == False:
            RESULTADO.write('J1 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
        
    for numero1 in range(0,len(NUMERO_TORPEDO1)):
        erro = (NUMERO_TORPEDO1[numero1]) in NUMEROS_TABULEIRO
        if erro == False:
            RESULTADO.write('J1 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
        
    for letraPeca1 in range(0,len(LETRA_PECA1)):
        erro = (LETRA_PECA1[letraPeca1]) in LETRAS_TABULEIRO
        if erro == False:
            RESULTADO.write('J1 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return

    for numeroPeca1 in range(0,len(NUMERO_PECA1)):
        erro = (NUMERO_PECA1[numeroPeca1]) in NUMEROS_TABULEIRO
        if erro == False:
            RESULTADO.write('J1 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
        
    # JOGADOR 2
    for letra2 in range(0,len(LETRA_TORPEDO2)):
        erro = (LETRA_TORPEDO2[letra2]) in LETRAS_TABULEIRO
        if  erro == False:
            RESULTADO.write('J2 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
        
    for numero2 in range(0,len(NUMERO_TORPEDO2)):
        erro = (NUMERO_TORPEDO2[numero2]) in NUMEROS_TABULEIRO
        if erro == False:
            RESULTADO.write('J2 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
        
    for letraPeca2 in range(0,len(LETRA_PECA2)):
        erro = (LETRA_PECA2[letraPeca2]) in LETRAS_TABULEIRO
        if erro == False:
            RESULTADO.write('J2 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return

    for numeroPeca2 in range(0,len(NUMERO_PECA2)):
        erro = (NUMERO_PECA2[numeroPeca2]) in NUMEROS_TABULEIRO
        if erro == False:
            RESULTADO.write('J2 ERROR_POSITION_NONEXISTENT_VALIDATION')
            return
        
# ============================================================================================================

    ACERTOS_EJ1, ACERTOS_PAJ1, ACERTOS_SJ1, ACERTOS_CJ1 = [], [], [], []
    ACERTOS_EJ2, ACERTOS_PAJ2, ACERTOS_SJ2, ACERTOS_CJ2 = [], [], [], []
    ENCOURACADO_ACERTADO1, PORTA_AVIOES_ACERTADO1, SUBMARINO_ACERTADO1, CRUZADOR_ACERTADO1 = 0, 0, 0, 0
    ENCOURACADO_ACERTADO2, PORTA_AVIOES_ACERTADO2, SUBMARINO_ACERTADO2, CRUZADOR_ACERTADO2 = 0, 0, 0, 0

    total_acertos_ej1 = 0
    for indice in range(0, len(ENCOURACADO_J1)):
        acerto = ENCOURACADO_J1[indice] in TORPEDOSJ2
        if acerto == True:
            ACERTOS_EJ1.append(ENCOURACADO_J1[indice])
            if len(ACERTOS_EJ1) == 4:
                ENCOURACADO_ACERTADO1 += 5
                total_acertos_ej1 = total_acertos_ej1 + 1
            else:
                ENCOURACADO_ACERTADO1 += 3
                
    # print("ACERTO ENCOURAÇADO JOGADOR 1")
    # print("Pontos: ", ENCOURACADO_ACERTADO1)
    # print("Posições acertadas: ", ACERTOS_EJ1)
    # print("Total acertado: ", total_acertos_ej1)
    # print()

    total_acertos_paj1 = 0
    for indice in range(0, len(PORTA_AVIOES_J1)):
        acerto = PORTA_AVIOES_J1[indice] in TORPEDOSJ2
        if acerto == True:
            ACERTOS_PAJ1.append(PORTA_AVIOES_J1[indice])
            if len(ACERTOS_PAJ1) == 5:
                PORTA_AVIOES_ACERTADO1 += 5
                total_acertos_paj1 = total_acertos_paj1 + 1
            else:
                PORTA_AVIOES_ACERTADO1 += 3

    # print("ACERTO PORTA-AVIÕES JOGADOR 1")
    # print("Pontos: ", PORTA_AVIOES_ACERTADO1)
    # print("Posições acertadas: ", ACERTOS_PAJ1)
    # print("Total acertado: ", total_acertos_paj1)
    # print()

    total_acertos_sj1 = 0
    for indice in range(0, len(SUBMARINOS_J1)):
        acerto = SUBMARINOS_J1[indice] in TORPEDOSJ2
        if acerto == True:
            ACERTOS_SJ1.append(SUBMARINOS_J1[indice])
            SUBMARINO_ACERTADO1 += 5
            total_acertos_sj1 = total_acertos_sj1 + 1

    # print("ACERTO SUBMARINOS JOGADOR 1")
    # print("Pontos: ", SUBMARINO_ACERTADO1)
    # print("Posições acertadas: ", ACERTOS_SJ1)
    # print("Total acertado: ", total_acertos_sj1)
    # print()

    total_acertos_cj1 = 0
    for indice in range(0, len(CRUZADORES_J1)):
        acerto = CRUZADORES_J1[indice] in TORPEDOSJ2
        if acerto == True:
            ACERTOS_CJ1.append(CRUZADORES_J1[indice])
            if len(ACERTOS_CJ1) == 2:
                CRUZADOR_ACERTADO1 += 5
                total_acertos_cj1 = total_acertos_cj1 + 1
            else:
                CRUZADOR_ACERTADO1 += 3

    # print("ACERTO CRUZADORES JOGADOR 1")
    # print("Pontos: ", CRUZADOR_ACERTADO1)
    # print("Posições acertadas: ", ACERTOS_CJ1)
    # print("Total acertado: ", total_acertos_cj1)
    # print()

    total_acertos_ej2 = 0
    for indice in range(0, len(ENCOURACADO_J2)):
        acerto = ENCOURACADO_J2[indice] in TORPEDOSJ1
        if acerto == True:
            ACERTOS_EJ2.append(ENCOURACADO_J2[indice])
            if len(ACERTOS_EJ2) == 4:
                ENCOURACADO_ACERTADO2 += 5
                total_acertos_ej2 = total_acertos_ej2 + 1
            else:
                ENCOURACADO_ACERTADO2 += 3
                
    # print("ACERTO ENCOURAÇADO JOGADOR 2")
    # print("Pontos: ", ENCOURACADO_ACERTADO2)
    # print("Posições acertadas: ", ACERTOS_EJ2)
    # print("Total acertado: ", total_acertos_ej2)
    # print()

    total_acertos_paj2 = 0
    for indice in range(0, len(PORTA_AVIOES_J2)):
        acerto = PORTA_AVIOES_J2[indice] in TORPEDOSJ1
        if acerto == True:
            ACERTOS_PAJ2.append(PORTA_AVIOES_J2[indice])
            if len(ACERTOS_PAJ2) == 5:
                PORTA_AVIOES_ACERTADO2 += 5
                total_acertos_paj2 = total_acertos_paj2 + 1
            else:
                PORTA_AVIOES_ACERTADO2 += 3

    # print("ACERTO PORTA-AVIÕES JOGADOR 2")
    # print("Pontos: ", PORTA_AVIOES_ACERTADO2)
    # print("Posições acertadas: ", ACERTOS_PAJ2)
    # print("Total acertado: ", total_acertos_paj2)
    # print()

    total_acertos_sj2 = 0
    for indice in range(0, len(SUBMARINOS_J2)):
        acerto = SUBMARINOS_J2[indice] in TORPEDOSJ1
        if acerto == True:
            ACERTOS_SJ2.append(SUBMARINOS_J2[indice])
            SUBMARINO_ACERTADO2 += 5
            total_acertos_sj2 = total_acertos_sj2 + 1

    # print("ACERTO SUBMARINOS JOGADOR 2")
    # print("Pontos: ", SUBMARINO_ACERTADO2)
    # print("Posições acertadas: ", ACERTOS_SJ2)
    # print("Total acertado: ", total_acertos_sj2)
    # print()

    total_acertos_cj2 = 0
    for indice in range(0, len(CRUZADORES_J2)):
        acerto = CRUZADORES_J2[indice] in TORPEDOSJ1
        if acerto == True:
            ACERTOS_CJ2.append(CRUZADORES_J2[indice])
            if len(ACERTOS_CJ2) == 2:
                CRUZADOR_ACERTADO2 += 5
                total_acertos_cj2 = total_acertos_cj2 + 1
            else:
                CRUZADOR_ACERTADO2 += 3

    # print("ACERTO CRUZADORES JOGADOR 2")
    # print("Pontos: ", CRUZADOR_ACERTADO2)
    # print("Posições acertadas: ", ACERTOS_CJ2)
    # print("Total acertado: ", total_acertos_cj2)
    # print()

    # SOMA DOS PONTOS
    PONTOS_JOGADOR_1 = ENCOURACADO_ACERTADO2 + PORTA_AVIOES_ACERTADO2 + SUBMARINO_ACERTADO2 + CRUZADOR_ACERTADO2
    PONTOS_JOGADOR_2 = ENCOURACADO_ACERTADO1 + PORTA_AVIOES_ACERTADO1 + SUBMARINO_ACERTADO1 + CRUZADOR_ACERTADO1
    TOTAL_ACERTADO_JOGADOR_1 = total_acertos_ej2 + total_acertos_paj2 + total_acertos_sj2 + total_acertos_cj2
    TOTAL_ACERTADO_JOGADOR_2 = total_acertos_ej1 + total_acertos_paj1 + total_acertos_sj1 + total_acertos_cj1
    NAO_ACERTADO_JOGADOR_1 = len(b) - TOTAL_ACERTADO_JOGADOR_1
    NAO_ACERTADO_JOGADOR_2 = len(a) - TOTAL_ACERTADO_JOGADOR_2

    # print("SOMA DOS PONTOS")
    # print("Pontos Jogador 1: ", PONTOS_JOGADOR_1)
    # print("Pontos Jogador 2: ", PONTOS_JOGADOR_2)
    # print("Total acertos Jogador 1: ", TOTAL_ACERTADO_JOGADOR_1)
    # print("Total acertos Jogador 2: ", TOTAL_ACERTADO_JOGADOR_2)
    # print("Não acertado Jogador 1: ", NAO_ACERTADO_JOGADOR_1)
    # print("Não acertado Jogador 2: ", NAO_ACERTADO_JOGADOR_2)
    # print()

    # JOGO EMPATADO
    if PONTOS_JOGADOR_1 == PONTOS_JOGADOR_2:
        RESULTADO.write("J1 {}AA {}AE {}PT \nJ2 {}AA {}AE {}PT".format(str(TOTAL_ACERTADO_JOGADOR_1),str(NAO_ACERTADO_JOGADOR_1),str(PONTOS_JOGADOR_1),str(TOTAL_ACERTADO_JOGADOR_2),str(NAO_ACERTADO_JOGADOR_2),str(PONTOS_JOGADOR_2)))
        return 
    
    # JOGADOR 1 - GANHOU
    if PONTOS_JOGADOR_1 > PONTOS_JOGADOR_2:
        RESULTADO.write('J1 {}AA {}AE {}PT'.format(str(TOTAL_ACERTADO_JOGADOR_1),str(NAO_ACERTADO_JOGADOR_1),str(PONTOS_JOGADOR_1)))
        return
    
    # JOGADOR 2 - GANHOU    
    if PONTOS_JOGADOR_2 > PONTOS_JOGADOR_1:
        RESULTADO.write('J2 {}AA {}AE {}PT'.format(str(TOTAL_ACERTADO_JOGADOR_2),str(NAO_ACERTADO_JOGADOR_2),str(PONTOS_JOGADOR_2)))
        return

#Inicia a Função
main()
JOGADOR1.close()
JOGADOR2.close()
RESULTADO.close()
exit()