class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.isEndOfWord = True

def findWords(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    rows, cols = len(board), len(board[0])
    result, visited = set(), set()
    
    def dfs(r, c, node, path):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] not in node.children:
            return
        visited.add((r, c))
        node = node.children[board[r][c]]
        path += board[r][c]
        if node.isEndOfWord:
            result.add(path)
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(r + dr, c + dc, node, path)
        visited.remove((r, c))
    
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root, "")
    
    return list(result)
