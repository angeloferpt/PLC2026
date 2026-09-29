# TP1

Aluno: Ângelo Francisco Gonçalves Fernandes.\
Id: A112434.

![Ângelo Fernandes](angelo.png)

## Enunciado

Escrever uma expressão regular que reconheça strings binárias que não contenham a substring `011`.

## Resolução

```regex
^1*(01?)*$
```