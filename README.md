# senac-ia2026
Repositório da turma de IA do senac 2026.

```python
# Vamos criar um arquivo markdown completo demonstrando todas as funcionalidades do Markdown de forma didática.
markdown_content = """# 📚 Manual Definitivo de Markdown (Cheat Sheet & Guia Didático)

Bem-vindo ao manual completo de Markdown! Este documento foi estruturado para demonstrar **todas** as principais funções, sintaxes e recursos avançados do Markdown de forma prática, bonita e didática. 

Você pode usar este arquivo como referência sempre que precisar formatar textos no GitHub, Notion, VS Code, Discord ou qualquer outra plataforma compatível.

---

## 📋 Sumário
1. [Títulos (Headings)](#1-títulos-headings)
2. [Formatação de Texto](#2-formatação-de-texto)
3. [Listas e Organização](#3-listas-e-organização)
4. [Links e Imagens](#4-links-e-imagens)
5. [Citações (Blockquotes)](#5-citações-blockquotes)
6. [Blocos de Código e Sintaxe](#6-blocos-de-código-e-sintaxe)
7. [Tabelas](#7-tabelas)
8. [Elementos Avançados](#8-elementos-avançados)

---

## 1. Títulos (Headings)
Os títulos são criados usando o caractere cerquilha (`#`) no início da linha. Quanto mais cerquilhas, menor o nível do título (de 1 a 6).

# Título H1 (Principal)
## Título H2 (Seção)
### Título H3 (Subseção)
#### Título H4
##### Título H5
###### Título H6

---

