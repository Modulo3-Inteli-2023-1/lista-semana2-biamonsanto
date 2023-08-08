from collections import Counter
def is_anagram(w1, w2):
    if Counter(w1) == Counter(w2):
        return True
    else:
        return False
