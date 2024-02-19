import random

# RSA Algorithm
print("RSA Algorithm")


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def generate_prime(a, b):
    while True:
        x = random.randint(a, b)
        if is_prime(x):
            return x


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    de, x, y = gcd_extended(b, a % b)
    return de, y, x - a // b * y


def mod_inverse(a, num):
    de, x, _ = gcd_extended(a, num)
    if de == 1:
        return x % num
    else:
        return None


def encrypt(msg, enk, num):
    return (msg ** enk) % num


def decrypt(c, dek):
    return (c ** dek) % n


p = generate_prime(100, 999)
q = generate_prime(100, 999)
n = p*q
phi_n = (p-1)*(q-1)
while True:
    e = random.randint(1, phi_n)
    if gcd(e, phi_n) == 1:
        break
m = 10

d = mod_inverse(e, phi_n)

Cipher = encrypt(m, e, n)
Decrypted_Text = decrypt(Cipher, d)

print("Values taken:")
print(f"p: {p}")
print(f"q: {q}")
print(f"n: {n}")
print(f"phi_n: {phi_n}")
print(f"Plain Text: {m}")
print(f"Cipher text: {Cipher}")
print(f"Decrypted text: {Decrypted_Text}")


# Diffie-Helman Algorithm
print("\nDiffie-Helman Algorithm")


def generate_private_key(lim):
    return random.randint(1, lim - 1)


def generate_public_key(gen, privkey, lim):
    return pow(gen, privkey, lim)


if e >  d:
    privno = e
else:
    privno = d

g = 5  # generator any no. from 1 to p-1

alprivkey = generate_private_key(privno)
alpubkey = generate_public_key(g, alprivkey, privno)
bobprivkey = generate_private_key(privno)
bobpubkey = generate_public_key(g, bobprivkey, privno)

alreckey = bobpubkey
bobreckey = alpubkey

alshrkey = pow(alreckey, alprivkey, privno)
bobshrkey = pow(bobreckey, bobprivkey, privno)

msg = 12

encrypted = msg*alshrkey
decrypted = encrypted/bobshrkey

print(f"Generator: {g}")
print(f"Alice's Private Key, a: {alprivkey}")
print(f"Bob's Private Key, b: {bobprivkey}")
print(f"g^a: {alpubkey}")
print(f"g^b: {bobpubkey}")
print(f"Alice sends to Bob, g^a: {bobreckey}")
print(f"Bob sends to Alice, g^b: {alreckey}")
print(f"Alice and Bob both calculate, g^ab: {alshrkey}")
print(f"Plain Text:  {msg}")
print(f"Encrypted (by Alice and sent to Bob): {encrypted}")
print(f"Decrypted (by Bob when received from Alice): {int(decrypted)}")

