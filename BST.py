class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class BST:
        def __init__(self):
            self.root=None
        #insert
        def insert(self,root,key):
            if root is None:
                return Node(key)
            if key<root.data:
                root.left=self.insert(root.left, key)
            elif key> root.data:
                root.right=self.insert(root.right,key)
            return root
        
        #search
        def search(self,root,key):
            if root is None:
                return False
            if root.data == key:
                return True
            if key < root.data:
                return self.search(root.left, key)
            return self.search(root.right, key)
        
        #inorder traversal
        def inorder(self, root):
            if root:
                self.inorder(root.left)
                print(root.data, end=" ")
                self.inorder(root.right)
        
        #preorder traversal
        def preorder(self,root):
            if root:
                print(root.data,end=" ")
                self.preorder(root.left)
                self.preorder(root.right)
        

        #postorder traversal
        def postorder(self, root):
            if root:
                self.postorder(root.left)
                self.postorder(root.right)
                print(root.data,end=" ")
        #find min
        def find_min(self,root):
            while root.left:
                root=root.left
            return(root)
        #find max
        def find_max(self,root):
            while root.right:
                root=root.right
            return(root)

bst = BST()
values = [13,6,9,4,7,10,20,15]

# Build the tree
for value in values:
    bst.root = bst.insert(bst.root, value)

# Print traversals
print("Inorder traversal: ", end="")
bst.inorder(bst.root)
print()

print("Preorder traversal: ", end="")
bst.preorder(bst.root)
print()
print("Postorder traversal: ", end="")
bst.postorder(bst.root)
print()
print("Minimimum value:",end=" ")
bst.find_min(root)
print()


        
       

