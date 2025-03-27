#Trie implementation

class TrieNode:

    def __init__(self):
      
        # Array for children nodes of each node
        self.children = [None] * 27
        
        # for end of word
        self.isEndOfWord = False

# Method to insert a key into the Trie
    def insert(root, key):

    # Initialize the curr pointer with the root node
        curr = root

    # Iterate across the length of the string
        for c in key:

        # Check if the node exists for the 
        # current character in the Trie
            index = ord(c) - ord('a')
            if index < 0 or index > 25:
                index = 26
            if curr.children[index] is None:

            # If node for current character does 
                # not exist then make a new node
                new_node = TrieNode()

            # Keep the reference for the newly
            # created node
                curr.children[index] = new_node

        # Move the curr pointer to the
        # newly created node
            curr = curr.children[index]

    # Mark the end of the word
        curr.isEndOfWord = True

# Method to search a key in the Trie
    def search(root, key):

    # Initialize the curr pointer with the root node
        curr = root

    # Iterate across the length of the string
        for c in key:

        # Check if the node exists for the 
        # current character in the Trie
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False

        # Move the curr pointer to the 
        # already existing node for the 
        # current character
            curr = curr.children[index]

    # Return true if the word exists 
    # and is marked as ending
        return curr.isEndOfWord

    def partial_search(nav, code):
        if nav is None:
            return None
        else:
            return nav.children(code)
