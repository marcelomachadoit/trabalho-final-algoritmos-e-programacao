#Função para adicionar o produto selecionado e sua quantidade no carrinho
def adicionarAoCarrinho(codigo,quantidade):
    if codigo == 1:
        valor = 25
    elif codigo == 2:
        valor = 22.50
    elif codigo == 3:
        valor = 35
    elif codigo == 4:
        valor = 10
    else:
        valor = 5
    return (float(valor*quantidade))

#Função que verifica e informa descontos
def verificarDesconto(valor):
    if valor < 50:
        possuiDesconto = False
        desconto = 1
        valorDoDesconto = 0
    elif valor >= 50 and valor < 100:
        possuiDesconto = True
        desconto = 0.95
        valorDoDesconto = 5
    else:
        possuiDesconto = True
        desconto = 0.90
        valorDoDesconto = 10
    return possuiDesconto, desconto, valorDoDesconto

#Inicio do código
print("""
ITEM                    CÓDIGO   PREÇO
Hamburguer Tradicional     1    R$25.00
Hamburguer Frango          2    R$22.50
Hamburguer Picanha         3    R$35.00
Batata-frita               4    R$10.00
Refrigerante               5    R$5.00
""")

#Validação de nomes (se há números ou caracteres especiais).
nomeValido = False
while nomeValido == False:
    nomeCliente = str(input("Insira o nome do cliente: ")).upper()
    #Funcionais próprias do Python foram usadas para a verificação de nome any() e isalnum()
    if any(caractere.isdigit() for caractere in nomeCliente) == False and nomeCliente.isalnum() == True:
        nomeValido = True
    else:
        print("Nome inválido! Insira uma nome válido")


pedindo = True
total = 0
#Loop para a compra completa
while pedindo:
    #Variavel e loop para garantir que seja inserido um valor aceito
    pedidoValido = False
    while pedidoValido == False:
        codigo = input("Insira o código do seu pedido: ")
        if codigo == "1" or codigo == "2" or codigo == "3" or codigo == "4" or codigo == "5":
            codigo = int(codigo)
            quantidadeReal = False
            #Variavel e loop para garantir que seja inserido um valor aceito
            while quantidadeReal == False:
                quantidade = input("Insira a quantidade desejada: ")
                #Não quebra o código se o usuario inserir um valor diferente de um numero
                if quantidade.isdigit() == True:
                    quantidade = int(quantidade)
                    quantidadeReal = True
                    compra = adicionarAoCarrinho(codigo,quantidade)
                    pedidoValido = True
                else:
                    print("Valor inválido! Insira um valor válido")

        else:
            #Caso de valor inválido
            print("Valor inválido! Insira um valor válido")
            pedidoValido = False
    total = total + compra

    #Variavel e loop para garantir que seja inserido um valor aceito
    verificadorResposta = False
    while verificadorResposta == False:
        continuar = str(input("Gostaria de finalizar a compra? (Sim ou Não) ")).lower() 
        #Continua o loop
        if continuar == "não" or continuar == "nao":
            verificadorResposta = True
            next
        #Realiza as operações e encerra o programa principal levando à parte de pagamento
        elif continuar == "sim":
            verificadorResposta = True
            pedindo = False
            possuiDesconto, desconto, valorDoDesconto = verificarDesconto(total)
            if possuiDesconto == True:
                valorFinal = total*desconto
            else:
                valorFinal = total
        #Caso de valor inválido
        else:
            print("Resposta inválida! Insira uma resposta válida")
            verificadorResposta = False

#Escolher forma de pagamento
print("""
Formas de pagamento
1. Dinheiro
2. PIX
3. Cartão
""")
#Variavel e loop para garantir que seja inserido um valor aceito
escolhendoPagamento = True
while escolhendoPagamento:
    formaDePagamento = input("Insira o código da forma de pagamento desejada: ")
    if formaDePagamento == "1" or formaDePagamento == "2" or formaDePagamento == "3":
        match formaDePagamento:
            case "1":
                formaDePagamento = "Dinheiro"
            case "2":
                formaDePagamento = "Pix"
            case "3":
                formaDePagamento = "Cartão"
        escolhendoPagamento = False
    else:
        print("Resposta inválida! Insira uma resposta válida")

#Saídas do programa
print("")
print(f"Nome do cliente: {nomeCliente}")
print(f"Valor original da compra: R${total}")
print(f"Desconto aplicado: {valorDoDesconto}%")
print(f"Valor do desconto: R${total-valorFinal}")
print(f"Valor final a ser pago: R${valorFinal}")
print(f"Forma de pagamento: {formaDePagamento}")