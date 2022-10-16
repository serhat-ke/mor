print("chatbot")

selamlama =["selam","merhaba","hello"]
nasılsın=("nasılsın","nasıl gidiyor")
isim = ("ismin ne","adın ne")
list_1 = ("hastayım","hasta gibiyim","kendimi iyi hissetmiyorum")

while True:    
    
    soru = input("you:")

    for i in selamlama:
        if soru == i:  
            print(i)
            
    for i in nasılsın:
        if soru == i:
            print("iyiyim siz nasılsınız")
            
    for i in isim:
        if soru == i:
            print("ben adım elina,sağlık botuyum")
    
    for i in list_1:
        if soru == i:
            print("size yardımcı olmayı çok isterim.Şikayetiniz nedir")
    
    if soru == "q":
        break

        
        
