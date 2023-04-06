#Döngüler,birbirine benzeyen işleri tekrar ettirmek için kullanılır.

krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan Alanlara Özel", "Mutlu Emekli İhtiyaç Kredisi"] 

for kredi in krediler:      #alias 
    print(kredi)


for i in range(10):
    print(i)

for i in range(len(krediler)):
    print(krediler[i])

for i in range(3,10):  # 3'den 10'a kadar yazdırır.
    print(i)

for i in range (0,10,2): #ikişer ikişer yazdırır.
    print(i)

