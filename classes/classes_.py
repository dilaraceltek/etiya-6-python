#class, nesne, obje, sınıf

class human:
    #property,attribute >> özellik

    name = ""
    age = 20
#içinde bulunduğumuz claas ın içindeki keyword ü işaret eder >>> self
#nesenlere, özellik-davranış gibi veriler atarız.
    def __init__(self,name,age):
        self.name =name
        self.age = age
        print("Yapıcı blok çalıştı")
    def talk(self,message):
        print(f"{self.name} : {message}")
    def walk(self):
        print(f"{self.name} is walking..")


#instance >> örnek üretmek
human1 =human("Dilara", 23) #constructor >> yapıcı blok
#human1.name = "Dilara"
#human1.age = "23"
human1.talk("Selam")
human1.walk()

