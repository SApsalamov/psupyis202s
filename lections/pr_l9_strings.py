s = "Alea jacta est"
print(s)
print("First simbol ",s[0])
print("Last simbol ",s[-1])
print("Third simbol ",s[2])
print("Third from last simbol ",s[-3])
print("Length of string ", len(s))

s2 = "Lorem ipsum dolor sit amet,consectetur adipisicing elit."
print(s2)
print(len(s2))
print(s2[:8], " = ",len(s2[:8]))
s2center = int(len(s2)/2)
print("s2center = ", s2center, " center simb = ", s2[s2center])
print(s2[(s2center - 2):-(s2center-2)])
print("sumbols per 3 = ", s2[::3])
