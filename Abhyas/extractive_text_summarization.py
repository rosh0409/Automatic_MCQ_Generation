from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stopWords = set (stopwords.words("english"))

def summarize(raw_text):
  words = word_tokenize(raw_text)
  freqTable = dict()
  for word in words:
    word = word.lower()
    if word in stopWords:
      continue
    if word in freqTable:
      freqTable[word] += 1
    else:
      freqTable[word] = 1
  sentences = sent_tokenize(raw_text)
  sentenceValue = dict()

  for sentence in sentences:
    for word, freq in freqTable.items():
      if word in sentence.lower():
        if sentence in sentenceValue:
          sentenceValue[sentence] += freq
        else:
          sentenceValue[sentence] = freq

  sumValues = 0

  for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

  average = int(sumValues / len(sentenceValue))

  summarized_text = ""

  for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
      summarized_text += " " + sentence

  return(summarized_text)


# input_text = "A Lion lay asleep in the forest, his great head resting on his paws. A timid little Mouse came upon him unexpectedly, and in her fright and haste to get away, ran across the Lion's nose. Roused from his nap, the Lion laid his huge paw angrily on the tiny creature to kill her. Spare me! begged the poor Mouse. Please let me go and some day I will surely repay you. The Lion was much amused to think that a Mouse could ever help him. But he was generous and finally let the Mouse go. Some days later, while stalking his prey in the forest, the Lion was caught in the toils of a hunter's net. Unable to free himself, he filled the forest with his angry roaring. The Mouse knew the voice and quickly found the Lion struggling in the net. Running to one of the great ropes that bound him, she gnawed it until it parted, and soon the Lion was free. You laughed when I said I would repay you, said the Mouse. Now you see that even a Mouse can help a Lion."

# summarize(input_text)


























































































# import torch
# from transformers import T5ForConditionalGeneration,T5Tokenizer
# import nltk
# # nltk.download('punkt')
# # nltk.download('brown')
# # nltk.download('wordnet')
# from nltk.corpus import wordnet as wn
# from nltk.tokenize import sent_tokenize

# summary_model = T5ForConditionalGeneration.from_pretrained('t5-base')
# summary_tokenizer = T5Tokenizer.from_pretrained('t5-base')

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# summary_model = summary_model.to(device)

# def postprocesstext (content):
#   final=""
#   for sent in sent_tokenize(content):
#     sent = sent.capitalize()
#     final = final +" "+sent
#   return final



# def summarize_raw_text(text):
#   text = text.strip().replace("\n"," ")
#   text = "summarize: "+text
#   # print (text)
#   max_len = 512
#   encoding = summary_tokenizer.encode_plus(text,max_length=max_len, pad_to_max_length=False,truncation=True, return_tensors="pt").to(device)

#   input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

#   outs = summary_model.generate(input_ids=input_ids,
#                                   attention_mask=attention_mask,
#                                   early_stopping=True,
#                                   num_beams=3,
#                                   num_return_sequences=1,
#                                   no_repeat_ngram_size=2,
#                                   min_length = 75,
#                                   max_length=300)


#   dec = [summary_tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]
#   summary = dec[0]
#   summary = postprocesstext(summary)
#   summary= summary.strip()

#   return text , summary

# # text = """A Lion lay asleep in the forest, his great head resting on his paws. A timid little Mouse came upon him unexpectedly, and in her fright and haste to
# # get away, ran across the Lion's nose. Roused from his nap, the Lion laid his huge paw angrily on the tiny creature to kill her.  "Spare me!" begged
# # the poor Mouse. "Please let me go and some day I will surely repay you."  The Lion was much amused to think that a Mouse could ever help him. But he
# # was generous and finally let the Mouse go.  Some days later, while stalking his prey in the forest, the Lion was caught in the toils of a hunter's
# # net. Unable to free himself, he filled the forest with his angry roaring. The Mouse knew the voice and quickly found the Lion struggling in the net.
# # Running to one of the great ropes that bound him, she gnawed it until it parted, and soon the Lion was free.  "You laughed when I said I would repay
# # you," said the Mouse. "Now you see that even a Mouse can help a Lion." """

# # summarized_text = summarize_raw_text(text,summary_model,summary_tokenizer)

# # print(summarized_text)