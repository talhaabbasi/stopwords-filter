from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

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