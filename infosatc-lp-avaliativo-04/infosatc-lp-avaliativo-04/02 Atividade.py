

def verificar (nome,nome_invertido):
    if nome_invertido == nome [::-1]:
        return True
    else:
        return False
nome = input("Digite o nome normal para ser verificado:") 
nome_invertido = input ("Digite o nome invertido para ser comparado:")

comparação= verificar (nome_invertido,nome)
print ("comparação:",comparação)
    
