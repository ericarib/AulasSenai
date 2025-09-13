
'''
for num in range( 1 ,11):
    print("*")

for num in range(1, 10):
    for num2 in range(num):
        print("*", end=" ")
    print("")

for num in range(8):
    for num2 in range(8):
        print("*", end=" ")
    print("")
# Piramide invertida


logica função range (incio, fim, intervalo)


for num in range(11, 0, -1):
    for num2 in range(num):
        print("*", end=" ")
    print("")
'''
'''
# Piramide invertida
print("Piramide invertida")
for num in range(10, 1):
    for num2 in range(num, -1):
        print("*", end=" ")
    print("")
'''

print("Piramide completa")
# Piramide completa
for num in range(1, 10):
    for num2 in range(num):
        print("*", end=" ")
    print("")

for num in range(-10, 1):
    for num2 in range(-num):
        print("*", end=" ")
    print("")


print("Piramide invertida")

for num in range(-10, 1):
    for num2 in range(-num):
        print("*", end=" ")
    print("")   