#diziler-listeler

sayilar = [100,200,300,400,500, "merhaba"]   #listedeki veri tipinin uyumlu olmasına gerek yoktur.
#programcı 0'dan saymaya başlar. yani ilk bşlangıç değeri 0. olarak geçer. index = 0
print(sayilar[1])

print(sayilar)
sayilar.append(100)
sayilar.append(600)        #append, listenin sonuna eleman ekler.

print(sayilar)

sayilar.pop(0)             #pop, index-parametre verilmediği durumda son indexi siler.
print(sayilar)             #indexe göre çalışır.

sayilar.remove(100)        #listedeki değere göre çalışır. birden fazla aynı değere sahip veri varsa ilk değer silinir.
print(sayilar)

sayilar.extend([700,800,900])           #extend, iki listeyi birleştirir.
print(sayilar)                         #apend aksine tek bir değer eklemez.
sayilarEkleme= [10,40,90]
sayilar.extend(sayilarEkleme)
print(sayilar)

sayilar.clear()              #dizinin içini boşaltır, siler.
print(sayilar)

#**************************
#string interpolation
hello = "Merhaba"
userName = "Dilara"
totalText = hello+ " " +userName
print(hello+ " " +userName)
print(totalText)

totalText = "{message} Sayın {name}".format(message="Merhaba", name="Dilara")
print(totalText)
totalText = "{message} Sayın {name}".format(message=hello, name=userName)
print(totalText)
# f-string
totalText= f"Hoşgeldiniz {userName}"
print(totalText)   #metni birleştirmeyi işe yarıyor.

#************************

#karar yapıları
ortalamaNot = input("Lütfen ortalamanızı giriniz: ")
ortalamaNotAsInteger = int(ortalamaNot)

#input str yapıda veri saklar. sayı gireceksek int, double, float dönüştürmeliyiz.

#if-else blokları
if ortalamaNotAsInteger > 80:
    print("Bravo.")
    
elif ortalamaNotAsInteger > 60:
    print("Ortalama.")
elif ortalamaNotAsInteger > 50:
    print("Normal.")
       
else:
    print("Maalesef.")
    print("Kaldınız.")



