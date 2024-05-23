def Abastecer():
    tanque = "cheio" #variável local
    print("-Frentista: Abastecimento realizado. Seu tanque ficou", tanque)

#Bloco principal
tanque = "vazio" #variável global
print("-Você: Chegando no posto meu tanque estava", tanque) #variável vazio

Abastecer() #função abastecer = cheio
print("-Você: Saindo do posto meu tanque estava", tanque) #variável vazio