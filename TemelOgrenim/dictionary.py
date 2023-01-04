

sozluk = {
    "book":"kitap", "table":"masa"
    }

print(sozluk)

print("\n")

print(sozluk ["book"]) #aradiimigz elemani bulurz

print("\n")

#yeni bir eleman  eklmek


sozluk["pencil"]="kalem"
print(sozluk)

sozluk2 =dict(kitap="book", masa="table")
print(sozluk2)
del(sozluk["book"])
print(sozluk)