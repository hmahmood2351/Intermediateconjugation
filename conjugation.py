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
import reprlib

URL = 'http://www-personal.umich.edu/~jlawler/wordlist'
page = requests.get(URL)
splittedpagetext = page.text.split()






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