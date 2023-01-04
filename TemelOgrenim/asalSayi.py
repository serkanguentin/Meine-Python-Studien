sayi=int(input("sayi griniz: "))

asalMi=True
for x in range(2,sayi):
    if (sayi%x==0):
        asalMi=False
        break
if asalMi:
    print("asal sayidir..")   
else:
    print("asal degildir.. ")