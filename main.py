from flask import Flask
import sys
import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer 


book_one = open("static\Frankenstein.txt", encoding="utf8").read()

book_two = open("static\Dracula.txt", encoding="utf8").read()

book_three = open("static\Hound of Baskersville.txt", encoding="utf8").read()

book_four = open("static\Crime and Punishment.txt", encoding="utf8").read()


def clean_words(text):
    def remove_nonAscii(text):
        return ''.join((c for c in str(text) if ord(c) < 128))

    def make_lowercase(text):
        text = str(text).lower()
        return text

    def remove_stopwords(text):
        text = text.split() 
        stops = set(stopwords.words("english"))
        text = [w for w in text if not w in stops]
        text = " ".join(text)
        return text

    def remove_punctuation(text):
        tokenizer = RegexpTokenizer(r'\w+')
        text = tokenizer.tokenize(text)
        text = " ".join(text)
        return text

    def remove_html(text):
        html_pattern = re.compile("<.*?>")
        return html_pattern.sub(r'', text)


    input = remove_nonAscii(text)
    input = make_lowercase(input)
    input= remove_stopwords(input)
    input = remove_punctuation(input)
    input = remove_html(input)

    return input



#print (book_one.encode("utf-8"))
processed_inputs_one = clean_words(book_one)
processed_inputs_two = clean_words(book_two)
processed_inputs_three = clean_words(book_three)
processed_inputs_four = clean_words(book_four)
final_input = processed_inputs_one + processed_inputs_two + processed_inputs_three + processed_inputs_four

#print(processed_inputs.encode("utf-8"))

chars = sorted(list(set(final_input)))
char_to_num = dict((c, i) for i, c in enumerate(chars))
input_len = len(final_input)
vocab_len = len(chars)
print ("Total number of characters:", input_len)
print ("Total vocab:", vocab_len)

    










# appy = Flask(__name__)
# if __name__ == '__main__':
#     appy.run(debug=True)



