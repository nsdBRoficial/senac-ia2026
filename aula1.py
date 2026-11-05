# O caractere '#' cria um comentário que a máquina ignora. Serve apenas para humanos.
# A função print exibe mensagens na tela do Terminal.
# Isso é fundamental para debugar (verificar o que o código está fazendo).

print("Hello, World! O interpretador Python está online.")
print("A CPU acabou de processar e renderizar esta mensagem.")
print("Olá, eu sou Douglas")
print("vai desabar o mundo")

# Conceito de variaveis

nome = "Sistema"        # String (Texto)
versao = 2              # Integer (numero inteiro)
nota = 9.5              # Float

print("---Dados Salvos---")
print("Nome:", nome)
print("Versão", versao)
print(f"O {nome} esta na {versao} e sua nota é {nota}.")

# Conceito de input

print("---CALCULADORA BÁSICA ----")

# Coletando os numeros e já conrtendo para decimais (float) para aceitar numeros quebrados
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Processando as opereações matematicas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# Exibinado os resultados
print("\n --- RESULTADOS ---")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicacação: {multiplicacao}")
print(f"Divisão: {divisao}")

print("=== Calculadora Completa em Python ===")

# O loop 'while True' mantém o programa rodando em um ciclo infinito 
# até que o comando 'break' seja acionado.
while True:
    print("\nSelecione a operação desejada:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("0 - Sair")

    # Coleta a escolha do usuário como texto (String)
    escolha = input("Digite o número da operação (0 a 4): ")

    # Condição de saída do programa
    if escolha == '0':
        print("Encerrando a calculadora. Até logo!")
        break

    # Validação de entrada: se a escolha não estiver na lista permitida, 
    # o 'continue' reinicia o loop para pedir novamente.
    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida! Tente novamente.")
        continue

    # O bloco try/except impede que o programa trave (crash) se o usuário digitar letras em vez de números.
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")
        continue

    # Estruturas condicionais (if/elif/else) para executar a operação escolhida
    if escolha == '1':
        resultado = num1 + num2
        print(f"\nResultado: {num1} + {num2} = {resultado}")
        
    elif escolha == '2':
        resultado = num1 - num2
        print(f"\nResultado: {num1} - {num2} = {resultado}")
        
    elif escolha == '3':
        resultado = num1 * num2
        print(f"\nResultado: {num1} * {num2} = {resultado}")
        
    elif escolha == '4':
        # Tratamento matemático para impedir erro fatal de divisão por zero
        if num2 == 0:
            print("\nErro: Não existe divisão por zero na matemática.")
        else:
            resultado = num1 / num2
            print(f"\nResultado: {num1} / {num2} = {resultado}")



