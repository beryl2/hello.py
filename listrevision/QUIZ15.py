#Python function to create the HTML string with tags around the word                       
def add_tags(tag, word):
    return '<%s>%s</%s>' %(tag, word, tag)
print(add_tags('i', 'html'))  
print(add_tags('b','python tutorial')) 