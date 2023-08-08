#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui







# Teste a sua função aqui (caso ache necessário)




def conta_palavras_unicas(frase):
    contagem = 0 
    frase = frase.split()
    for i in range(len(frase)):
        palavra_unicas = True
        for y in range(len(frase)):
            if i != y and frase[i] == frase[y]:
                palavra_unicas = False
                break
        if palavra_unicas:
            contagem += 1
    return contagem


