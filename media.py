print("___________________________________________")
print()
# Primeiro, vamos pedir as duas notas pro usuário
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

# Calculando a média
media = (nota1 + nota2)/ 2

# Mostrando a média
print(f"A média do aluno é:  {media}")

# Agora vem a decisão: aprovado, recuperação ou reprovado
if media >= 6:
    print("Aluno aprovado")
elif media >= 4:
    print("Aluno em recuperação")  
else:
    print("Aluno reprovado")