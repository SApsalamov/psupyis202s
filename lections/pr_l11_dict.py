school = {'1a':14,'1b':20, '2a':19, '2b':15}
print(school)
print(school['1a'])
print(school['2b'])
school['1b'] = 15
school['1a'] = 19
school['2b'] = 20
school['3a'] = 12
school['3b'] = 15
del(school['2a'])
print(school)