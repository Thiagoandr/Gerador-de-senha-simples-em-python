import random 
min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
simbolo = '[]{}()*#;/,-_%'
quantidade = int(input('Digite qual tamanho da senha(recomendavel 8): '))
length = quantidade
total = min + max + num + simbolo
senha_total = "".join(random.sample(total,length))
print("sua senha é",senha_total)




