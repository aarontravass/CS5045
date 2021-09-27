from random import randint

dna = "ACTG"


def isDNA(s):
    a = s.count('A')
    c = s.count('C')
    g = s.count('G')
    t = s.count('T')
    if a == 0 or c == 0 or g == 0 or t == 0:
        return False
    return (a + c + t + g) == len(s)


def mutate(s):
    s_pos = randint(0, len(s) - 1)
    dna_pos = randint(0, len(dna) - 1)
    return s[:s_pos]+dna[dna_pos]+s[s_pos+1:]


s = input("Enter a DNA sequence ")
s = s.upper()
assert isDNA(s), "Not a DNA sequence"
print("DNA string before mutation is ", s)
print("DNA string after mutation is ", mutate(s))
