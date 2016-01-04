import sys, re

if len(sys.argv) != 2:
    print 'Usage: code.py WORD_LIST_FILE_NAME'
    sys.exit(0)
    
wordlist = sys.argv[1]
words = [x.strip().lower() for x in open(wordlist, 'r').read().split("\n")]
print 'Dictionary has %d words' % (len(words))

elems = [x.lower() for x in open('elements.txt', 'r').read().split("\n")]
elems_regex = re.compile('^(?:'+'|'.join(elems)+')+$', re.I)

def elements_only(word):
    return elems_regex.match(word) is not None

n = 0
valid_w = []
for word in words:
    if elements_only(word):
        valid_w.append(word)
    n += 1
    if n % 100 == 0:
        sys.stdout.write('\rProcessed %d words and found %d valid words' % (n, len(valid_w)))
        sys.stdout.flush()
print

o = open('elemental-%s' % (wordlist), 'w')
for w in valid_w:
    o.write(w+"\n")
o.close()
