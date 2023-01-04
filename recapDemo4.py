ogrenciler=["serkan","ismail","amine","melike"]
fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
fileToAppend.close()    