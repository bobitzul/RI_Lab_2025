from trie import *
from b_plus import *
import queue
import requests

Q = queue.Queue(100)
Q.put('https://www.robotstxt.org')



while not Q.empty() or not Q.full():
    L = Q.get()
    if L:
        continue
    P = requests.get(L)
    if P:
        continue