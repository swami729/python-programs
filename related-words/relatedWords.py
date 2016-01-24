#!/usr/bin/python

words_to_num = {}
num_to_words = {}
related_words = {}
words_meaning = {}
#num = 1

# add the related word to the related_words dictionary
# INPUT : related-word , number representing the word  
def add_related(related_word, num):
    if not related_word in related_words:
        related_words[related_word]= []
    # print "[add_related]" + related_word + ":" + str(num)
    related_words[related_word].append(num)

# relate a word with a number, which is then appended to related_word's list
# INPUT : word extracted from the file
def add_word_num(word, num):
    if not word in words_to_num:
        words_to_num[word] = num
        num_to_words[num] = word
        num += 1
        # print "[add_word_num]" + word + ":" + str(num)
    return num

# add the word's number with related word's list
# INPUT : filename of the related-words and words
def make_relation_dict(filename):
    num = 1
    for line in filename:
        if line[0] != "\t":
            related_word = line[:-1]
            # print "[make_relation_dict]" + related_word
        else:
            word = line[1:-1]
            num = add_word_num(word, num) # num is incremented here need workaround
            add_related(related_word, words_to_num[word])
            # print "[make_relation_dict]" +  ":" + word + ":" + str(num)
            # need to check if the number is already in the word's list before adding to it
          
# get meanings of the words and map-it with filenames
# INPUT : filename containing the meanings
def make_meanings_dict(mean_file):
    for line in mean_file:
        line = line[:-1]
        # print "[make_menaings_dict]" + ":" + line
        if line[0] != "\t" :
            num = words_to_num[line]      
            if not num in words_meaning:
                words_meaning[num] = []
        else:
            meaning = line[1:]
            words_meaning[num].append(meaning)
            # a word can have multiple meanings, each meaning is given in a line
            # same word with different meaning can be given in different places in the file
#        print "[make_meanings_dict]" + str(num) + ":" + ":" + meaning

    
# Return : list of words for the related-word
def get_words(related_word):
    words_list = []
    for num in related_words[related_word]:
        words_list.append(num_to_words[num])
    return words_list

# Return : list of meaning(s) for words with related-word
def get_words_meanings(related_word):
    meanings_list = []
    for num in related_words[related_word]:
        meanings_list.append(words_meaning[num])
    return meanings_list


def make_dicts():
    MEANINGS_FILE = "meanings.txt"
    RELATIONS_FILE = "relations.txt"
    relations_file = open(RELATIONS_FILE)
    meanings_file = open(MEANINGS_FILE)
    make_relation_dict(relations_file)
    make_meanings_dict(meanings_file)
