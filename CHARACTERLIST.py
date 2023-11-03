sen = input("Character: ")
con = []
count = 0
counts = 0
while sen != '':
  if sen not in con:
    count = count + 1
  con.append(sen)
  sen = input("Character: ")
  if sen in con:
    counts = counts + 1
print(f"You named {count} character (s)")
print(f"You repeated {counts} time (s)")
