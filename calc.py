def soma(a,b):
    return a+b;

def subtracao(a,b):
    return a-b;

if __name__ == "__main__":
    print("Calculadora v1.0.0: ")
    print()
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    resultSoma = soma(a,b)
    resultSubtracao = subtracao(a,b)
    print()
    
    print("Soma: " + str(resultSoma))
    print("Subtracao: " + str(resultSubtracao))