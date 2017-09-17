f = open('myfile.txt', 'r')
text = f.read()
f.close()
print(text)

fw = open('myfile.txt', 'w')
fw.write('Hellow')
fw.close()

# Использование менеджера контекста
# который в любом случае закроет файл
with open('myfile.txt', 'a') as f:
	f.write("Yo!")