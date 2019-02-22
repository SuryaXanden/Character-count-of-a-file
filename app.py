import re

def find_char_count(check_file):
    with open(check_file) as f:
        input_file = f.read()
    
    input_file = [ re.sub(r"(\n)|(\r)|(\t)|(\z)", "", input_file, 0, re.MULTILINE) for i in input_file ]
    return len(input_file)

result = find_char_count('dummy.txt')
# input file is sent to the function which inturn returns the character count
print(result)