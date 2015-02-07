import sklearn
import string

def countCaps(message):
    #returns percentage of capital letters in a string message
    count = 0
    lowerMessage = string.lower(message)
    for index in xrange (len(message)):
        if(message[index] != lowerMessage[index]):
            #uppercase in message[index]
            count = count + 1
    return count/float(len(message))


def countParagraphs(message):
    count = 0
    for c in message:
        if c == '\n':
            count += 1
    return count    
    
def countWords(message):
    return len(string.split(message))      
    
    
