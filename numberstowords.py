# Challenge
# The code should take in a number and respond with the word description for what that number is.

# Example
# Enter a number:
# 123
# One hundred and twenty-three


#done through the use of modules - num2words and inflect
#refer to docs if necessary for modules

#num2words

# from num2words import num2words

# x = int(input("Type in your number to be printed as a word: "))
# print(num2words(x))


# #inflect

# import inflect 

# inflect = inflect.engine()

# y = int(input("Type in your number to be printed as a word: "))
# print(inflect.number_to_words(y))


#Using someone else's module is too easy, creating my own function:

# Steps:
# 1. researching into numbers and how they translate into words 

# 1-10 one two three ten etc
# 100 one hundred two hundred three hundred four hundred nine hundred 
# 150 one hundred and fifty   one hundred and sixty       one hundred and ninety 
# 199     one hundred and ninety nine         one hundred and ninety six      one hundred and ninety two 
# 1000        one thousand three thousand        four thousand 
# 1050        one thousand and fifty      one thousand and seventy            one thousand and ninety 
# 1250        one thousand two hundred and fifty 
# 10000       ten thousand        twenty thousand         ninety thousand     ninety nine thousand and nine hundred and ninety nine 
# 12500       twelve thousand and five hundred        twelve thousand and seven hundred 
# 12399       twelve thousand and three hundred and ninety nine
# 123000      one hundred and twenty three thousand
# 1230000     one million and two hundred and thirty thousand 

# 0 = absence of pronouncing number (refer to leftmost until reaching digit)
# number of digits after a number = dictates whether its a one, hundred, thousand, ten thousand million etc 
# (exception) - if referring above ten thousand up to million then use up to a thousand 
# if referring up to a billion it goes up to a thousand million as well 
# if referring up to a trillion it goes up to a thousand billion as well
# etc etc etc quadrillion quintillion nonillion decillion

# up to ten probably have literal values mapped 
# anything else have a set word for each place value e.g. hundred thousand etc 

# 2. form dictionary for base 10 
# 3. form dictionary for tens/hundreds/thousands etc 
# 4. mapping numbers and length to dictionary 
# 5. output 


pronouncables = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',
12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty',
30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}

placevalues = {1:'ten', 2:'hundred', 3:'thousand', 4:'ten thousand', 5:'hundred thousand', 6:'million', 9:'billion',
12:'trillion', 15:'quadrillion', 18:'quintillion', 21:'nonillion', 24:'decillion'}

# def parsenumber(number):
#     words = ''
#     charsleft = 0
#     strnumber = str(number)

#     if number in pronouncables:
#         return pronouncables[number]
#     elif len(strnumber) == 2:
#         return pronouncables[int(strnumber[0]+'0')] + pronouncables[int(strnumber[1])]
#     elif len(strnumber) == 3:
#         for i in range(len(strnumber)):
#             charsleft = len(strnumber[i:])
#             words = words + pronouncables[number[0]] + placevalues[charsleft]
#             if strnumber[1:] 


# def parsenumber(number):

#     strnumber = str(number)

#     if number in pronouncables:
#         return pronouncables[number]
    
#     if number > 20 and number < 100:
#         return pronouncables[int(strnumber[0]+'0')] + pronouncables[strnumber[1]]

# z = parsenumber(81)
# print(z)

#iterate through number 984:
#find out how long, judge number of chars from first index
#keep on finding out how long to judge word positioning 
#if the length of chars left is 2 or under 2, resort to finding out last 2 columns

words = ''
for i in range(len(str(984))):
    currentindex = i
    currentchar = str(984)[i]
    charsleft = len(str(984)[i:-1])
    print(currentindex, currentchar, charsleft)

    if charsleft != 1 or charsleft != 2:
        
        # error checking if first integer is a 0 
        if str(984)[0] == 0:
            print("error")
        
        #judging whether first word is a one/ten/hundred 
        #100 900 500 one hundred nine hundred five hundred (2)
        #120 000 one hundred and twenty thousand (5)
        #1 120 000  one million one hundred and twenty thousand (6)
        #10 000 000 ten milli (7)
        #100 000 000 hundred milli (8)

        if charsleft % 3 == 2:
            print("This is a hundred pronouncable")
            print(pronouncables[int(currentchar)])
            words = words + pronouncables[int(currentchar)] + placevalues[charsleft % 3]
        
        if charsleft % 3 == 1:
            print("This is a ten pronouncable")
            print(currentchar)
            
            if 


        if charsleft % 3 == 0: 
            print("This is a one pronouncable")
            print(currentchar)


        #getting place value 
print(words)