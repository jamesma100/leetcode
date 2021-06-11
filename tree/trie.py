'''
Trie data structure
- root node is NULL
- each node has val (if a word ending in the word has been added i.e. exists) and 
ptrs (array of <num alphabet> pointers to nodes)
- ptrs dic: <key: value> <letter: Node>
- word only "exists" if it has been added i.e. if only "word" was added, "word" is True
but "wor" is False

- Trie(): initializes trie object
- void insert(String word): inserts string word into trie
- boolean search(String word): returns true if word is in trie
- boolean startsWith(String prefix): returns true if there is a previously inserted string
word that has prefix prefix and false otherwise
'''
class Node:
    def __init__(self):
        self.val = False
        self.ptrs = {}

class True:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.ptrs:
                cur.ptrs[letter] = Node()
            cur = cur.ptrs[letter]
        cur.val = True
    
    def search(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.ptrs:
                return False
            cur = cur.ptrs[letter]
        return cur.val
    
    def startsWith(self, prefix):
        cur = self.root
        for letter in prefix:
            if letter not in cur.ptrs:
                return False
            cur = cur.ptrs[letter]
        if cur.val:
            return True
        for ptr in cur.ptrs:
            if ptr:
                return True
        return False

