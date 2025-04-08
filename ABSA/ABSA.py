"""Instantiate model and create tools for running basic ASBA from input

Created by Griffin Gooch-Breault 4/7/2025
"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

tokenizer = AutoTokenizer.from_pretrained(
    "yangheng/deberta-v3-base-absa-v1.1")
model = AutoModelForSequenceClassification.from_pretrained(
    "yangheng/deberta-v3-base-absa-v1.1")


def run_absa(aspect, text):
    """Send text to model and format response"""

    inputs = tokenizer(
        f"[CLS] {text} [SEP] {aspect} [SEP]",
        return_tensors="pt"
    )

    output = model(**inputs)

    # This enforces that the sum of the output numbers = 1
    probs = F.softmax(output.logits, dim=1)
    probs = probs.detach().numpy()[0]

    out = ""

    for prob, label in zip(probs, ["Negative", "Neutral", "Positive"]):
        out += f"{label} = {prob}\n"

    return out


def list_absa(aspects, texts):
    """take input from list of text and aspects"""
    if aspects is None or texts is None:
        return None

    out = ""

    for a in aspects:
        for t in texts:
            out += (f" - The sentiment of \"{a}\", in the text \"{t}\" is: \n")
            out += run_absa(a, t)

    return out
