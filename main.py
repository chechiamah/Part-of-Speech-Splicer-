import nltk
nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')
from nltk.tag import pos_tag
from nltk import RegexpParser, chunk
from nltk.tokenize import word_tokenize, sent_tokenize
#from chunk_counters import np_chunk_counter

# import text of choice here
text = "None"
while text != "q":
  text = input ("Enter a sentence (press 'q' to quit): ") 
  if text == 'q':
    break
# old code for the classic book files 
#open("dorian_gray.txt",encoding='utf-8').read().lower()

# word tokenize the text

  sentence_tokenized_text = sent_tokenize(text);
  word_tokenized_text = [word_tokenize(sent) for sent in sentence_tokenized_text]

# make sure we can print a single word
# single_word_tokenized_sentence = word_tokenized_text[77]
# print(single_word_tokenized_sentence)

# put part-of-speech-tagged text in a list and make sure we can print one tagged word
  pos_tagged_text = [pos_tag(word) for word in word_tokenized_text]
  print(pos_tagged_text)

# define adjective-noun chunk grammar here
  chunk_grammar =  "AN:{<JJ><NN>}"

# create RegexpParser object here
  chunk_parser = RegexpParser(chunk_grammar)

# define noun phrase chunk grammar here
  np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create noun phrase RegexpParser object here
  np_chunk_parser = RegexpParser(np_chunk_grammar)

# define verb phrase chunk grammar here
  vp_chunk_grammar =  "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"

# create verb phrase RegexpParser object here
  vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
  np_chunked_text = []
  vp_chunked_text  = []


# create a for loop through each pos-tagged sentence here
  for pos_tagged_sentence in pos_tagged_text:
  # chunk each sentence and append to lists here
    np_chunked_text.append(np_chunk_parser.parse(pos_tagged_sentence))
    vp_chunked_text.append(vp_chunk_parser.parse(pos_tagged_sentence))

#print(vp_chunked_text)

# this should be able to work on CodeAcademy with the "from collections import Counter" import 

# store and print the most common NP-chunks here
#most_common_np_chunks = np_chunk_counter(np_chunked_text)
#print(most_common_np_chunks)

# store and print the most common VP-chunks here
#most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
#print(most_common_vp_chunks)

