#fonksiyonlar

def ortalamaHesapla():
    final = 60
    vize = 100
    ortalama = (vize*0.4) + (final*0.6)
    print(ortalama)
def ortalamaHesaplaveDondur(vize:float ,final:float) -> float:
    # final = 60
    # vize = 100
    #ortalama = (vize*0.4) + (final*0.6)
    #expression >> geriye dönmek
    #return ortalama
    return (vize*0.4) + (final*0.6)

#triggerlamak, çalıştırmak, execute etmek >>> fonk. çağırmak anlamaına gelir.

ortalamaHesapla()
benimOrtlamam = ortalamaHesapla()

#benimOrtlamam2 = ortalamaHesaplaveDondur()


print(benimOrtlamam) #>>>> none değeri verir.
#print(benimOrtlamam2) #>>> return kullandığımız için fonk. içinde elinde tuttuğu son değeri yazar.
#yukarıdaki yazım şekli yerine şu şekilde de yazılabilir;
print(ortalamaHesaplaveDondur(100,60))



