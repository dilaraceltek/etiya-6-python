#Liste  [] olan yerde liste var demektir.
krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan Alanlara Özel", "Mutlu Emekli İhtiyaç Kredisi"]  

print(krediler)
print(krediler[0])     #python'da diziler 0'dan başlar. index sayısı
print(krediler[1])
print(krediler[2])
print(len(krediler))   #length liste içinde sayıyı verir.

krediler[0] = "Çabuk Kredi"
print(krediler)

print(krediler[5])    #liste 3 elemanlı olduğu için hata verecektir.
print(krediler[0])
print(krediler[1])


