class AVLtree:
    root = None
    
class AVLNode:
    
    parent = None
    leftnode = None
    rightNode = None
    key = None
    value = None
    balance_factor = None
    height = None
    
def search(tree,element):
    
    node = searchNodeR(tree.root,element)
    
    if node == None:
        return
    else:
        return node.key
    
#Funcion search recursiva
def searchNodeR(node,element):
    
    if node == None:
        return
    
    if node.value==element:
        return node
    
    right = searchNodeR(node.rightnode,element)
    if right != None:
        return right

    left = searchNodeR(node.leftnode, element)
    if left != None:
        return left

def searchNode(B,element):
    return searchNodeR(B.root,element)

def insert(tree, element, key):
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element

    if (tree.root == None):
        tree.root = newNode
        return newNode
    return insertR(tree, newNode, tree.root)

#Funcion insert recursiva
def insertR(tree, newNode, currentNode):
    
    if newNode.key > currentNode.key:
        if currentNode.rightnode == None:
            newNode.parent = currentNode
            currentNode.rightnode = newNode
            update_bf_ancestors(tree, newNode)
            return newNode
        else:
            right = insertR(tree, newNode, currentNode.rightnode)
            if right != None:
                return right        
    else:
        
        if currentNode.leftnode == None:
            newNode.parent = currentNode
            currentNode.leftnode = newNode
            update_bf_ancestors(tree, newNode)
            return newNode
        else:
            left = insertR(tree, newNode, currentNode.leftnode)
            if left != None:
                return left
def update_bf_ancestors(tree, node):
    while node is not None:
        calculate_bf(node)
        if node.balanceFactor < -1 or node.balanceFactor > 1:
            balance(tree, node)
        node = node.parent
        
def delete(tree,element):
    
    node = searchNode(tree,element)
    if node == None:
        return
    else:
        return deleteCurrentCase(tree,node)
    
def deleteCurrentCase(tree,node):
    
    if node.rightnode == None:
        if node.leftnode == None:

            # Caso 1: El nodo a eliminar es una hoja
            if node.parent.leftnode != None and node.parent.leftnode == node:
                node.parent.leftnode = None
                update_bf_ancestors(tree, node)
                return node.key
            elif node.parent.rightnode != None and node.parent.rightnode == node:
                node.parent.rightnode = None
                update_bf_ancestors(tree, node)
                return node.key

        # Caso 2: El nodo a eliminar tiene un hijo del lado izquierdo
        if node.parent.leftnode != None and node.parent.leftnode == node:
            node.parent.leftnode = node.leftnode
            update_bf_ancestors(tree, node)
            return node.key
        elif node.parent.rightnode != None and node.parent.rightnode == node:
            node.parent.rightnode = node.leftnode
            update_bf_ancestors(tree, node)
            return node.key
    else:
        # Caso 2: El nodo a eliminar tiene un hijo del lado derecho
        if node.leftnode == None:
            if node.parent.leftnode == node:
                node.parent.leftnode = node.rightnode
                update_bf_ancestors(tree, node)
                return node.key
            elif node.parent.rightnode == node:
                node.parent.rightnode = node.rightnode
                update_bf_ancestors(tree, node)
                return node.key
        else:		
			# Caso 3: El nodo a eliminar tiene dos hijos
            changeNode = bigger(node.leftnode)
            node.value = changeNode.value
            oldKey = node.key
            node.key = changeNode.key
            deleteCurrentCase(tree, changeNode)
            update_bf_ancestors(tree, node)
            return oldKey

def smaller(node):
    if node.leftnode != None:
        current = smaller(node.leftnode)
        if current != None:
            return current
    else:
        return node
def bigger(node):
    if node.rightnode != None:
        current = bigger(node.rightnode)
        if current != None:
            return current
    else:
        return node

def deleteKey(tree,key):
    
    node = searchKeyR(tree.root,key)
    if node == None:
        return
    else:
        return deleteCurrentCase(tree,node)

def searchKeyR(node,key):
    
    if node == None:
        return
    
    if node.key == key:
        return node
    
    right = searchKeyR(node.rightnode, key)
    if right != None:
        return right

    left = searchKeyR(node.leftnode, key)
    if left != None:
        return left
def access(tree,key):
    
    node = searchKeyR(tree.root,key)
    if node == None:
        return
    else:
        return node.value
    
def update(tree,element,key):
    
    node = searchKeyR(tree.root,key)
    if node == None:
        return
    else:
        node.value = element
        return node.key

def rotateLeft(tree,avlnode):
    
    newroot = avlnode.rightnode
    avlnode.rightnode = newroot.leftnode
    
    if newroot.leftnode != None:
        newroot.leftnode.parent = avlnode
    newroot.parent = avlnode.parent
    
    if avlnode.parent == None:
        
        tree.root = newroot    
    elif avlnode.parent.leftnode == avlnode:
        
        avlnode.parent.leftnode == newroot
    else:
        
        avlnode.parent.rightnode = newroot
    
    newroot.leftnode = avlnode
    avlnode.parent = newroot

def rotateRight(tree,avlnode):
    
    newroot = avlnode.leftnode
    avlnode.leftnode = newroot.rightnode
    
    if newroot.rightnode != None:
        
        newroot.righnode.parent = avlnode
    
    newroot.parent = avlnode.parent
    
    if avlnode.parent == None:
        
        tree.root = newroot    
    elif avlnode.parent.rightnode == avlnode:
        
        avlnode.parent.rightnode == newroot
    else:
        
        avlnode.parent.leftnode = newroot
    
    newroot.rightnode = avlnode
    avlnode.parent = newroot

def balance(tree, node):
    if node is not None:
        balance(tree, node.leftnode)
        balance(tree, node.rightnode)
        calculate_bf(node)

        if node.balanceFactor < -1:
            calculate_bf(node.rightnode)
            if node.rightnode.balanceFactor == 1:
                rotateRight(tree, node.rightnode)
                rotateLeft(tree, node)
            else:
                rotateLeft(tree, node)
        elif node.balanceFactor > 1:
            calculate_bf(node.leftnode)
            if node.leftnode.balanceFactor == -1:
                rotateLeft(tree, node.leftnode)
                rotateRight(tree, node)
            else:
                rotateRight(tree, node)
    return tree

def calculate_bf(node):
    update_height(node)
    if node.leftnode is not None and node.rightnode is not None:
        node.balanceFactor = node.leftnode.height - node.rightnode.height
    elif node.rightnode is not None:
        node.balanceFactor = -node.height
    else:
        node.balanceFactor = node.height

def update_height(node):
    if node is not None:
        update_height(node.leftnode)
        update_height(node.rightnode)
        if node.leftnode is not None and node.rightnode is not None:
            node.height = 1 + max(node.leftnode.height, node.rightnode.height)
        elif node.leftnode is not None:
            node.height = 1 + node.leftnode.height
        elif node.rightnode is not None:
            node.height = 1 + node.rightnode.height
        else:
            node.height = 0