"""The following file provides a rough prototype for an ASBA system.

Written by Griffin Gooch-Breault 3/17/2025
"""

# import
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
import nltk
from rake_nltk import Rake
import csv

# Example text:
test_sentence = """Steve Bannon is playing MAGA enforcer from the outside. Is the White House listening?"""
test_csv_path = """"""
test_aspects = ["Transgender", "MAGA", "Trump", "America"]


def extract_keywords(text, max_words):
    """
    Rudimentary system to take text and extract n top-rated keywords
    """
    r = Rake(max_length=max_words)

    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()


def named_entity_recognition(text):
    """
    Unfinished function to identify proper nouns
    """
    # Separate and tokenize words
    tokenized_text = nltk.word_tokenize(text)
    # Tag words with part-of-speech
    tagged_tokenized_text = nltk.pos_tag(tokenized_text)
    entities = nltk.ne_chunk(tagged_tokenized_text)

    #keywords = []
    #for i in entities:
    #if isinstance(i[0], tuple):

    #re.sub(r'^.*? ', '', i[0][0])


def instance_model():
    """Instantiate Model"""
    tokenizer = AutoTokenizer.from_pretrained(
        "yangheng/deberta-v3-base-absa-v1.1")
    model = AutoModelForSequenceClassification.from_pretrained(
        "yangheng/deberta-v3-base-absa-v1.1")
    return tokenizer, model


def run_absa(aspect, text):
    """Send text to model and format response"""
    tokenizer, model = instance_model()


    inputs = tokenizer(
        f"[CLS] {text} [SEP] {aspect} [SEP]",
        return_tensors="pt"
    )

    output = model(**inputs)

    return softmax_response(output)


def softmax_response(output):
    """
    Normalizes output
    """
    probs = F.softmax(output.logits, dim=1)
    probs = probs.detach().numpy()[0]

    for prob, label in zip(probs, ["Negative", "Neutral", "Positive"]):
        print(f"{label} = {prob}")
    print()


def sentence_response(output):
    """
    Returns sentence in a simple human-readable format.
    """
    probs = output.logits
    probs = probs.detach().numpy()[0]

    labeled_probs = zip(probs, ["Negative", "Neutral", "Positive"])

    print(f"{max(labeled_probs)[1]}\n")


def read_csv(path):
    """Function to return CSVs as lists."""
    file = open(path, encoding="utf8")
    csv_file = csv.reader(file)
    # this takes 0th element because CSVs only have one column
    lines = [i[0] for i in csv_file]
    return lines


def list_ASBA(aspects=[], texts=[]):
    """take input from list of text and aspects"""
    for a in aspects:
        for t in texts:
            print(f" - The sentiment of \"{a}\", in the text \"{t}\" is: \n")
            print(run_absa(a, t))


if __name__ == "__main__":
    texts = read_csv(test_csv_path)
    list_ASBA(test_aspects, texts)
    #print(read_csv(test_csv_path))
