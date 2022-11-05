a = int(input("Bilangan Ke-1 : "))
b = int(input("Bilangan Ke-2 : "))
c = int(input("Bilangan Ke-3 : "))

if a<b and a<c :
    if b<c :
        print(a, b, c)
    else :
        print(a, c, b)  
elif b<a and b<c :
    if a<c :
        print(b, a, c)
    else :
        print(b, c, a)
else :
    if a<b :
        print(c, b, a)
    else :
        print(c, a, b)