#calculadora

continuar = input("Desaja continuar: ")

while continuar == ("sim"):
    if continuar in ['sim', 'Sim', 'SIM']:
            n1 = int(input("Digite o n1: "))
            n2 = int(input("Digite o n2: "))
            
            operacao = input("Escolha a operação: ")
            
            if operacao == ("soma"):
                print(n1 + n2)
            elif operacao == ("subtração"):
                print(n1 - n2)
            elif operacao == ("multiplicação"):
                print(n1 * n2)
            elif operacao == ("divisão"):
                if n2 == 0:
                    print("Não é possível a divisão com o denominador sendo zero") 
                elif n2 != 0:
                    print(n1 / n2)               
                
                
            continuar = input("Deseja continuar: ")    
else:
    if continuar == ("não"):
        print("Ok até mais")
    else:
        print("Resposta inválida") 
        
        
    
    
    