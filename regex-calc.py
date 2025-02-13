import re;
SUM = 1
SUB = 2
MULT = 3
DIV = 4

def busca_operacao(text):
    accumulator = 0
    while(1):
        num1 = 0
        num2 = 0
        sumRes = re.search(sumPatt, text)
        subRes = re.search(subPatt, text)
        multRes = re.search(multPatt, text)
        divRes = re.search(divPatt, text)
        if(divRes):
            num1 = float(divRes.group(1))
            num2 = float(divRes.group(3))
            if(num2 == 0): print("Não é possível dividir por 0")
            else: 
                accumulator = num1 / num2
                text = text.replace(divRes.group(), str(accumulator))
        elif(multRes):
            num1 = float(multRes.group(1))
            num2 = float(multRes.group(3))
            accumulator = num1 * num2
            text = text.replace(multRes.group(), str(accumulator))
        elif(sumRes): 
            if(sumRes.group(1) == ""): num1 = 0
            else: num1 = float(sumRes.group(1))
            num2 = float(sumRes.group(3))
            accumulator = num1 + num2
            text = text.replace(sumRes.group(), str(accumulator))
        elif(subRes): 
            if(subRes.group(1) == ""): num1 = 0
            else: num1 = float(subRes.group(1))
            num2 = float(subRes.group(3))
            accumulator = num1 - num2
            text = text.replace(subRes.group(), str(accumulator))
            if(accumulator == float(text)): break
        else: break
    return accumulator

#nenhum ou mais dígito "+" Pelo menos 1 dígito
sumPatt = r"(\d*\.?\d*)(\s*\+\s*)(\d*\.?\d*)"
#nenhum ou mais dígito "-" Pelo menos 1 dígito
subPatt = r"(\d*\.?\d*)(\s*\-\s*)(\d*\.?\d*)"
# Pelo menos um dígito "*" Pelo menos 1 dígito
multPatt = r"(\d*\.?\d*)(\s*\*\s*)(\d*\.?\d*)"
# Pelo menos 1 Dígito "/" Pelo menos 1 Dígito != 0
divPatt = r"(\d*\.?\d*)(\s*\/\s*)(\d*\.?\d*)"

accumulator = 0
text = ""
while (text != "\3"):
    text = input("")
    print(f"Resultado: {busca_operacao(text)}")


# "3 + 5" 	8
# " 10 - 2 * 3 " 	4
# "4 + 8 / 2" 	8
# "2.5 * 4 - 1" 	9
# "(3 + 5) * 2" 	16 (se implementar parênteses)

# Exemplo
# text = "Meu número de telefone é 123-456-7890"
# padrao = r"\d{3}-\d{3}-\d{4}"

# resultado = re.search(padrao, text)
# if resultado:
#     print("Encontrado:", resultado.group())
# else:
#     print("Não encontrado")
