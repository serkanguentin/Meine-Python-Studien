#substring
yeniMesaj="serkangintn"
print(yeniMesaj[:9]);
bilgi="serkangintn"
print(len(bilgi))
yeni =bilgi[3:len(bilgi)-1]  #3.karakterden son karakter karaktere kadar yazdir
print(yeni)

#lower upper
okul="liborsscule"
print(okul.upper())
print(okul.lower())

print(okul.replace("o", "ö"))
print(okul.replace("o", "ö"))
print(okul.replace("o", "ö"))
print(okul)  #son hamlede yine aynisi oldu cünkü fonksiyonu deistirmedik
okul2=okul.replace("s","x")
print(okul2)
print(okul2)
print(okul2)
#split bölmek
bilgi ="serkan guntn mamet"
print(bilgi.split()) #print(bilgi.split("e")) yazdigimzda e ler den sonra böler


#input  veri almak icn 
ad=input("adinizi giriniz:")
print(ad)






