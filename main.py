import sys
from stats import get_num_words, char_count, char_by_appearances

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents= f.read()
    return(file_contents)

def main():
    arguments = sys.argv  # List of arguments   
    script_name = sys.argv[0]  # Name of the script   
    # Checking if an argument is provided before accessing it   
    if len(sys.argv) != 2:   
       print(f"Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    else:   
        bookpath = sys.argv[1] 
    bookstring = get_book_text(bookpath)
    chardict = char_count(bookstring)
    appearances = char_by_appearances(chardict)
    i=0


    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}..."+"\n"+"----------- Word Count ----------")
    print(f"Found {get_num_words(bookstring)} total words"+"\n"+"--------- Character Count -------")
    for i in range(0, len(appearances)):
        dicti=appearances[i]

        print(f"{dicti["String"]}: {dicti["Integer"]}")
    print(f"============= END ===============")

""""
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
"""
main()

