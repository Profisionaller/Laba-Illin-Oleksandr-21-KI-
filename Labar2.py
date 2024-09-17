a= "Illin"
b = "Oleksandr"
c = 17
list1=[a, b, c]
print(list1)
list2=[type(a), type(b), type(c)]
print(list2)
if type(a) == type(b) == type(c):
    print("Всі типи str")
elif type(a) == type(b) !=type(c):
    print("Переважають тип str ")
else: 
    print("Переважно тип int")
