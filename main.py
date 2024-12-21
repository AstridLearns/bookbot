def copy():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return(file_contents)

def count(s):
    words = s.split()
    return(len(words))

def char_count(string):
    lowered = string.lower()
    char_dict = {"letter":"number"}
    
    for lower in lowered:
        if lower == ' ' or lower == "'" or lower == ',' or lower == '(' or lower ==')' or lower == '\n' or lower == '.' or lower == '-' or lower == ':' or lower == '1' or lower == '7' or lower == '2' or lower == '0' or lower == '8' or lower == '[' or lower == '#' or lower == '4' or lower == ']' or lower == '*' or lower == '?' or lower == ';' or lower == '!' or lower == '"' or lower == '3' or lower == '5' or lower == '9'  or lower == '6'  or lower == '_' or lower == '/' or lower == '%' or lower == '@' or lower =='$':
            # to ignore numbers and other special chars
            continue
        elif lower in char_dict:
             char_dict[lower]+=1
        else:
            char_dict[lower] = 1
    return (char_dict)    

def list_iterations(dict):
    alphabet= list(dict.keys()) #creating an alphabet
    alphabet.sort()
    ordered = {i:dict[i] for i in alphabet} #creating a new dictionary with the letters sorted
    return (ordered)
    

def main():
    dico = {}
    text = copy()
    number = count(text)
    dico = char_count(text)
    print(f"Report", f"{number} words found in the document")
    ordered= {"a":"b"}
    ordered= list_iterations(dico)
    for a in ordered:
        print(f"{a} found {ordered[a]} times in the document")

main()
