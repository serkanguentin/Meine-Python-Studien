sayi=int(input("lütfen bir sayi giriniz: \n"))
toplam =0  
for i in range(1,sayi):
    # print(i)
    if sayi%i==0:
        toplam += i
        
if (sayi==toplam):
    print("mükemmel sayidir")   
else:
    print("mükemmel sayi degildir")     
        
        