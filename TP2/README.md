# TP2

Aluno: Ângelo Francisco Gonçalves Fernandes.  
Id: A112434.

![Ângelo Fernandes](../angelo.png)

## Enunciado

Criar em Python um conversor simples de Markdown para HTML que suporte:

- Cabeçalhos `#`, `##` e `###`;
- Texto em **bold**;
- Texto em *itálico*;
- Listas numeradas;
- Links;
- Imagens.

## Resolução

### Formatação de texto

Foi criada a função `inline_to_html`, responsável pelas conversões que podem aparecer dentro de uma linha: bold, itálico, links e imagens. Para isso são usadas expressões regulares com `re.sub`.

### Cabeçalhos

As linhas que começam por `#`, `##` ou `###` são identificadas e convertidas, respetivamente, para `h1`, `h2` e `h3`.

### Listas numeradas

Quando é encontrada uma linha no formato `n. texto`, é criada uma lista `<ol>` e cada elemento é colocado num `<li>`. A lista termina quando aparece uma linha que já não é um item numerado.

### Conversão do ficheiro

O programa lê um ficheiro Markdown passado como argumento e escreve o HTML correspondente no terminal. O resultado pode ser redirecionado diretamente para um ficheiro:

```bash
python3 tp2.py teste.md > resultado.html
```

## Resultados

Para testar o programa foi usado um ficheiro com exemplos de todas as construções pedidas no enunciado.

- [Programa](tp2.py)
- [Markdown de teste](teste.md)
- [HTML obtido](resultado.html)
