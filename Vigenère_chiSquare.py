"""
finds the key word of the cipher text with a known key word length.
uses chi-square to select the sub-key
"""

# counts the frequancy of a letter
def frequancy(msg, ltr):
    count = 0
    for i in msg:
        if i == ltr:
            count += 1
    return count

# finds the total chi-square of a given message by encrypting using sub-key A-Z
def chiSquare(msg):
    probablity = {'A': 0.0815, 'B': 0.0144, 'C' : 2.76/100, 'D':3.79/100, 'E':13.11/100, 'F':2.92/100, 'G':1.99/100, 
     'H':5.26/100, 'I':6.35/100, 'J':0.13/100, 'K':0.42/100, 'L':3.39/100,'M':2.54/100, 'N':7.10/100, 'O':8.00/100, 
      'P':1.98/100, 'Q':0.12/100, 'R':6.83/100, 'S':6.10/100, 'T':10.47/100,'U':2.46/100, 'V':0.92/100, 
      'W':1.54/100, 'X':0.17/100, 'Y':1.98/100, 'Z':0.08/100}
    chi_total = 0
    chi_sqr = 0
    count = 0
    for i in msg:
        count = frequancy(msg, i)
        chi_sqr = (count - len(msg)*probablity[i])**2/(len(msg)*probablity[i])
        chi_total += chi_sqr
    return chi_total

# find key
def findKey(cipher):
    db = {'A': 0, 'B': 1, 'C' : 2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11,'M':12, 'N':13, 'O':14, 
      'P':15, 'Q':16, 'R':17, 'S':18, 'T':19,'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
    ky = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plntxt = ''
    key, f = 0, 10000000000000
    for j in ky:
        for i in cipher:
            plntxt += ky[(db[i]-db[j]) % 26]
        s = chiSquare(plntxt)
        if f>s:
            f = s
            key = j
        plntxt = ''
    return key

# split the cipher into columns of length equal with key word length
def splitItky(cipher, key_len):
    cipher = [cipher[i:i+key_len] for i in range(0, len(cipher)-key_len, key_len)]
    st, ky = '', ''
    for i in range(key_len):
        for j in cipher:
            st += j[i]
        ky += findKey(st)
        st = ''
    return ky