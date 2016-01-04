import sys, re

if len(sys.argv) != 2:
    print 'Usage: code.py WORD_LIST_FILE_NAME'
    sys.exit(0)
    
wordlist = sys.argv[1]
words = open(wordlist, 'r').read()
print 'Dictionary has %d words' % (len(re.findall('\n', words)))
elems = filter(lambda x: x != '', [x.lower() for x in open('elements.txt', 'r').read().split("\n")])
valid_w = re.findall('(^(?:'+'|'.join(elems)+')+?$)', words, re.I|re.M)
print 'Found %d elemental words' % (len(valid_w))
o = open('elemental-%s' % (wordlist), 'w')
for w in valid_w:
    o.write(w+"\n")
o.close()
