from trie import *
from b_plus import *
from pathlib import Path

def app_direct_quant_index(exc, noise, folder):
    stopwords = TrieNode()
    exceptions = TrieNode()
    f = open(noise, "r")
    e = open(exc, "r")
    for line in f:
        key = line.strip()
        stopwords.insert(key)
    f.close()
    for line in e:
        key = line.strip()
        exceptions.insert(key)
    e.close()
    print(stopwords)
    print(exceptions)

    p = Path(folder)
    



if __name__ == "__main__":
    app_direct_quant_index("exceptions.txt", "stopwords.txt", "books")