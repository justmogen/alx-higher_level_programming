#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        return (leng, None)
    else:
        return (leng, sentence[0])
