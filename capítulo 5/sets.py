s1 = {1,2,3,4,5}

print(s1)
print(type(s1))

s2 = set([4,5,6,7,8])

print(s2)

u = s1.union(s2)

print(u)

#Sets tiram itens duplicados de um banco de dados, ele verifica os dados em comum no conjunto

i = s1.intersection(s2)

print(i)

s1.add('item novo')

print(s1)

d = s1.difference(s2)

print(d)

