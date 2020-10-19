"""
It finds length of a keyword using Index of Coincidence.
Note: the cipher should be large enough.
"""

def frequencyCount(txt): # count frequency occurance
    freq = {}
    for letter in txt: 
        if letter in freq: freq[letter] += 1
        else: freq[letter] = 1
    return freq

def keyLen(cipher):
    freq_sum, n = 0, len(cipher)
    frequency = frequencyCount(cipher)
    msg = set(cipher)
    for ltr in msg:
        freq_sum += frequency[ltr]*(frequency[ltr] -1)
    ic = freq_sum/(n*(n-1))  # finds incidence of concidence
    key_length = round((0.027*n)/(ic*(n-1) - 0.038*n + 0.0645))  # finds length of key
    return key_length