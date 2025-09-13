i = 1
# Enquanto I for menor que 6
while i < 6:
    print(i)
    i = i + 1
print("-------------------------------------------")
#  Pare o código quando o i valer 3 

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i = i + 1

print("----------------------------------------------")

# Break para o looping 
# Continue pula para o proximo looping

print("------------------------------------------------")

i = 1
while i < 6:
    i = i + 1
    if i ==3:
        continue
    print(i)