## 2. Formatação de Texto
Você pode alterar a ênfase e o estilo do texto utilizando asteriscos (`*`), sublinhados (`_`), tils (`~`) ou crases (`` ` ``).

* **Negrito:** Use `**texto**` ou `__texto__` para obter **negrito**.
* *Itálico:* Use `*texto*` ou `_texto_` para obter *itálico*.
* **_Negrito e Itálico_:** Use `***texto***` para combinar ambos.
* ~~Tachado (Rascunho):~~ Use `~~texto~~` para riscar o texto.
* <u>Sublinhado:</u> Em alguns flavors, usa-se tag HTML `<u>texto</u>`.
* `Texto em código (inline)`: Use crases simples `` `texto` `` para destacar termos técnicos.

---

## 3. Listas e Organização

### Listas Não Ordenadas (Bullet Points)
Você pode usar asterisco (`*`), hífen (`-`) ou sinal de mais (`+`).

* Item principal da lista
  * Sub-item com recuo (espaço duplo ou tab)
    * Sub-sub-item ainda mais interno
* Outro item principal
  * Outro sub-item

### Listas Ordenadas (Numeradas)
Basta usar números seguidos de ponto. O Markdown numera automaticamente na exibição.

1. Primeiro passo da tarefa
2. Segundo passo da tarefa
   1. Passo intermediário A
   2. Passo intermediário B
3. Terceiro passo da tarefa

### Listas de Tarefas (Task Lists)
Perfeitas para acompanhar o progresso de issues ou projetos.

- [x] Estudar a documentação do Git e do GitHub
- [x] Criar o primeiro repositório local
- [ ] Subir o código para o servidor remoto (`git push`)
- [ ] Solicitar o primeiro Code Review

---

## 4. Links e Imagens

### Links
Você pode criar links nomeados ou links diretos.

* [Visite o site oficial do Git](https://git-scm.com/)
* Link automático direto: <https://github.com>

### Imagens
Para inserir imagens, a sintaxe é parecida com a de links, mas precedida por um ponto de exclamação `!`.

![Logotipo do Git](https://git-scm.com/images/logos/downloads/Git-Icon-178C.png)

---

## 5. Citações (Blockquotes)
Úteis para destacar avisos, citações de falas ou notas importantes.

> "A simplicidade é o pré-requisito para a confiabilidade."
> — *Edsger W. Dijkstra*

> **Nota do Instrutor:**
> > Citações também podem ser aninhadas colocando mais de um sinal de maior (`>`) lado a lado.

---

## 6. Blocos de Código e Sintaxe
Ideal para desenvolvedores compartilharem códigos formatados e coloridos (syntax highlighting).

```python
# Exemplo de código em Python formatado
def cumprimentar_estagiario(nome):
    mensagem = f"Olá, {nome}! Bem-vindo à equipe de engenharia."
    print(mensagem)

cumprimentar_estagiario("Novo Desenvolvedor")

```

```javascript
// Exemplo de código em JavaScript
const statusProjeto = "Em andamento";
console.log(`O status atual do projeto é: ${statusProjeto}`);

```

---

## 7. Tabelas

As tabelas são construídas usando barras verticais (`|`) para separar colunas e hífens (`-`) para estruturar o cabeçalho.

| Elemento Markdown | Sintaxe | Resultado Visual |
| --- | --- | --- |
| **Negrito** | `**texto**` | **texto** |
| *Itálico* | `*texto*` | *texto* |
| `Código` | ``código`` | `código` |
| Tachado | `~~texto~~` | ~~texto~~ |

*(Nota: Os dois pontos `:` nas linhas divisórias definem o alinhamento: `:---` esquerda, `:---:` centralizado, `---:` direita).*

---

## 8. Elementos Avançados

### Linha Divisória (Horizontal Rule)

Você pode usar três asteriscos (`***`), hífens (`---`) ou sublinhados (`___`) em uma linha vazia.

---

### Notas de Rodapé (Footnotes)

Você pode adicionar notas explicativas no texto que direcionam para o rodapé[^1].

[^1]: Esta é a nota de rodapé explicativa que aparece no final do documento.

### Blocos Colapsáveis (Details / Summary)

Útil para esconder informações longas ou respostas de gabarito.

Parabéns! Você descobriu como usar tags HTML customizadas dentro de arquivos Markdown para criar elementos interativos avançados.

---

*Manual criado especialmente para guiar desenvolvedores iniciantes.*
"""

with open("README_Completo.md", "w", encoding="utf-8") as f:
f.write(markdown_content)
print("Arquivo README_Completo.md gerado com sucesso!")

```

```text?code_stdout&code_event_index=1
Arquivo README_Completo.md gerado com sucesso!


```

O seu arquivo README completo foi gerado com sucesso!

Seu arquivo `README_Completo.md` está pronto. Abaixo apresento o conteúdo integral para você visualizar e utilizar diretamente:

---

```markdown
# 📚 Manual Definitivo de Markdown (Cheat Sheet & Guia Didático)

Bem-vindo ao manual completo de Markdown! Este documento foi estruturado para demonstrar **todas** as principais funções, sintaxes e recursos avançados do Markdown de forma prática, bonita e didática. 

Você pode usar este arquivo como referência sempre que precisar formatar textos no GitHub, Notion, VS Code, Discord ou qualquer outra plataforma compatível.

---

## 📋 Sumário
1. [Títulos (Headings)](#1-títulos-headings)
2. [Formatação de Texto](#2-formatação-de-texto)
3. [Listas e Organização](#3-listas-e-organização)
4. [Links e Imagens](#4-links-e-imagens)
5. [Citações (Blockquotes)](#5-citações-blockquotes)
6. [Blocos de Código e Sintaxe](#6-blocos-de-código-e-sintaxe)
7. [Tabelas](#7-tabelas)
8. [Elementos Avançados](#8-elementos-avançados)

---

## 1. Títulos (Headings)
Os títulos são criados usando o caractere cerquilha (`#`) no início da linha. Quanto mais cerquilhas, menor o nível do título (de 1 a 6).

# Título H1 (Principal)
## Título H2 (Seção)
### Título H3 (Subseção)
#### Título H4
##### Título H5
###### Título H6

---

## 2. Formatação de Texto
Você pode alterar a ênfase e o estilo do texto utilizando asteriscos (`*`), sublinhados (`_`), tils (`~`) ou crases (`` ` ``).

* **Negrito:** Use `**texto**` ou `__texto__` para obter **negrito**.
* *Itálico:* Use `*texto*` ou `_texto_` para obter *itálico*.
* **_Negrito e Itálico_:** Use `***texto***` para combinar ambos.
* ~~Tachado (Rascunho):~~ Use `~~texto~~` para riscar o texto.
* <u>Sublinhado:</u> Em alguns flavors, usa-se tag HTML `<u>texto</u>`.
* `Texto em código (inline)`: Use crases simples `` `texto` `` para destacar termos técnicos.

---

## 3. Listas e Organização

### Listas Não Ordenadas (Bullet Points)
Você pode usar asterisco (`*`), hífen (`-`) ou sinal de mais (`+`).

* Item principal da lista
  * Sub-item com recuo (espaço duplo ou tab)
    * Sub-sub-item ainda mais interno
* Outro item principal
  * Outro sub-item

### Listas Ordenadas (Numeradas)
Basta usar números seguidos de ponto. O Markdown numera automaticamente na exibição.

1. Primeiro passo da tarefa
2. Segundo passo da tarefa
   1. Passo intermediário A
   2. Passo intermediário B
3. Terceiro passo da tarefa

### Listas de Tarefas (Task Lists)
Perfeitas para acompanhar o progresso de issues ou projetos.

- [x] Estudar a documentação do Git e do GitHub
- [x] Criar o primeiro repositório local
- [ ] Subir o código para o servidor remoto (`git push`)
- [ ] Solicitar o primeiro Code Review

---

## 4. Links e Imagens

### Links
Você pode criar links nomeados ou links diretos.

* [Visite o site oficial do Git](https://git-scm.com/)
* Link automático direto: <https://github.com>

### Imagens
Para inserir imagens, a sintaxe é parecida com a de links, mas precedida por um ponto de exclamação `!`.

![Logotipo do Git](https://git-scm.com/images/logos/downloads/Git-Icon-178C.png)

---

## 5. Citações (Blockquotes)
Úteis para destacar avisos, citações de falas ou notas importantes.

> "A simplicidade é o pré-requisito para a confiabilidade."
> — *Edsger W. Dijkstra*

> **Nota do Instrutor:**
> > Citações também podem ser aninhadas colocando mais de um sinal de maior (`>`) lado a lado.

---

## 6. Blocos de Código e Sintaxe
Ideal para desenvolvedores compartilharem códigos formatados e coloridos (syntax highlighting).

```python
# Exemplo de código em Python formatado
def cumprimentar_estagiario(nome):
    mensagem = f"Olá, {nome}! Bem-vindo à equipe de engenharia."
    print(mensagem)

cumprimentar_estagiario("Novo Desenvolvedor")

```

```javascript
// Exemplo de código em JavaScript
const statusProjeto = "Em andamento";
console.log(`O status atual do projeto é: ${statusProjeto}`);

```

---

## 7. Tabelas

As tabelas são construídas usando barras verticais (`|`) para separar colunas e hífens (`-`) para estruturar o cabeçalho.

| Elemento Markdown | Sintaxe | Resultado Visual |
| --- | --- | --- |
| **Negrito** | `**texto**` | **texto** |
| *Itálico* | `*texto*` | *texto* |
| `Código` | ``código`` | `código` |
| Tachado | `~~texto~~` | ~~texto~~ |

*(Nota: Os dois pontos `:` nas linhas divisórias definem o alinhamento: `:---` esquerda, `:---:` centralizado, `---:` direita).*

---

## 8. Elementos Avançados

### Linha Divisória (Horizontal Rule)

Você pode usar três asteriscos (`***`), hífens (`---`) ou sublinhados (`___`) em uma linha vazia.

---

### Notas de Rodapé (Footnotes)

Você pode adicionar notas explicativas no texto que direcionam para o rodapé[^1].

[^1]: Esta é a nota de rodapé explicativa que aparece no final do documento.

### Blocos Colapsáveis (Details / Summary)

Útil para esconder informações longas ou respostas de gabarito.

Parabéns! Você descobriu como usar tags HTML customizadas dentro de arquivos Markdown para criar elementos interativos avançados.

---

*Manual criado especialmente para guiar desenvolvedores iniciantes.*

```

***

O arquivo `README_Completo.md` já está salvo no seu ambiente de trabalho pronto para ser utilizado ou versionado!

```
