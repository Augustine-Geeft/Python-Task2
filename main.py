# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from os import read


def read_file_content(Story):
    # [assignment] Add your code here 
    with open('story.txt') as file:
        read_file_contents = file.read()        
    return read_file_contents


def count_words():
    Story = read_file_content("story.txt")
    # [assignment] Add your code here
    Story = Story.split()
    count = {}
    for words in Story:
        if words in count:
            count[words] += 1
        else: 
            count[words] = 1
    return count
    # return {"as": 10, "would": 20}

print(count_words())
