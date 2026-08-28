def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def calcular_imc(peso_kg, altura_m):
    """Calcula o IMC e retorna o valor junto com a classificação."""
    if altura_m <= 0:
        raise ValueError("A altura deve ser maior que zero.")

    imc = peso_kg / (altura_m ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade grau I"
    elif imc < 40:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    return round(imc, 2), classificacao


def menu():
    print("\n===== CALCULADORA =====")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Calcular IMC")
    print("0. Sair")


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número.")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Encerrando a calculadora.")
            break

        elif opcao in {"1", "2", "3", "4"}:
            a = ler_numero("Digite o primeiro número: ")
            b = ler_numero("Digite o segundo número: ")

            try:
                if opcao == "1":
                    resultado = somar(a, b)
                elif opcao == "2":
                    resultado = subtrair(a, b)
                elif opcao == "3":
                    resultado = multiplicar(a, b)
                elif opcao == "4":
                    resultado = dividir(a, b)

                print(f"Resultado: {resultado}")

            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "5":
            peso = ler_numero("Digite seu peso em kg: ")
            altura = ler_numero("Digite sua altura em metros: ")

            try:
                imc, classificacao = calcular_imc(peso, altura)
                print(f"Seu IMC é {imc} ({classificacao})")
            except ValueError as erro:
                print(f"Erro: {erro}")

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
