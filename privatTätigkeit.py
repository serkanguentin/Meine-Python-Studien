# İki vize ve bir final sınavına girilen üniversitede
#  harf notuna vizeler %30 final ise %40 etkilidir.
#  Bu üniversitenin harf ortalamasını hesaplayan kodu yazınız.

vize1=int(input("ilk vizeyi giriniz:\n = "))
vize2=int(input("ikinci vizeyi giriniz:\n = "))
final=int(input("finali giriniz:\n = "))
ortalama =int((vize1*3+vize2*3+final*4)/10)
if ortalama>=90:
    print("harf notunuz: "+"AA")
elif ortalama>=85:
    print("harf notunuz: "+"BA")
elif ortalama >=80:
    print("harf notunuz: "+"BB")
elif ortalama >=75:
    print("harf notunuz: "+"CB")    
elif ortalama >=70:
    print("harf notunuz: "+"CC")
elif ortalama >=65:
    print("harf notunuz: "+"DC")    
elif ortalama >=60:
    print("harf notunuz: "+"DD")
elif ortalama >=50:
    print("harf notunuz: "+"E")  
elif ortalama >=0:
    print("harf notunuz: "+"F")    