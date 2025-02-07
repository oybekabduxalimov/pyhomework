def insert_underscores(txt):
    vowels = "AEIOUaeiou"
    result = []
    count = 0
    
    for i, char in enumerate(txt):
        result.append(char)
        count += 1
        # Insert underscore after every 3rd non-vowel character
        if count == 3 and i < len(txt) - 1:
            if char not in vowels and txt[i + 1] != "_":
                result.append("_")
            count = 0
    
    return "".join(result)