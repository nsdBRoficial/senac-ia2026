print("=== Sistema CRUD: Gerenciador de Modelos de IA ===")

# Nossa "tabela" de banco de dados na memória RAM (uma lista vazia)
banco_de_dados = []
# Variável para controlar o ID (identificador único) de cada registro
proximo_id = 1

while True:
    print("\n" + "="*40)
    print("MENU PRINCIPAL")
    print("1 - Adicionar novo modelo (CREATE)")
    print("2 - Listar modelos cadastrados (READ)")
    print("3 - Atualizar um modelo (UPDATE)")
    print("4 - Excluir um modelo (DELETE)")
    print("0 - Sair do sistema")
    print("="*40)

    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Encerrando o sistema. Até logo!")
        break

    # ==========================================
    # C - CREATE (Criar / Inserir)
    # ==========================================
    elif opcao == '1':
        print("\n--- Adicionar Modelo ---")
        nome = input("Nome do modelo (ex: Llama 3, GPT-4): ")
        empresa = input("Empresa criadora (ex: Meta, OpenAI): ")
        
        # Criamos um Dicionário (chave/valor) para representar o dado
        novo_modelo = {
            "id": proximo_id,
            "nome": nome,
            "empresa": empresa
        }
        
        # Adicionamos o dicionário na nossa lista
        banco_de_dados.append(novo_modelo)
        print(f"✅ Modelo '{nome}' cadastrado com sucesso com o ID {proximo_id}!")
        
        proximo_id += 1 # Aumenta o ID para o próximo cadastro não repetir

    # ==========================================
    # R - READ (Ler / Listar)
    # ==========================================
    elif opcao == '2':
        print("\n--- Lista de Modelos ---")
        # Verifica se a lista está vazia
        if len(banco_de_dados) == 0:
            print("Nenhum modelo cadastrado ainda.")
        else:
            # O laço 'for' percorre cada item da lista
            for modelo in banco_de_dados:
                print(f"ID: {modelo['id']} | Nome: {modelo['nome']} | Empresa: {modelo['empresa']}")

    # ==========================================
    # U - UPDATE (Atualizar / Editar)
    # ==========================================
    elif opcao == '3':
        print("\n--- Atualizar Modelo ---")
        try:
            id_busca = int(input("Digite o ID do modelo que deseja atualizar: "))
            modelo_encontrado = False
            
            for modelo in banco_de_dados:
                if modelo['id'] == id_busca:
                    modelo_encontrado = True
                    print(f"Modelo atual: {modelo['nome']} ({modelo['empresa']})")
                    
                    # Coleta os novos dados
                    novo_nome = input("Digite o novo nome (ou aperte Enter para manter): ")
                    nova_empresa = input("Digite a nova empresa (ou aperte Enter para manter): ")
                    
                    # Só atualiza se o usuário digitou algo
                    if novo_nome != "":
                        modelo['nome'] = novo_nome
                    if nova_empresa != "":
                        modelo['empresa'] = nova_empresa
                        
                    print("✅ Modelo atualizado com sucesso!")
                    break # Sai do laço for, pois já achou o que precisava
            
            if not modelo_encontrado:
                print("❌ Erro: ID não encontrado.")
                
        except ValueError:
            print("❌ Erro: Por favor, digite um número de ID válido.")

    # ==========================================
    # D - DELETE (Deletar / Excluir)
    # ==========================================
    elif opcao == '4':
        print("\n--- Excluir Modelo ---")
        try:
            id_busca = int(input("Digite o ID do modelo que deseja excluir: "))
            modelo_encontrado = False
            
            # Usamos enumerate para saber a posição (índice) exata do item na lista
            for indice, modelo in enumerate(banco_de_dados):
                if modelo['id'] == id_busca:
                    modelo_encontrado = True
                    # Remove o item da lista usando o comando pop()
                    removido = banco_de_dados.pop(indice)
                    print(f"🗑️ Modelo '{removido['nome']}' excluído com sucesso!")
                    break
            
            if not modelo_encontrado:
                print("❌ Erro: ID não encontrado.")
                
        except ValueError:
            print("❌ Erro: Por favor, digite um número de ID válido.")

    # ==========================================
    # Validação de Opção Inválida
    # ==========================================
    else:
        print("❌ Opção inválida. Escolha um número de 0 a 4.")
