idade = int(input("'digite sua idade: "))
dinheiro = int(input("digite a quantidade de dinheiro que vc tem:"))
carteira = input("vc tem carteira de motorista? (s/n)")

if (idade >= 18 and dinheiro >=50)or carteira =="s":
    print("voce pode alugar um carro.")
else:
    print("voce nao pode alugar um carro")
