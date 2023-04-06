vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzunu giriniz: "))
ortalama = ( vize*0.4) + (final*0.6)
# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

if final <40:
    print("Kaldınız.")
elif ortalama < 50:
    print("Kaldınız.")
elif vize == (final*2):
    print("Kaldınız.")
else:
    print("Geçtiniz.")
    
    
