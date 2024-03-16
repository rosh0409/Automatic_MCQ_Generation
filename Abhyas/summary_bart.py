from transformers import pipeline

pipe = pipeline("summarization", model="facebook/bart-large-cnn")
#  *,max_length=90, min_length=30*/
def get_summary(raw_text):
    pipe_out = pipe(raw_text,max_length=len(raw_text)/6, min_length=30)
    return pipe_out[0]["summary_text"]