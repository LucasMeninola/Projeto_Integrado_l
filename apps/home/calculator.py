import sqlite3

valor_bandeira = {
'verde': 0.0,
'cinza': 0.1420 ,#BANDEIRA CINZA É COR DE CRISE HIDRICA
'amarela': 0.01874,
'vermelha1': 0.03971,
'vermelha2': 0.09492
}

icms = 25 #PESQUISAR UMA FORMA DE BUSCA ESSE VALOR NO SITE OFICIAL DA ENEL
calculadora = True

while calculadora:
    kwh = input("Total de Kwh gerado no mês: ")
    sair = "q"
    
    if kwh == sair:
        calculadora = False

    try:
        calc_consumo_Kilowatts = valor_bandeira['cinza'] * float(kwh)#calculo baseado na bandeira
        calc_conta_enel = calc_consumo_Kilowatts * icms/100 +(calc_consumo_Kilowatts)#calculo baseado no icms mais badeira e consul
        calc_taxa_concessionaria =  calc_conta_enel - calc_consumo_Kilowatts#calculo baseado só na concessionaria

        #criar a taxa de porcentagem baseado na porcentagem
        
        #print é para comprender a parte do codigo na hora de calcular os valores para debug
        print("Valor basedo no consumo de Kw/M: {}".format(calc_consumo_Kilowatts))
        print('Valor baseado com as taxas da concessionária: {}'.format(calc_conta_enel))
        print("Valor só de taxa da concessionária: {}".format(calc_taxa_concessionaria))

    except ValueError as msg:
        print("Valor errado ou adicionado caracter, tente colocar numeros inteiros")

print("Você saiu da calculadora!")