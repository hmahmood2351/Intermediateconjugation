# A list of English words can be found here: http://www-personal.umich.edu/~jlawler/wordlist
# Find out how many different words you can make, from smaller valid sub-words

# For example:

# Enter your word:
# Awesomeness
# 3 Subwords:
# Awe, Some, Ness

# Enter your word:
# Something
# 3 Subwords:
# So, Me, Thing

# Enter your word:
# Disproportionate
# 5 Subwords:
# Dis, Pro, Port, Ion, Ate


import requests
import random

URL = 'http://www-personal.umich.edu/~jlawler/wordlist'
page = requests.get(URL)
splittedpagetext = page.text.split()

# received a whole list of words in string format 

# need to take a word, and break it down into characters, that gets bigger
# one by one, not being 1 char in length, until it finds a respective word 
# in the list of words.

# adding that word somewhere else to be used later, and then moving on to the 
# next set of characters left within the word up until the end 

# finishes when the combined set of subwords is equal to the word itself 


# 1. have list with all words inside in string format 
# 2. have word we want to break down 
# 3. iterate through word, finding all combinations available 
# 4. gather subwords and combinations to form word 
# 5. present all combinations and subwords to make the word 
# 6. profit??

# splitted page text is the variable
# ogword = 'hello'
# subwords = []


subwords = []
subwordstext = []
originalword = 'pancake'

for i in splittedpagetext:
    if i in originalword and len(i) > 1 and i != originalword:
        subwords.append(i)

print(subwords)
print("Combination to make the word", originalword, "are:")

# for index, i in enumerate(subwords):
#     subwordstext.append(i)
#     tempcheck = ''.join(subwordstext)
#     correctlengthword = originalword[:len(tempcheck)]
#     correcttofillword = originalword[len(tempcheck):]
#     print(correctlengthword, correcttofillword)
#     if tempcheck != correctlengthword:
#         del(subwordstext[-1])
#     if correcttofillword in subwords:
#         subwordstext.append(correcttofillword)

def figureoutwords():
    for i in subwords:
        subwordstext.append(i)
        tempcheck = ''.join(subwordstext)
        correctlengthword = originalword[:len(tempcheck)]
        correcttofillword = originalword[len(tempcheck):]
        if tempcheck != correctlengthword:
            del(subwordstext[-1])
        if correcttofillword in subwords:
            subwordstext.append(correcttofillword)

while ''.join(subwordstext) != originalword:
    subwordstext = []
    random.shuffle(subwords)
    figureoutwords()

print(subwordstext)


### try out new way of looking into wordslist for words 
### that are in word and printing them out one by one 
### collect them together and then sort through them in a list 
### to find combinations to fit the word we got in the first place 

# take a look at itertools permutations 

########## close one but doesnt work properly

#testlist = ['some', 'thing']

# while subwords != originalword:
#     for i in range(len(word)):
#         temptext += word[i] 
#         print(temptext)
#         if temptext in splittedpagetext and len(temptext)>1:
#             print("word found: ", word[:i+1])
#             subwords += word[:i+1]
#             word = word[len(temptext):]
#             temptext=''
#             break

##################



# def iteratethroughpoint(word, index=0):
#     newtext = ''
#     for i in word[index:]:
#         newtext += i
#     return newtext


# for i in range(len(word)):
#     temptext = temptext + word[i]
#     print(temptext)
#     if temptext in splittedpagetext:
#         maxlist.append(temptext)


# def findlongestbreakdown(word, list):
#     newlisttemp = []
#     for i in range(len(word)):
#         if word[i:] in list and (len(word[i:])) > 1 and word[i:] != word:
#             newlisttemp.append(word[i:])
#     return newlisttemp


# while subwords != word:
#     for i in range(len(word)):
#         temptext = temptext + word[i]
#         if temptext in splittedpagetext and len(temptext) != 1:
#             subwords = subwords + temptext
#             print("broken down word: ", temptext)
#             temptext=''


# def subwords(wordlist, word):
#     splitword = ''
#     subwords = []
#     for i in wordlist:
#         for j in i:
#             splitword = splitword + j
#             print(splitword)
#             if splitword in word and len(splitword) >= 1:
#                 subwords.append(splitword)
#                 splitword = ''
#             else:
#                 continue
#     if len(subwords) == 0:
#         return False 

#     return subwords

# x = subwords(['some', 'lol', 'thing'], 'some')
# print(x)