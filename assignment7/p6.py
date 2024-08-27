def replace_words(text, word_dict):
    words = text.split()
    for i in range(len(words)):
        if words[i] in word_dict:
            words[i] = word_dict[words[i]]
    return ' '.join(words)

# Example usage
text = "Hello world"
word_dict = {"Hello": "Hi", "world": "earth"}
print(replace_words(text, word_dict))
