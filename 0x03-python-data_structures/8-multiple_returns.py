#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        new_sent = (len(sentence), sentence[0])
    else:
        new_sent = (0, None)
    return new_sent
