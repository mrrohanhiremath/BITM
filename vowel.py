word="wonderful"
vowels="aeiou"
result=[char for char in word if char  not in vowels]
print(result)
print(word[::-3])
sep='-'.join(word[::2])
print(sep)
for i in range(0,len(word)):
    if(i%3==0 and i!=0):
        print('-',end=' ')
    else:
        print(word[i],end='')
    
