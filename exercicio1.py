#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui







# Teste a sua função aqui (caso ache necessário)




def conta_palavras_unicas(frase):
    contagem = 0
    palavras = frase.split()
    contagem_palavras = {} 

    for palavra in palavras:
        if palavra in contagem_palavras:
            contagem_palavras[palavra] += 1
        else:
            contagem_palavras[palavra] = 1

    for palavra, ocorrencias in contagem_palavras.items():
        if ocorrencias == 1:
            contagem += 1

    return contagem