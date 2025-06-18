import string

def count_words(text):
    
    words = text.lower().split()
    
    
    cleaned_words = [word.strip(string.punctuation) for word in words]
    
    word_count = {}
    for word in cleaned_words:
        if word:  
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    return word_count

sentence = input("Enter a sentence: ")
result = count_words(sentence)
print(result)
