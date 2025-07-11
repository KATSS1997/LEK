# Calculadora Simples em Python

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    else:
        return x / y

def main():
    print("Calculadora Simples")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Escolha a operação: ")

    if escolha == "1":
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        print("Resultado:", soma(x, y))
    elif escolha == "2":
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        print("Resultado:", subtracao(x, y))
    elif escolha == "3":
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        print("Resultado:", multiplicacao(x, y))
    elif escolha == "4":
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        print("Resultado:", divisao(x, y))
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()