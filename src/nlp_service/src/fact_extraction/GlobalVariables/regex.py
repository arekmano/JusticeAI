import re

class Regex:
    phrase_match = re.compile('ADJP|PP|ADVP|NP|S|SQ|SBARQ|VP')
    noun_match = re.compile('NN|PRP|PRP$|CC')
    noun_phrase_match = re.compile('NP')
    verb_match = re.compile('VB|IN|TO')
    w_word_match = re.compile('WRB')
    verb_phrase_match = re.compile('VP|WHADVP')
    adjective_match = re.compile('JJ|CC')
    determiner_match = re.compile('DT|EX')
    adjective_phrase_match = re.compile('ADJP')
    prepositoinal_phrase_match = re.compile('PP')
    conjunction_match = re.compile('CC')
    adverb_match = re.compile('RB')
    adverb_phrase_match = re.compile('ADVP')
