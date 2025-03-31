"""The following file provides a rough prototype for an ASBA system.

Written by Griffin Gooch-Breault 3/17/2025"""

# import
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

# Example text:
test_sentence = """
    I really do like living in Vermont, but I absolutely hate the snow.
    """


# Example aspects:
aspect = ["Vermont", "Snow"]


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
    probs = F.softmax(output.logits, dim=1)
    probs = probs.detach().numpy()[0]

    for prob, label in zip(probs, ["Negative", "Neutral", "Positive"]):
        print(f"{label} = {prob}")
    print()


def sentence_response(output):
    probs = output.logits
    probs = probs.detach().numpy()[0]

    labeled_probs = zip(probs, ["Negative", "Neutral", "Positive"])

    print(f"{max(labeled_probs)[1]}\n")


if __name__ == "__main__":
    run_absa(aspect, test_sentence)
