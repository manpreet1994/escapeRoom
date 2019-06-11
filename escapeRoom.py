# -*- coding: utf-8 -*-
def wordcheckinDictionary(result):
    #import nltk
    from nltk.corpus import words
    wordsThatMakesSense=[]
    listOfWords=set(words.words())
    for x in result:
        if(x in listOfWords):
            wordsThatMakesSense.append(x)
    return wordsThatMakesSense


def findAnswer(samplelist, desiredchar,char):
    from itertools import permutations
    guessAnswer = []
    result=[]
    char_comb = permutations(samplelist,desiredchar)
    for x in char_comb:
        jword = ''.join(x)
        guessAnswer.append(jword)
    result = [i for i in guessAnswer if i.startswith(char)]
    #print (wordcheckinDictionary(result))
    return (wordcheckinDictionary(result))
    
def checkWordRepation(chars):
    repalpha = ['ss','ee', 'tt', 'ff', 'll', 'mm', 'oo','nn', 'pp']
    validReps = []
    for x in repalpha:
        if(x[1] in chars):
            validReps.append(x[1])
    return validReps
    
def wordsthatmatter(inputStr, lenreq):
    ansList = []
    #puzzleWords = significanceOrder(inputStr)
    puzzleWords = inputStr
    characters = list(puzzleWords)
    for x in characters:
        ansList.append(findAnswer(characters, lenreq, x))
        #print(ansList)
    return ansList
    

def wordsthatmatterRepitition(inputStr, lenreq):
    finalans=[]
    repWords = checkWordRepation(list(inputStr))
    print("length = ", len(repWords), repWords)
    for i in range(0,len(repWords)):
        puzzleWords = inputStr
        puzzleWords = puzzleWords + repWords[i]
        #puzzleWords = significanceOrder(puzzleWords)
        possibleWords = wordsthatmatter(puzzleWords,lenreq)
        
        if len(finalans)!=0:
            for l1 in range(0,len(possibleWords)):
                for l2 in possibleWords[l1]:
                    #print("L1 List ", finalans[l1],"and l2", l2)
                    if( l2 not in finalans[l1]):
                        finalans[l1].append(l2)
                        #print("going in ",l2) 
                    else:
                        #print("present already")
                        pass
        else:
          #  pass
            finalans=possibleWords
    return finalans
        
def significanceOrder(inputWords):
    significantOrderList = []
    alphabetFreq = list("taoiswcbphfmdrelnguvyjkqxz")   
    for x in alphabetFreq:
        if(x in inputWords):
            significantOrderList.append(x)
    return significantOrderList
            
############################ Main Functions ##############################
import time
start = time.time()
abc=wordsthatmatter('tefvginyrxso',5)
end = time.time()
print("time taken", end-start)

import time
start = time.time()
abc=wordsthatmatterRepitition('tefvginyrxso',5)
end = time.time()
print("time taken", end-start)



