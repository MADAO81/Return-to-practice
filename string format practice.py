name = 'Vasya'
surname = 'Pupkin'
age = 32

text = "My name is " + name + " " + surname + " and I'm " + str(age) + " years old."
text_1 = "My name is %s %s and I'm %s years old." % (name, surname, age) # Old style format
text_2 = "My name is {1} {0} and I'm {2} years old.".format(name, surname, age)
text_3 = f"My name is {name} {surname} and I'm {age} years old."

print(text)
print(text_1)
print(text_2)