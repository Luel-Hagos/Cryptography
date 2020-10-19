"""
It finds length of a keyword using kasiski
"""

# count frequency occurance with any length 
def frequency(txt, length):
    count = {}
    for i in range(0, len(txt)-length): 
        count.setdefault(txt[i:i+length], 0)
        count[txt[i:i+length]] = count[txt[i:i+length]] + 1
    return sorted(count.items(), key = lambda x : x[1], reverse = True) 

# finds the distance between the occurances
def find_difference(word, message, ln): 
    distance, diff = 0, []
    for i in range(len(message)-ln):
        if message[i:i+ln] == word[0]:
            diff += [i-distance]
            distance = i
    return diff[1:]

def allDivisors(lst): # finds divisors
    divisors = {}
    for i in lst:
        for j in range(3, 21):
            if i % j == 0:
                divisors.setdefault(j, 0)
                divisors[j] = divisors[j] + 1
    return sorted(divisors.items(), key = lambda x : x[1], reverse = True)[0][0]
    

def findKeyLen(cipher):
    difference = []
    for j in range(3, 7):
        word_count = frequency(cipher, j)
        word_collection = [i for i in word_count if i[1]>=2]
        for word in word_collection:
            difference += find_difference(word, cipher, j)
    dif = list(set(difference))
    key_length = allDivisors(dif)
    return key_length
