def p1(strs):
    
    common = ''
    
    smallest_word_len = sys.maxsize
    
    for word in strs:
        smallest_word_len = min(len(word), smallest_word_len)
    
    for i in range(smallest_word_len):
        first_word = strs[0]
        letter = first_word[i]
        
        for word in strs:
            if word[i] != letter:
                return first_word[:i]
        
        common += letter
    
    return common
