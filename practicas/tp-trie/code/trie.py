class Trie:
    
    root = None
    
class TrieNode:
    
    parent = None
    children = None
    key = None
    isEndOfWorld = False

def insert(T,element):
    
    if T.root.children is None:
        T.root.children = []
    
    insertR(T.root.children,None,element,0)

def insertR(list,node,str,str_index):
    
    if str_index >= len(str):
        return
    
    char = str[str_index]
    Node = searchInList(list,char)
    trieNode = None
    
    if Node != None:
        trieNode = Node
        
    if trieNode == None:
        
        
        
        
def searchInList(L,char):
    
    for i in range L:
        
        if L[i] == char:
            
            current = L[i]
            
    return current    
    
    
        