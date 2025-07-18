def get_num_words(file_contents):
    words = file_contents.split()
    return(len(words))

def char_count(file_contents):
    lowered = file_contents.lower()
    char_dict = {}
    
    for lower in lowered:
        if lower.isalpha():
            if lower in char_dict:
                char_dict[lower]+=1
            else:
                char_dict[lower] = 1
        else:
            continue
    return (char_dict)

def char_by_appearances(char_dict):
    def sort_on(items):
        return items["Integer"]
    alphabet = []
    for key in char_dict:
        alphabet.append({"String": key, "Integer": char_dict[key]})
    alphabet.sort(reverse=True, key=sort_on)
    return (alphabet)
    
    