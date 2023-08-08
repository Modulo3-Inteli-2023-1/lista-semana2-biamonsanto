#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui







# Teste a sua função aqui (caso ache necessário)




def conta_palavras_unicas(frase):
    contagem = 0
    palavras = frase.split()
    for palavra in palavras:
        if palavras.count(palavra) == 1:
            contagem += 1
    return contagem

