"""
Calculadora Interativa em Python
Módulo com funções matemáticas, histórico de cálculos e suporte a operações avançadas.
"""

import math

historico = []


def obter_numero(mensagem: str) -> float:
    """Solicita um número ao usuário e trata erros de digitação."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um valor numérico válido.")


def adicionar_historico(operacao: str, resultado: float) -> None:
    """Registra uma operação e seu resultado no histórico."""
    historico.append(f"{operacao} = {resultado}")


def exibir_historico() -> None:
    """Exibe todas as operações realizadas na sessão atual."""
    print("\n--- HISTÓRICO DE CÁLCULOS ---")
    if not historico:
        print("Nenhum cálculo realizado até o momento.")
    else:
        for idx, item in enumerate(historico, 1):
            print(f"{idx}. {item}")
    print("-----------------------------")


def soma(a: float, b: float) -> float:
    return a + b


def subtracao(a: float, b: float) -> float:
    return a - b


def multiplicacao(a: float, b: float) -> float:
    return a * b


def divisao(a: float, b: float):
    if b == 0:
        return None
    return a / b


def potencia(base: float, expoente: float) -> float:
    return base ** expoente


def raiz_quadrada(numero: float):
    if numero < 0:
        return None
    return math.sqrt(numero)


def porcentagem(valor: float, percentual: float) -> float:
    return (valor * percentual) / 100


def menu_calculadora():
    """Loop principal de interação com o usuário."""
    while True:
        print("\n===============================")
        print("   CALCULADORA PYTHON AVANÇADA")
        print("===============================")
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Potenciação (^)")
        print("6 - Raiz Quadrada (√)")
        print("7 - Porcentagem (%)")
        print("8 - Ver Histórico")
        print("0 - Sair")
        print("===============================")

        opcao = input("Selecione uma opção: ").strip()

        if opcao == "0":
            print("\nObrigado por usar a calculadora. Até mais!")
            break

        elif opcao == "8":
            exibir_historico()
            continue

        elif opcao == "6":
            num = obter_numero("Digite o número para calcular a raiz quadrada: ")
            resultado = raiz_quadrada(num)
            if resultado is None:
                print("Erro: Não é possível calcular raiz quadrada de número negativo nos Reais.")
            else:
                expr = f"√{num}"
                adicionar_historico(expr, resultado)
                print(f"\nResultado: {expr} = {resultado}")

        elif opcao in ["1", "2", "3", "4", "5", "7"]:
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")

            if opcao == "1":
                resultado = soma(num1, num2)
                expr = f"{num1} + {num2}"
            elif opcao == "2":
                resultado = subtracao(num1, num2)
                expr = f"{num1} - {num2}"
            elif opcao == "3":
                resultado = multiplicacao(num1, num2)
                expr = f"{num1} * {num2}"
            elif opcao == "4":
                resultado = divisao(num1, num2)
                if resultado is None:
                    print("\nErro: Divisão por zero não é permitida.")
                    continue
                expr = f"{num1} / {num2}"
            elif opcao == "5":
                resultado = potencia(num1, num2)
                expr = f"{num1} ^ {num2}"
            elif opcao == "7":
                resultado = porcentagem(num1, num2)
                expr = f"{num2}% de {num1}"

            adicionar_historico(expr, resultado)
            print(f"\nResultado: {expr} = {resultado}")

        else:
            print("Opção inválida! Escolha um número válido entre 0 e 8.")


if __name__ == "__main__":
    menu_calculadora()

