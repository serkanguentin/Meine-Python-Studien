sayi1=int(input("1.sayiyi giriniz:  "))
sayi2=int(input("2.sayiyi giriniz:  "))
sayi3=int(input("3.sayiyi giriniz:  "))

if (sayi1>=sayi2) and (sayi1>=sayi3):
       EnBuyuk=sayi1
elif (sayi2>=sayi2) and (sayi2>=sayi3):
        EnBuyuk=sayi2
else:
    EnBuyuk=sayi3
print("en buyuk sayi:",EnBuyuk)
