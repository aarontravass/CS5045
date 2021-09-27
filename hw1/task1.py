protien_seq = "ACDEFGHIKLMNPQRSTVWY"

def proteinCheck(s):
    for pr in protien_seq:
        if s.count(pr) <= 0:
            print("Not a protein sequence")
            return False
    print("This is a protein sequence")
    return True


def aminoAcidCalc(s):
    if not proteinCheck(s):
        return
    print("Percentage of Acidic Amino acids is "+str((s.count('D')+s.count('E'))/len(s)))
    return

aminoAcidCalc(input("Input a sequence - "))