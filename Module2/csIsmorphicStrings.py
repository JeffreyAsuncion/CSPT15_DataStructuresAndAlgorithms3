
# https://www.youtube.com/watch?v=CKHBA1m13y8
def csIsomorphicStrings(a, b):
    if len(a) != len(b):
        return False
    
    a_list = [0 for _ in range(128)]
    b_list = [0 for _ in range(128)]
    
    for i in range(0, len(a)):
        a_idx = ord(a[i]);
        b_idx = ord(b[i]);
        
        if a_list[a_idx] != b_list[b_idx]:
            return False
            
            a_list[a_idx] = i+1
            b_list[b_idx] = i+1
    
    return True
