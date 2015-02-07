import string

"""This is a function designed to extract an attribute vector out of the text of
a Craigslist posting. These attribute vectors will be fed to the SciKit Learn
module to determine the quality of the posting itself."""
def extractVectorsFromListOfPosts(postList):
    
    def extractVectorFromPost(postText):
        upperCaseText = string.upper(postText)
        count, whiteCount, letterCount, symbolCount, lowerCaseCount = 0, 0, 0 ,0, 0
        for i in xrange(len(postText)):
            if postText[i] in string.whitespace: whiteCount += 1
            elif postText[i] in string.ascii_letters: 
                letterCount += 1
                lowerCaseCount += (1 - (upperCaseText[i] == postText[i]))
            else: symbolCount += 1
            #Python boolean arithmetic casts True to 1 and 0 to False.
            #If a char was lowercase, the count will increase
        upperCaseRatio = 1 - float(lowerCaseCount)/letterCount
        symbolRatio = float(symbolCount)/count
        whiteRatio = float(whiteCount)/count
        return [upperCaseRatio, symbolRatio, whiteRatio]
        
    return [extractVectorFromPost(postText) for postText in postList]
    
def extractVectorsFromListOfPosts(postList):
    return [extractVectorFromPost]