from __future__ import print_function
import sys, re

if len(sys.argv) != 2:
    print('Usage: code.py WORD_LIST_FILE_NAME')
    sys.exit(0)
    
wordlist = sys.argv[1]
words = open(wordlist, 'r').read()
print('Dictionary has %d words' % (len(re.findall('\n', words))))
with open('elements.txt', 'r') as eles:
    elems = {e.lower(): e for e in eles.read().split()}
valid_w = re.findall('(^(?:'+'|'.join(elems.keys())+')+?$)', words, re.I|re.M)
print('Found %d elemental words' % (len(valid_w)))
pattern = re.compile('|'.join(elems.keys()))
elementify = lambda s: pattern.sub(lambda x: elems[x.group()], s)
with open('elemental-%s' % (wordlist), 'w') as o:
    for w in valid_w:
        o.write(elementify(w)+"\n")
