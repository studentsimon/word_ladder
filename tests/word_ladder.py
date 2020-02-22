#!/bin/python3

import collections
from collections import deque
import copy


def ladderLength(beginWord, endWord, dictionary_file='words5.dict'):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        f = open(dictionary_file,'r')


        wordList = [line[0:5] for line in f.readlines()]


        

        lit = [beginWord]
        
        if beginWord in wordList:
            wordList.remove(beginWord)
        
        if endWord not in wordList:
            return "ERROR, END WORD IS NOT IN LIST"

        lit.append(endWord)
        queue = collections.deque([[beginWord, 1]])
        leng = len(beginWord)
        
        while queue:
            print(lit)
            word, length = queue.popleft()
            if word == endWord:
                print(lit) 
                return length
            wordListCopy = wordList.copy()

        
            for n in wordListCopy:
                if sum(n[i]!=word[i] for i in range(leng))==1:
                    wordList.remove(n)
                    queue.append(n)
                    lit.append([n,length+1])
                    
        
        return 0
        


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):


    f = open(dictionary_file,'r')
    wordList = [line[0:5] for line in f.readlines()]
    
    list1 = []                                                  #create a stack
    list1.append(start_word)                                    #push start word onto stack
    q1 = deque()                                                #create a queue
    q1.append(list1)                                            #enque the stack onto the queue
    while len(q1) > 0:                                          #while queue is not empty
            o1 = q1.popleft()                                   #dequeue a stack from the queue
            for i in wordList:                                  #for each word in the dictionary
                    if _adjacent(o1[len(o1)-1], i):             #if word is adjacent to the top of the stack
                            if i == end_word:
                                    print(o1[len(o1)-1])        #if word is end word
                                    print(i)                    
                                    
                                
                                    o3 = o1
                                    o3.append(i)
                                    
                                                                #you are done
                                    return(o3)                  #front stack + this word is word ladder
                                              
                            o2 = copy.deepcopy(o1)              #make copy of the stack
                            o2.append(i)                        #push found word onto copy
                            q1.append(o2)                       #enqueue the copy
                            wordList.remove(i)                  #delete word from dictionary                              
                         
                            
                            
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    


def verify_word_ladder(ladder):
    if len(ladder) == 0:
            return False
        
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    while len(ladder) >= 1:
            if _adjacent(ladder[0], ladder[1]) == True:
                    ladder.remove(ladder[0])
                    
            else:
                    return False

    return True
                


def _adjacent(word1, word2):

    i = 0
    
    if len(word1) != len(word2):
        return False

    if word1[:1] == word2[:1]:
        i = i + 1
        
    if word1[1:2] == word2[1:2]:
        i = i + 1

    if word1[2:3] == word2[2:3]:
        i = i + 1
        
    if word1[3:4] == word2[3:4]:
        i = i + 1

    if word1[4:5] == word2[4:5]:
        i = i + 1

    

    if i == 4:   
        return True
    else:
        return False
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

