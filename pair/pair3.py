#Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından en büyük olanı kullanıcıya gösterelim.

liste=[]

for x in range(10):
    sayi=float(input("Lütfen sayı giriniz: "))
    liste.append(sayi)
print(max(liste))




