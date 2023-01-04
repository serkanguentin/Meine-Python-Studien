# class Mathe:
#     def topla(self,sayi1,sayi2):
#         return sayi1 + sayi2
    
#     def cikar(self,sayi1,sayi2):
#         return sayi1 - sayi2
    
#     def carp(self,sayi1,sayi2):
#         return sayi1 * sayi2
    
#     def bol(self,sayi1,sayi2):
#         return sayi1 / sayi2
 
# mat=Mathe()

# print(mat.topla(1,2))    


class Mathe:
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
        
    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
 
mat=Mathe(1,2)

print(mat.topla())    


class Person:
    def __init__(self,firstName,LastName,age):
        self.firstName =firstName
        self.LastName=LastName
        self.age=age
        
        
person1=Person("Serkan", "guntin", "32")
print(person1)

class Worker(Person):
    def __init__(self,salary):
        self.salary=salary
        
class Customer(Person):
    def __init__(self,crediKartnumber):
        self.crediKartnumber=crediKartnumber

ahmet=Worker()

mehmet=Customer()
  
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



