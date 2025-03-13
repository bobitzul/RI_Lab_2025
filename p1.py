from bs4 import BeautifulSoup as bs

class TrieNode:
    def __init__(self):
        self.children = [None] * 27
        self.isEndOfWord = False

def insert(root, key):
    curr = root
    for c in key:
        index = ord(c) - ord('a')
        if index < 0 or index > 26:
            if curr.children[26] is None:
                new_node = TrieNode()
                curr.children[26] = new_node
            curr = curr.children[26]
        else:
            if curr.children[index] is None:
                new_node = TrieNode()
                curr.children[index] = new_node
            curr = curr.children[index]
    curr.isEndOfWord = True
def search(root, key):
    curr = root
    for c in key:
        index = ord(c) - ord('a')
        if index < 0 or index > 26:
            if curr.children[26] is None:
                return False
            curr = curr.children[26]
        else:
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
    return curr.isEndOfWord

def __main__():
    root = TrieNode()

    f = open("stopwords.txt", "r")
    stopwords_str = f.read()
    stopwords = stopwords_str.split("\n")
    ns = 0

    for s in stopwords:
        insert(root, s)

    with open("1848 - Wikipedia.html") as fp:
        site = bs(fp, 'html.parser')
    s = site.decode()
    print(s)