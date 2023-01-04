x = [[12,7,3],[4 ,5,6],[7 ,8,9]]

y = [[1,2,3],[5 ,5,5],[0,0,0]]

sonuc =[[0,0,0],[0,0,0],[0,0,0]]

# sonuc[0:4][0:4]=x[0:4][0:4]+y[0:4][0:4]:
for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j]=x[i][j]+y[i][j]
print(sonuc)