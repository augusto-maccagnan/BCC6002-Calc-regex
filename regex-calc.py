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
        numRes = re.search(numPatt, text)
        sumRes = re.search(sumPatt, text)
        subRes = re.search(subPatt, text)
        multRes = re.search(multPatt, text)
        divRes = re.search(divPatt, text)
        if(divRes):
            num1 = float(divRes.group(1))
            num2 = float(divRes.group(3))
            if(num2 == 0):
                print("Não é possível dividir por 0")
                return 0
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
        elif(numRes):
            accumulator = float(numRes.group())
            break
        else: break
    return accumulator

def busca_parenteses(text):
    parentRes = re.search(parentPatt, text)
    if(parentRes):
        # Substituindo o resultado da operação dentro do parênteses pelo match do par de parênteses
        text = text.replace(parentRes.group(), str(busca_operacao(parentRes.group(0))))
        return busca_parenteses(text)
    else:
        return busca_operacao(text)
    
#nenhum ou mais dígito "." nenhum ou mais dígito
numPatt = r"\d+\.?\d*"
#nenhum ou mais dígito "+" Pelo menos 1 dígito
sumPatt = r"(\d*\.?\d*)(\s*\+\s*)(\d+\.?\d*)"
#nenhum ou mais dígito "-" Pelo menos 1 dígito
subPatt = r"(\d*\.?\d*)(\s*\-\s*)(\d+\.?\d*)"
# Pelo menos um dígito "*" Pelo menos 1 dígito
multPatt = r"(\d+\.?\d*)(\s*\*\s*)(\d+\.?\d*)"
# Pelo menos 1 Dígito "/" Pelo menos 1 Dígito != 0
divPatt = r"(\d+\.?\d*)(\s*\/\s*)(\d+\.?\d*)"
# Par de parênteses
parentPatt  = r"\([^\(\)]*\)"

text = ""
while (text != '\3'):
    text = input("")
    print(f"Resultado: {busca_parenteses(text)}")


# "3 + 5" 	8
# " 10 - 2 * 3 " 	4
# "4 + 8 / 2" 	8
# "2.5 * 4 - 1" 	9
# "(3 + 5) * 2" 	16 (se implementar parênteses)
