pt = input("Enter the plaintext: ")
key = int(input("Enter the key value: "))

cp = ""
for char in pt:
   cp = cp + chr(ord(char) + key)

print("Ciphertext:", cp)

pt = ""

for char in cp:
   pt = pt + chr(ord(char) - key)

print("Plain Text:", pt)