#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        new_sentence = len(sentence)
    else:
        new_sentence = 0
    return(new_sentence, sentence if not sentence else sentence[:1])
