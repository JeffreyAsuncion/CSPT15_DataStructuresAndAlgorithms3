# https://www.youtube.com/watch?v=cHNnP2j3M6o


def csWordPattern(pattern, a):
    # word key - letter value
    d = {}
    d2 = {}
    
    words = a.split()
    
    if len(words) != len(pattern):
        return False
        
    i = 0
    while i < len(words):
        if words[i] not in d and pattern[i] not in d2:
            d[words[i]] = pattern[i]
            d2[pattern[i]] = True
        elif d.get(words[i]) != pattern[i]:
            return False
        i += 1
    return True



pattern = "abba"
a = "lambda school school coding"

print(csWordPattern(pattern, a))