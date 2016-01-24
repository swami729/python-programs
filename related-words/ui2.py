#!/usr/bin/python
import relatedWords

class words:
    current_words = ""
    current_meanings = ""
    i = 0
    num_words = []
    related_word = ""
    total_answers_gussed = []
    related_words = {}
    related_words_list = []

    def init_answers(self):
        for word in self.related_words_list:
            self.total_answers_gussed.append([False] * len(self.related_words[word]))

        
    def __init__(self):
        relatedWords.make_dicts() 
        self.related_words = relatedWords.related_words
        # print self.related_words.keys()
        self.related_words_list = self.related_words.keys()
        self.num_words = len(self.related_words)
        self.init_answers()
        self.related_num_list = range(len(self.related_words_list))
        self.get_words_meanings()
#        print self.current_words
#        print self.current_meanings
        
    def get_words_meanings(self):
        self.related_num = self.related_num_list[self.i]
        self.related_word = self.related_words_list[self.related_num]
        self.current_words = relatedWords.get_words(self.related_word)
        self.current_meanings = relatedWords.get_words_meanings(self.related_word)
        

    def show_word_meaning(self,word,word_meanings,answer_gussed):
        output = []
        if answer_gussed == True:
            output.append("The word is :" + word)
        else:
            output.append("Word still not gussed : " + "    ")
        num = 0
        for meaning in word_meanings:
            output.append("   " + str(num + 1) + "> " + meaning)
            num += 1
        return output

    
    def show_words_screen(self):
        output = []
        answers_gussed = self.total_answers_gussed[self.i]
        output.append(">>> The related word is :" + self.related_word + " <<<\n\n")
        i = 0
        # print self.current_words
        for word in self.current_words:
            # print word
            output.append(" " + str(i + 1) + ") ")
            output = output + self.show_word_meaning(word, self.current_meanings[i], answers_gussed[i])
            i += 1
        return output

    
    def go_previous(self):
        if self.i == 0:
            self.i = len(self.related_words) - 1
        else:
            self.i -= 1
        self.get_words_meanings()

    def go_next(self):
        if self.i == len(self.related_words) - 1:
            self.i = 0
        else:
            self.i += 1
        self.get_words_meanings()


def get_input_key(valid_keys):
    while(True):
        print "\n\n"
        inp = raw_input("Enter The choice.." +str(valid_keys) + ">>> ")
        if inp.isdigit():
            inp = int(inp)
        if inp in valid_keys:
            return inp
        else:
            print "Sorry...Enter a valid number"
            
def inp_word_check(word, answers_gussed, wrd_no):
    inp_word = raw_input("Enter the word>>>")
    if inp_word == word:
        print "Right word"
        answers_gussed[wrd_no] = True
        return True
    else:
        print "Wrong answer!!!!"
        return False

# def show_subscreen(w, num):
#     answers_gussed = w.total_answers_gussed[w.i]
#     show_words_meanings(w.current_words[num], current_meanings[num], answers_gussed[num])
    
def main():
    MAIN_VALID_KEYS = ['q', 'p', 'n', 'r']
    SUB_VALID_KEYS = ['q', 'r']
    w = words()
    
    while True:
        inp1 = "r"
        while inp1 == "r":
            output = w.show_words_screen()
            print '\n'.join(output)
            inp1 = get_input_key(MAIN_VALID_KEYS + range(1, len(w.current_words) + 1))

        if type(inp1) == int:
            num = inp1 - 1
            inp2 = "r"
            while(inp2 == "r"):
                # show_subscreen(w, wrd_no)
                answers_gussed = w.total_answers_gussed[w.i]
                output = w.show_word_meaning(w.current_words[num], w.current_meanings[num], answers_gussed[num])
                print '\n'.join(output)
                inp_word_check(w.current_words[num], answers_gussed, num)
                inp2 = get_input_key(SUB_VALID_KEYS)
                
        if inp1 == "p":
            w.go_previous()
        elif inp1 == "n":
            w.go_next()
        elif inp1 == "q":
            exit(0)
            

if __name__ == "__main__":
    main()

# w = words()
# print w.current_words
# print w.current_meanings
# w.show_words_screen()
