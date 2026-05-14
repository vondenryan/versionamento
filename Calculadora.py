import Operacoes

def start():
    val1 = int(input("Digite o valor 1: "))
    val2 = int(input("Digite o valor 2: "))

    operacao = int(input("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n-> "))
    result = None

    match operacao:
        case 1:
            result = Operacoes.soma(val1, val2)
        case 2:
            result = Operacoes.subtracao(val1, val2)
        case 3:
            result = Operacoes.multiplicacao(val1, val2)
        case 4:
            result = Operacoes.divisao(val1, val2)
        case _:
            print("Operação inválida!")

    print(f"Resultado da operação é: {result}")