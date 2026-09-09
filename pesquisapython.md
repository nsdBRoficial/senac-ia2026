Aqui está um guia de referência completo e estruturado com os principais comandos e sintaxes do Python. Este formato está pronto para ser salvo em um arquivo `.md`.

## 1. Variáveis e Tipos de Dados

Em Python, a tipagem é dinâmica, o que significa que o interpretador infere o tipo de dado automaticamente.

| Tipo | Descrição | Exemplo |
| --- | --- | --- |
| **`int`** | Números inteiros | `idade = 30` |
| **`float`** | Números com casas decimais | `preco = 19.99` |
| **`str`** | Cadeia de caracteres (texto) | `nome = "Maria"` |
| **`bool`** | Valores lógicos | `ativo = True` |
| **`None`** | Ausência de valor | `resultado = None` |

```python
# Conversão de tipos (Casting)
numero = int("10")
texto = str(100)
decimal = float(5)

```

---

## 2. Operadores Principais

### Matemáticos e Atribuição

* **`+`, `-`, `*`, `/**`: Operações básicas.
* **`//`**: Divisão inteira (ex: `10 // 3` resulta em `3`).
* **`**`**: Exponenciação (ex: `2 ** 3` resulta em `8`).
* **`%`**: Módulo/Resto da divisão (ex: `10 % 3` resulta em `1`).
* **`+=`, `-=`, `*=**`: Atribuição com operação (ex: `x += 1` é igual a `x = x + 1`).

### Lógicos e Comparação

* **`==`, `!=**`: Igual a, Diferente de.
* **`>`, `<`, `>=`, `<=**`: Maior, Menor, Maior ou igual, Menor ou igual.
* **`and`, `or`, `not**`: E lógico, OU lógico, Negação.

---

## 3. Estruturas de Controle

### Condicionais (`if`, `elif`, `else`)

```python
idade = 18

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")

```

### Laços de Repetição (`for`, `while`)

```python
# FOR: Iterando sobre uma sequência ou intervalo
for i in range(1, 5):  # Conta de 1 a 4
    print(i)

# FOR: Iterando sobre listas
frutas = ["maçã", "uva", "pera"]
for fruta in frutas:
    print(fruta)

# WHILE: Executa enquanto a condição for verdadeira
contador = 0
while contador < 3:
    print(contador)
    contador += 1

```

---

## 4. Estruturas de Dados

Python possui coleções nativas poderosas para armazenar múltiplos itens.

```python
# 1. LISTAS (Mutáveis e ordenadas)
lista = [1, 2, 3, "quatro"]
lista.append(5)          # Adiciona ao final
lista.remove(2)          # Remove o elemento '2'
primeiro = lista[0]      # Acessa o primeiro item

# 2. TUPLAS (Imutáveis e ordenadas)
coordenadas = (10.0, 20.5)
# coordenadas[0] = 15.0  <-- Isso geraria um erro

# 3. DICIONÁRIOS (Chave-Valor, mutáveis)
usuario = {
    "nome": "João",
    "idade": 25
}
usuario["email"] = "joao@email.com" # Adiciona nova chave
print(usuario.keys())               # Retorna todas as chaves

# 4. SETS (Conjuntos não ordenados de itens únicos)
numeros = {1, 2, 2, 3, 4} # O resultado será {1, 2, 3, 4}

```

---

## 5. Funções

Blocos de código reutilizáveis. Python usa indentação para definir o escopo.

```python
# Função tradicional com parâmetro padrão
def saudacao(nome="Visitante"):
    return f"Olá, {nome}!"

print(saudacao("Carlos"))

# Função Lambda (Função anônima de uma linha)
dobro = lambda x: x * 2
print(dobro(5)) # Retorna 10

```

---

## 6. Tratamento de Erros e Exceções

Previne que o programa quebre inesperadamente ao encontrar um erro.

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except Exception as e:
    print(f"Ocorreu um erro genérico: {e}")
finally:
    print("Este bloco sempre é executado, com ou sem erro.")

```

---

## 7. Manipulação de Arquivos

O gerenciador de contexto `with` é a forma mais segura de lidar com arquivos, pois fecha o arquivo automaticamente.

```python
# Escrevendo em um arquivo (o modo 'w' sobrescreve, 'a' adiciona)
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha do arquivo.\n")

# Lendo de um arquivo
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

```

---

## 8. Programação Orientada a Objetos (POO)

```python
class Animal:
    # Método construtor
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        
    def emitir_som(self):
        return f"O {self.especie} {self.nome} fez um barulho."

# Instanciando um objeto
meu_pet = Animal("Rex", "Cachorro")
print(meu_pet.emitir_som())

```
