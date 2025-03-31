pt = input("Enter the plain text")
row1 = row2 = ""

for i in range(len(pt)):
    if i % 2 == 0:
        row1 = row1 + pt[i]
    else:
        row2 = row2 + pt[i]
print("Cipher text is:", row1 + row2)