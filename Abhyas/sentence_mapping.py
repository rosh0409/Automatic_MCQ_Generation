from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor
def tokenize_sentences(text):
  sentences = [sent_tokenize(text)]
  sentences = [y for x in sentences for y in x]
  # Remove any short sentences less than 20 letters.
  sentences = [sentence.strip() for sentence in sentences if len(sentence) > 20]
  return sentences

def get_sentences_for_keyword(final_keywords, sentences):
  keyword_processor = KeywordProcessor()
  keyword_sentences = {}
  for word in final_keywords:
    keyword_sentences[word] = []
    keyword_processor.add_keyword(word)
  for sentence in sentences:
    keywords_found = keyword_processor.extract_keywords(sentence)
    for key in keywords_found:
      keyword_sentences[key].append(sentence)
  for key in keyword_sentences.keys():
    values = keyword_sentences[key]
    values = sorted(values, key=len, reverse=True)
    keyword_sentences[key] = values
  return keyword_sentences

# sentences = tokenize_sentences(summarized_text)
# keyword_sentence_mapping = get_sentences_for_keyword(final_keywords, sentences)
# keyword_sentence_mapping1 = get_sentences_for_keyword(imp_keywords, sentences)

# print (keyword_sentence_mapping)
# print (len(keyword_sentence_mapping))
# print (keyword_sentence_mapping1)
# print (len(keyword_sentence_mapping1))