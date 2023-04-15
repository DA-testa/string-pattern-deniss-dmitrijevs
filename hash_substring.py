# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    in_type = input()

    if "i" in in_type.lower():
        pattern = input()
        text = input()
    elif "f" in in_type.lower():
        file_name = '06'
        path = "tests/" + file_name
        with open(path, 'r') as file:
            pattern = file.readline()
            text = file.readline()


    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    instance_indices = []
    pattern_length = len(pattern)
    pattern_hash = get_text_hash(pattern)
    # and return an iterable variable
    for i in range(0, len(text)):
        if get_text_hash(text[i:i + pattern_length]) == pattern_hash:
            if text[i:i + pattern_length] == pattern:
                instance_indices.append(i)
    return instance_indices

def get_text_hash(text: str) -> int:
    multiplier = 23
    modulo = 137
    hash = 0
    for char in text:
        hash = (hash * multiplier + ord(char)) % modulo
    return hash

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

