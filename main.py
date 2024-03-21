from flask import Flask , render_template,request

import nltk
nltk.download("all")
from Abhyas.extractive_text_summarization import summarize
from Abhyas.keyword_extraction import get_keywords
# from Abhyas.sentence_mapping import tokenize_sentences , get_sentences_for_keyword
from Abhyas.question_generation import get_question
from Abhyas.summary_bart import get_summary
from Abhyas.question_generation_t5 import get_questions
from Abhyas.wrong_option_generation import get_distractors
app = Flask(__name__)


# @app.route("/")
# def a():
#     return "hello"


# @ app.route("/hii")
# def hii():
#     return "hii"

@app.route("/get-MCQ",methods=["GET","POST"])
def a():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        data = request.get_json()
        raw_text = data["raw_text"]
        # print(raw_text)
        summary_text = get_summary(raw_text)
        # summarized_text = summarize(raw_text)
        keywords = get_keywords(raw_text,summary_text,10)
        # sentences = tokenize_sentences(summarized_text)
        # keyword_sentence_mapping = get_sentences_for_keyword(keywords,sentences)
        question1 = tuple()
        # question2 = tuple()
        for answer in keywords:
          question1 += (get_question(summary_text,answer),)
        #   question2 += (get_questions(summary_text,answer),)

        #   print (question)
        #   print (answer.capitalize())
        #   print ("\n")
        list_question1 = list(question1)
        # list_question2 = list(question2)
        option = list()
        for i in range(0,len(keywords)):
            option += [get_distractors(keywords[i],list_question1[i],40,0.2)]
            keywords[i] = keywords[i].capitalize()


        MCQ = {
            "Question1":list_question1,
            # "Question2":list_question2,
            "Answer":keywords,
            "Option":option
        }
        return MCQ























# @app.get('/home/<menu>')
# def single_converter(menu):
 
#     return "You tried accessing 'single_converter' \
#     endpoint with value of 'menu' as " + str(menu)
 
# text = """A Lion lay asleep in the forest, his great head resting on his paws. A timid little Mouse came upon him unexpectedly, and in her fright and haste to
# get away, ran across the Lion's nose. Roused from his nap, the Lion laid his huge paw angrily on the tiny creature to kill her.  "Spare me!" begged
# the poor Mouse. "Please let me go and some day I will surely repay you."  The Lion was much amused to think that a Mouse could ever help him. But he
# was generous and finally let the Mouse go.  Some days later, while stalking his prey in the forest, the Lion was caught in the toils of a hunter's
# net. Unable to free himself, he filled the forest with his angry roaring. The Mouse knew the voice and quickly found the Lion struggling in the net.
# Running to one of the great ropes that bound him, she gnawed it until it parted, and soon the Lion was free.  "You laughed when I said I would repay
# you," said the Mouse. "Now you see that even a Mouse can help a Lion." """
# # print(extractive_text_summarization.summarize_raw_text(text))
# @app.route("/")
# def hello():
#     text1 , summary = extractive_text_summarization.summarize_raw_text(text)
#     keyword = keyword_extraction.get_keywords(text1,summary,10)
#     return "Text :: {} /n  Summary :: {} /n Keyword :: {}".format(text1,summary,keyword)

# @app.post("/add")
# def ret():
#     return "hii"
    # a = int(request.values['a'])
    # b = int(request.values['b'])
    # print(a,b)
    # return a+b


if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")
