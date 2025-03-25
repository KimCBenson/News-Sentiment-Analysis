"""The following file provides a rough prototype for an ASBA system.

Written by Griffin Gooch-Breault 3/17/2025
"""

# import
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
import nltk

# rake_nltk requires these resources, need better solution than this
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


from rake_nltk import Rake


# Example text:
test_sentence = """
    Steve Bannon is playing MAGA enforcer from the outside. Is the White House listening?
    """


def extract_keywords(text, max_words):
    """
    Rudimentary system to take text and extract n top-rated keywords
    """
    r = Rake(max_length=max_words)

    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()


def instance_model():
    """Instantiate Model"""
    tokenizer = AutoTokenizer.from_pretrained(
        "yangheng/deberta-v3-base-absa-v1.1")
    model = AutoModelForSequenceClassification.from_pretrained(
        "yangheng/deberta-v3-base-absa-v1.1")
    return tokenizer, model


def run_absa(aspects, text):
    """tokenize text and aspect"""
    tokenizer, model = instance_model()

    for a in aspects:
        inputs = tokenizer(
            f"[CLS] {text} [SEP] {a} [SEP]",
            return_tensors="pt"
        )

        output = model(**inputs)

        print(f"Sentiment of '{a}' is:")
        softmax_response(output)


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


if __name__ == "__main__":
    aspects = extract_keywords(test_sentence, 4)
    run_absa(aspects, test_sentence)
