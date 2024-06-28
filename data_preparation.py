# prepare config yaml file for training 
import os

with open("dataset/List/Logo-2K+classes.txt") as file:
    class_names = file.read()

class_names = class_names.split("\n")
for index, item in enumerate(class_names):
    class_names[index] = f"{index+1}: {class_names[index]}"
    print(class_names[index])
