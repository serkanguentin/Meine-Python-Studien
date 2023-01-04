sayi=int(input("bir sayi giriniz"))
faktoriyel=1
if sayi<0:
    print("negatif sayilarin fakrteli hesablanamaz")
elif sayi==0:
    print("sonucc:1")
else:
    for i in range(1,sayi+1):
        faktoriyel=faktoriyel*i
    print(faktoriyel)
    