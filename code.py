import sys

if len(sys.argv) != 2:
    print 'Usage: code.py WORD_LIST_FILE_NAME'
    sys.exit(0)
    
wordlist = sys.argv[1]
words = [x.strip().lower() for x in open(wordlist, 'r').read().split("\n")]
print 'Dictionary has %d words' % (len(words))
elems = [x.lower() for x in open('elements.txt', 'r').read().split("\n")]
elems1 = filter(lambda x: len(x) == 1, elems)
elems2 = filter(lambda x: len(x) == 2, elems)
elems3 = filter(lambda x: len(x) > 2, elems)
print 'Read %d elements. %d 1-leter, %d 2-letter, %d 3-letter' % (len(elems), len(elems1), len(elems2), len(elems3))

## We ignore the 3 letter elements
def elements_only(word):
    s2 = [word[i:i+2] for i in xrange(0, len(word), 2)]
    ## remove all 2 letter elements
    t1 = filter(lambda x: x not in elems2, s2)
    if len(t1) == 0: return True
    ## remove all 1 letter elements
    t2 = filter(lambda x: x not in elems1, list(''.join(t1)))
    ##print s2, '\n  ', t1, '\n    ', t2
    return len(t2) == 0

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
