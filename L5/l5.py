from trie import *
from b_plus import *
from porter_stemmer import *
from pathlib import Path
import string
import os

def app_direct_quant_index(exc, noise, folder):
    k = 0
    dir_index = BplusTree(19)
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
    port = PorterStemmer()

    p = Path(os.getcwd() + '/L5/' + folder)
    for q in p.iterdir():
        if not q.is_dir():
            key = BplusTree.hash_str(q,31,19)
            with open(q, "r") as g:
                c = 0
                while g.tell() != None:
                    wrd = ''
                    while g.read(1) not in (string.whitespace + '_\'.,:;[]()?\\|`~<>=+/*&^%$#@!+'):
                        g.seek(c)
                        try:
                            g.read(1)
                        except:
                            continue
                        else:
                            char = g.read(1)
                            wrd += char
                        finally: c += 1
                        if stopwords.partial_search(char) is None:
                            continue
                        if exceptions.partial_search(char) is None:
                            continue
                    c += 1
                    if wrd is not '':
                        wrd = wrd.lower()
                        print(wrd)
                        if exceptions.search(wrd):
                            dir_index.insert(wrd, key)
                        elif stopwords.search(wrd):
                            continue
                        else:
                            wrd = port.stem(wrd, 0, len(wrd) - 1)
                            if dir_index.search(wrd):
                                k += 1
                                dir_index.insert(wrd, key)
    dir_index.printTree()

if __name__ == "__main__":
    app_direct_quant_index("L5/exceptions.txt", "L5/stopwords.txt", "books")