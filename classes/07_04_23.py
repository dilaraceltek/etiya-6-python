#3.gün workshop çözüm
biggestValue=0
for i in range(10):
    sayi=int(input(f"{i+1}. sayıyı giirniz: "))
    #0'dan başlat 10'dan küçük olana kadar döngüyü çalıştır,
    # döngü her çalıştığında i değeri 1 artırır. {i+1}
    if sayi > biggestValue:
       biggestValue = sayi

print(f"Girdiğiniz sayılar arasında en büyük sayı {sayi}")

#ikinci en büyük sayıyı bulmak için 
sayilar = []
for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayıyı giriniz: ")))
sayilar.sort(reverse=True)
enbuyukN = int(input("Sayılar arasından en büyük kaçıncı elemanı istiyorsunuz: "))
print(sayilar[enbuyukN-1])

# kullanıcın vereceği üst limit ile
# 0dan üst limite kadar olan tüm çift sayıları yazdıralım
#forRange = int(input("Üst limit belirleyiniz: "))
# for i in range(forRange+1):
#     if i % 2 == 0:
#         print(i)
#start => döngü kaç sayısından başlasından
#stop => döngü kaç sayısında son bulsun
#step => döngü kaç kaç artırılsın
#for i in range(0,forRange+1,2):
    #print(i)
## end


## 3. ister => 2. isterdeki alt limit kullanıcı belirlemelidir
forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))
for i in range(forRangeMin, forRangeMax+1):
    if i % 2 == 0:
        print(i)
##end

# döngüler - loops -start

# i=0
# i<10 == True

# iterate etmek, iteration

for i in range(0,10):
    print(i)

ogrenciler = ["Volkan","Süeda","Zühal","Selen","Ümit"]
#length
print(len(ogrenciler))
# 5
# 0, 1, 2, 3, 4

#break => ilgili döngünün o anda kırılmasını (bitirilmesini) sağlar

for i in range(len(ogrenciler)):
    if i==3:
        break
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

#pass => ilgili alanın bodysini boş bırakabilmemize olanak sağlar
for i in range(0,10):
    pass

#continue => iterasyondaki current değeri atla, bir sonraki değer ile devam et
for i in ogrenciler:
    if i=="Volkan":
        continue
    print(f"Öğrenci: {i}")


# while booleanDeger
#infinite loop - sonsuz döngü
# ctrl+c => terminali durduran manual işlem
i = 0
while i < 10:
    i = i + 1
    if i==3:
        break
    print(f"While içerisindeki i değeri: {i}")
    

# döngüler - loops -end

