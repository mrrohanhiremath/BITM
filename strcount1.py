def count_words(string):
    s=string.split()
    s_freq={}
    for s in words:
        if s in word_freq:
            s_freq[word]+=1
        else:
            s_freq[word]=1
    return s_freq
string=str(input('enter string'))
s_frequency=count_word(string)
print(s frequency) 
