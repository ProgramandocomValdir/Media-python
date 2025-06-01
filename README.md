# 📚 Cálculo de Média em Python

Este projeto ensina como calcular a média de duas notas usando Python, aplicando as estruturas condicionais **if, elif e else**.

Perfeito para quem está começando na programação e quer entender lógica de decisão de forma prática.

## 🚀 Funcionalidades do código:
- ✅ Solicita duas notas do usuário
- ✅ Calcula a média entre as notas
- ✅ Mostra se o aluno está:
  - ✔️ Aprovado (média ≥ 6)
  - ⚠️ Recuperação (média ≥ 4 e < 6)
  - ❌ Reprovado (média < 4)

## 💻 Código em Python:

```python
# Programa para calcular a média de duas notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A média do aluno é: {media}")

if media >= 6:
    print("Aluno aprovado!")
elif media >= 4:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")
