
p = int(input("Enter the P"))
q = int(input("Enter the q"))
e = int(input("Enter the e"))

pt = int(input("Ente the input:"))

n = p*q

phi  = (p-1)*(q-1)

j = 0
d = int((1+j * phi)/e)
d1 = (1+j * phi)/e

while d1!=d:
    d = int((1+j * phi)/e)
    d1 = (1+j * phi)/e
    j = j+1

print(d)
ct = (pt**e) % n
print("cipher text:",ct)
pt = (ct**d)%n
print("plain text:",pt)
