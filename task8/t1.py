surname = input("Enter surname: ")
name = input("Enter name: ")
middle_name = input("Enter middle_name: ")

if len(surname) > len(name) and len(surname) > len(middle_name):
    print("Surname is longest")
elif len(name) > len(middle_name) and len(name) > len(surname):
    print("Name is longest")
elif len(middle_name) > len(name) and len(middle_name) > len(surname):
    print("Middle name is longest")
else:
    print("Text the same")