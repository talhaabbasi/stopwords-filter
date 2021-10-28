from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

example_text = "Hello, how are you? The weather is great and Python is awesome."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)

example_sentence = "This is an example showing off stop word filtration."

stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)

filtered_sentence = [w for w in words if not w in stop_words]

print(filtered_sentence)

ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))
example_words = ["club","clubs","clubbing","clubed"]
for w in example_words:
    print(ps.stem(w))

new_sentence = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly atleast once."
words = word_tokenize(new_sentence)
for w in words:
    print(ps.stem(w))
