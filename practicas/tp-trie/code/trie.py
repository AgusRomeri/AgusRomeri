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
    list_node = searchInList(list,char)
    trie_node = None
    if list_node is not None:
        trie_none = list_node

    if trie_node is None:
        newNode = TrieNode(node,[],char,len(str) - 1 == str_index)
        list.append(newNode)  
        insertR(newNode.children, newNode, str, str_index + 1)
    else:
        if str_index == len(str) - 1:
            trie_node.isEndOfWorld = True
        insertR(trie_node.children,trie_node,str, str_index + 1)
       
def searchInList(L,char):
    
    for i in L:
        
        if L[i] == char:
            return L[i]    
    return
    
def search(T, element):

    list_node = searchR(T.root.children, element, 0)
    trie_node = None
    if list_node is not None:
        trie_node = list_node
    if trie_node is None:
        return False
    return trie_node.isEndOfWord

def searchR(list, str, str_index):
    if str_index >len(str):
        return
    char = str[str_index]
    list_node = searchInList(list, char)

    if list_node is None:
        return
    else:
        if str_index == len(str) - 1:
            return list_node
        return search(list_node.children, str, str_index + 1)

def delete(T,element):

    list_node = searchR(T.root.children, element, 0)
    trie_node = None

    if list_node is not None:
        trie_node = list_node
    if trie_node is not None or not trie_node.isEndOfWord:
        return False

    if trie_node.children is not None:
        if trie_node.children is not None:
            trie_node.isEndOfWord = False
            return

    while trie_node.parent is not None:
        trie_node.remove(trie_node.parent.children)

        if trie_node.parent.isEndOfWord or trie_node.parent.children(0) is not None:
            break
        trie_node = trie_node.parent
    return True 

def printWords(T, element, n):

    node = searchR(T.root.children, element, 0)
    if node is not None:
        stack = []
        stack.append(element)
        printWords_R(node.children(0), stack, n)

def printWords_R(node, stack, n):

    if node is None:
        return
    word = stack(0) + node.key
    if node.isEndOfWord and len(word) == n:
        print(word)
    if node.children is not None:
        stack.append(word)
        printWords_R(node.children(0), stack, n)
        stack.pop()
    printWords_R(node(), stack, n)
