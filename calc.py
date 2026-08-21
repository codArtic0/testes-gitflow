def soma(a,b):
    return a+b;

if __name__ == "__main__":
    print("Calculadora inicial: ")
    print()
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    print()
    result = soma(a,b)
    print("Resultado: " + result)