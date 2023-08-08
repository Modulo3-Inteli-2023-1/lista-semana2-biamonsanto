#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui







# Teste a sua função aqui (caso ache necessário)





def conta_palavras_unicas(frase):
    contagem = 1 
    frase = frase.split()
    for i in range(len(frase) - 1):
        for y in range(i + 1,len(frase)):
            if frase[i] == frase[y]:
                teste = True
                if teste == True:
                    contagem =+ 1 
        contagem += 1

    return(contagem)   



