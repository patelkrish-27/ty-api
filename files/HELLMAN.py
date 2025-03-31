import random 

n = 101
g = 179

x =  random.randint(1,100)
y =  random.randint(1,100)

print("x:",x)
print("y:",y)

def calc(base, exp, mod):
    return (base**exp) % mod

A = calc(g, x, n)
B = calc(g, y, n)
print("A:", A)
print("B:", B)

ak = calc(B, x, n)
bk = calc(A, y, n)

print("ak:", ak)
print("bk:", bk)

print("key exchanged successfully" if ak == bk else "key exchange failed")