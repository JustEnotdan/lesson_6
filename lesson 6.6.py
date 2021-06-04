a = open("bakery.csv", "w+", encoding="utf-8")
a.write("5978,5\n8914,3\n7879,1\n1573,7")
num = input("Введите число(если их несколько, записывайте через пробел):   ")
a.seek(0)
if num == "":
    b = a.readlines()
    for i in b:
        print(i.replace("\n", ""))
elif len(num.split()) == 1:
    b = a.readlines()[int(num)-1:]
    for i in b:
        print(i.replace("\n", ""))
elif len(num.split()) == 2:
    b = a.readlines()[int(num.split()[0]) - 1: int(num.split()[1])]
    for i in b:
        print(i.replace("\n", ""))
