# -*- coding: utf-8 -*-

studentSet={"engin","ali","ahmet","cemla"}
print(studentSet)
for student in studentSet:
    print(student)
    print("\n")
print("\n ")
print("ahmet" in studentSet)    
print("\n bosluk biraktim")
print("\n")

if"ahmet" in studentSet:
    print("listede var")

studentSet.add("seymaaa")
print("\n")
print("\n")
print(studentSet)
print("\n")
print("\n")
studentSet.update(["leyla","antepli ","suvaslu"])
print(studentSet)

studentSet.remove("leyla")#leylayi sildik
print(studentSet)