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