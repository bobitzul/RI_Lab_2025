from trie import *
from b_plus import *
from pathlib import Path
import os

def app_direct_quant_index(exc, noise, folder):
    stopwords = TrieNode()
    exceptions = TrieNode()
    e = open(exc, "r")
    f = open(noise, "r")
    for line in f:
        key = line.strip()
        stopwords.insert(key)
    f.close()
    for line in e:
        key = line.strip()
        exceptions.insert(key)
    e.close()

    #print(stopwords.search(';ve'))
    #print(stopwords.search('\'ve'))

    p = Path(os.getcwd() + '/L5/' + folder)
    for q in p.iterdir():
        if not q.is_dir():
            g = open(q, "r")
            wrd = ''
            while g.read(1) not in '.,/;:\n':
                wrd += g.read(1)
                stopwords.partial_search(wrd)
                exceptions.partial_search(wrd)
            #if exceptions.search(wrd):


            



if __name__ == "__main__":
    app_direct_quant_index("L5/exceptions.txt", "L5/stopwords.txt", "books")
