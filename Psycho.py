import nltk


f=open('psycho2.txt','r')
raw=f.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

search = str(input('Enter a word to go psycho:\n'))
print('\n')

print('#'*84)
print('#' + ' '*82 + '#')


text.concordance(search,80, 2314)


print('#' + ' '*82 + '#')
print('#'*84)

print('\nMy punishment continues to elude me... and I gain no deeper knowledge of myself. \nNo new knowledge can be extracted from my telling. \nThis confession has meant... nothing. ')