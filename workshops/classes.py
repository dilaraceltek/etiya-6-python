#classlar-sınıflar
 # class:fonksiyon, değişken ve değerleri içeisinde tutabilen nesnelerdir.
  #self : this >>> bir parametre alınması gerektiği için bu keyword ekledik.
class human: 
    #def talk(self):
        #print("Human is talking..")
    # def talk(self,sentence):
    #     print(f"Human: {sentence}")
    name = "Dilara"
    #buil-in 
    #constructor
    #initialize
    def __init__(self, name):
        self.name = name
        print("Bir human instance'i üretildi.")
    def __str__(self):
        return f"str fonk. dönen değer: {self.name}"

    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

#instance:örnek

human1 = human("Nil")  # eğer ki bu şekilde kullanılırsa içerisine parametre atanması gerekmektedir. 
#human1.name="Ayşe"     # yoksa kod hata verecektir.
#human1.talk()
human1.walk()
human1.talk("Merhaba")
print(human1)

human2 =human("Zeynep")
#human2.name = "Dilara"
human2.talk("Merhaba")
human2.walk()
print(human2)

