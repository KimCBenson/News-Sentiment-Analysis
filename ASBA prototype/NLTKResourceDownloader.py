"""This file downloads the relevant NLTK dependencies onto a machine

Griffin Gooch-Breault """

import nltk

# system requires these resources, need better solution than this
NLTK_REQUIREMENTS = {
    'punkt',
    'stopwords',
    'averaged_perceptron_tagger_eng',
    'maxent_ne_chunker_tab',
    'words'
}

for i in NLTK_REQUIREMENTS:
    nltk.download(i)
