"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']
# i think this will print all the words in the brackets
for word in some_words:
    print(word) # it printed all the words
# I dont think it will print anything?
for x in some_words:
    print(x) #it repeated the words in the list
# I think it will re print the list
print(some_words) #it reprinted the list

if len(some_words) > 3: #I think it will print 'some_words contains more than 3 words'
    print('some_words contains more than 3 words') #It printed the statement 

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
