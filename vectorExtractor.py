import string
import sklearn
import numpy as np
from titleParse import *
import os


#testStringList = getTitles("test_data" + os.sep + "merged.txt")
#testStringList = getTitles("test.txt")
"""This is a function designed to extract an attribute vector out of the text of
a Craigslist posting. These attribute vectors will be fed to the SciKit Learn
module to determine the quality of the posting itself."""
def extractVectorsFromListOfPosts(postList):
    
    def extractVectorFromPost(postText):
        upperCaseText = string.upper(postText)
        count = len(postText)
        whiteCount, letterCount, symbolCount, lowerCaseCount = 0, 0 ,0, 0
        for i in xrange(count):
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
        return [upperCaseRatio, symbolRatio, whiteRatio,count]

    result = np.array(map(extractVectorFromPost,postList))
    #print result
    np.set_printoptions(precision=3)
    np.savetxt('long_run.txt',result)
    return result

def writeFile(filename, contents, mode="wt"):
    # wt stands for "write text"
    fout = None
    try:
        fout = open(filename, mode)
        fout.write(contents)
    finally:
        if (fout != None): fout.close()
    return True

extractVectorsFromListOfPosts(getTitles('output.txt'))
