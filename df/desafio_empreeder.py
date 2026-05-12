#Luz do bem#
lampadas = 0
orçamento = int(input("a area que deseja iluminar (em metros quadrados): "))
if orçamento <= 0:
    print("Valor inválido. Por favor, insira um número positivo.")  
elif orçamento <= 50:
    print("Você precisará de 1 lâmpada.")
    lampadas = 1
elif orçamento <= 100:
    print("Você precisará de 2 lâmpadas.")
    lampadas = 2
elif orçamento <= 150:
    print("Você precisará de 3 lâmpadas.")
    lampadas = 3
elif orçamento <= 200:
    print("Você precisará de 4 lâmpadas.")
    lampadas = 4
elif orçamento <= 250:
    print("Você precisará de 5 lâmpadas.")
    lampadas = 5
elif orçamento <= 300:
    print("Você precisará de 6 lâmpadas.")
    lampadas = 6
elif orçamento <= 350:
    print("Você precisará de 7 lâmpadas.")
    lampadas = 7
elif orçamento <= 400:
    print("Você precisará de 8 lâmpadas.")
    lampadas = 8

if lampadas <= 2:
    print("O valor total a ser gasto é de R$ 100,00.")
elif lampadas <= 4:
    print("O valor total a ser gasto é de R$ 150,00.") 
elif lampadas <= 6:
    print("O valor total a ser gasto é de R$ 200,00.")
elif lampadas <= 8:
    print("O valor total a ser gasto é de R$ 250,00.")
elif lampadas <= 10:
    print("O valor total a ser gasto é de R$ 300,00.")
elif lampadas <= 12:
    print("O valor total a ser gasto é de R$ 350,00.")
elif lampadas <= 14:
    print("O valor total a ser gasto é de R$ 400,00.")
elif lampadas <= 16:
    print("O valor total a ser gasto é de R$ 450,00.")
elif lampadas <= 18:
    print("O valor total a ser gasto é de R$ 500,00.")