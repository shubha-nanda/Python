d={100:"durga",200:"ravi",300:"shiva"}

print(d.get(100))
print(d.get(300,"abcd"))
print(d.get(400,"shiva"))
print(d)
print((d.items()))