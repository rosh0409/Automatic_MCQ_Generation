from flashtext import KeywordProcessor
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import string
import pke
import traceback

def get_nouns_multipartite(content):
    out=[]
    try:
        
        extractor = pke.unsupervised.MultipartiteRank()
        extractor.load_document(input=content,language='en')
        # extractor.load_document()
        #    not contain punctuation marks or stopwords as candidates.
        pos = {'PROPN','NOUN'}
        #pos = {'PROPN','NOUN'}
        stoplist = list(string.punctuation)
        # print("1 :: ",stoplist)
        stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
        # print("2 :: ",stoplist)
        stoplist += stopwords.words('english')
        # print("3 :: ",stoplist)
        # extractor.candidate_selection(pos=pos, stoplist=stoplist)
        extractor.candidate_selection(pos=pos)
        # 4. build the Multipartite graph and rank candidates using random walk,
        #    alpha controls the weight adjustment mechanism, see TopicRank for
        #    threshold/method parameters.
        extractor.candidate_weighting(alpha=1.1,
                                      threshold=0.75,
                                      method='average')
        keyphrases = extractor.get_n_best(n=15)
        

        for val in keyphrases:
            out.append(val[0])
    except:
        out = []
        traceback.print_exc()

    return out

def get_keywords(originaltext,summarytext,noOfKeywords):
  keywords = get_nouns_multipartite(originaltext)
  keyword_processor = KeywordProcessor()
  for keyword in keywords:
    keyword_processor.add_keyword(keyword)

  keywords_found = keyword_processor.extract_keywords(summarytext)
  keywords_found = list(set(keywords_found))

  important_keywords =[]
  for keyword in keywords:
    if keyword in keywords_found:
      important_keywords.append(keyword)

  if len(important_keywords) < noOfKeywords:
      noOfKeywords = len(important_keywords)
  return important_keywords[:noOfKeywords]

# raw_text="A Lion lay asleep in the forest, his great head resting on his paws. A timid little Mouse came upon him unexpectedly, and in her fright and haste to get away, ran across the Lion's nose. Roused from his nap, the Lion laid his huge paw angrily on the tiny creature to kill her. Spare me! begged the poor Mouse. Please let me go and some day I will surely repay you. The Lion was much amused to think that a Mouse could ever help him. But he was generous and finally let the Mouse go. Some days later, while stalking his prey in the forest, the Lion was caught in the toils of a hunter's net. Unable to free himself, he filled the forest with his angry roaring. The Mouse knew the voice and quickly found the Lion struggling in the net. Running to one of the great ropes that bound him, she gnawed it until it parted, and soon the Lion was free. You laughed when I said I would repay you, said the Mouse. Now you see that even a Mouse can help a Lion."
# summarized_text = "A Lion lay asleep in the forest, his great head resting on his paws. A timid little Mouse came upon him unexpectedly, and in her fright and haste to get away, ran across the Lion's nose. Roused from his nap, the Lion laid his huge paw angrily on the tiny creature to kill her. Some days later, while stalking his prey in the forest, the Lion was caught in the toils of a hunter's net. Running to one of the great ropes that bound him, she gnawed it until it parted, and soon the Lion was free."

# imp_keywords = get_keywords(raw_text,summarized_text,10)
# print ("keywords :: ",imp_keywords)
