sen = input("Words: ").split()
con = []
for i in sen:
  if i[0] in 'aeiou':
    con.append(i)
con.sort()
print(" ".join(con))
