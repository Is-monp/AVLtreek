from collections import deque
import re
import os
import graphviz as gv

class TreeNode:
    def __init__(self, key, fileType, fileSize):
        self.key = key
        self.fileType = fileType
        self.fileSize = fileSize
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    AVLTree class represents an AVL (Adelson-Velsky and Landis) tree data structure.
    It supports operations like insertion, deletion, and level order traversal.
    """

    def getHeight(self, node):
        """
        Returns the height of the given node.

        Parameters:
        - node: The node for which to calculate the height.

        Returns:
        The height of the node.
        """
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        """
        Returns the balance factor of the given node.

        Parameters:
        - node: The node for which to calculate the balance factor.

        Returns:
        The balance factor of the node.
        """
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rightRotate(self, y):
        """
        Performs a right rotation on the given node.

        Parameters:
        - y: The node to perform the right rotation on.

        Returns:
        The new root node after the rotation.
        """
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def leftRotate(self, x):
        """
        Performs a left rotation on the given node.

        Parameters:
        - x: The node to perform the left rotation on.

        Returns:
        The new root node after the rotation.
        """
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y


    def minValueNode(self, node):
        """
        Finds the node with the minimum key value in the given subtree.

        Parameters:
        - node: The root node of the subtree.

        Returns:
        The node with the minimum key value.
        """
        current = node

        while current.left:
            current = current.left

        return current
    
    def search(self, root, key):
        """
        Searches for a node with the given key in the AVL tree.

        Parameters:
        - root: The root node of the AVL tree.
        - key: The key value to search for.

        Returns:
        The node with the given key, or None if not found.
        """
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def printLevelOrder(self, root):
        """
        Prints the nodes of the AVL tree in level order traversal.

        Parameters:
        - root: The root node of the AVL tree.
        """
        if not root:
            return

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            print(node.key, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    # Create a getLevelOrder method that works exactly equal but returning a string
    def getLevelOrder(self, root):
        if not root:
            return ""

        queue = deque()
        queue.append(root)
        levelOrder = ""

        while queue:
            node = queue.popleft()
            levelOrder += f"{node.key} "

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return levelOrder
    # Get the double-rotations functions
    def doubleRotateLeft(self, root):
        root.left = self.leftRotate(root.left)
        return self.rightRotate(root)
    
    def doubleRotateRight(self, root):
        root.right = self.rightRotate(root.right)
        return self.leftRotate(root)
    
    def maxValueNode(self, node):
        current = node
        while current.right:
            current = current.right
        return current
    
    # A function that deletes a node with a given key from the AVL tree
    def delete(self, root, key):
        if not root:
            return root
        
        # Buscar la clave en el subárbol izquierdo
        if key < root.key:
            root.left = self.delete(root.left, key)
        
        # Buscar la clave en el subárbol derecho
        elif key > root.key:
            root.right = self.delete(root.right, key)
        
        # Si se encuentra la clave
        else:
            # Caso 1: El nodo tiene 0 o 1 hijo
            if not root.left or not root.right:
                temp = root.left if root.left else root.right
                if not temp:
                    temp = root
                    root = None
                else:
                    root = temp
            
            # Caso 2: El nodo tiene 2 hijos
            else:
                temp = self.maxValueNode(root.left)  # Encontrar el mayor del subárbol izquierdo
                root.key = temp.key
                root.left = self.delete(root.left, temp.key)
        
        # Si el nodo se eliminó, o no había nada que eliminar, se devuelve el nodo
        if not root:
            return root
        
        # Recalcular la altura del nodo actual
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        # Calcular el balance del árbol
        balance = self.getBalance(root)
        
        # Restaurar el equilibrio del árbol si es necesario
        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                return self.doubleRotateLeft(root)
        if balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                return self.doubleRotateRight(root)
        
        return root
    
    def verifyFileName(self, fileName):
        fileTypes = {
            "bike": r"bike_[0-3][0-9][0-9]",
            "cars": r"carsgraz_[0-4][0-9][0-9]",
            "cats": r"cat\.[1-9][0-9]?[0-9]?",
            "dogs": r"dog\.[1-9][0-9]?[0-9]?",
            "flowers": r"0[0-2][0-9][0-9]",
            "horses": r"horse-[1-9][0-9]?[0-9]?",
            "human": r"rider-[1-9][0-9]?[0-9]?"
        }
        for key, value in fileTypes.items():
            if re.fullmatch(value, fileName):
                return key
        return None
    
    def getFileRoute(self, fileName):
        masterFolder=self.verifyFileName(fileName)
        if not masterFolder:
            return None
        extensions={
            "bike": "bmp",
            "cars": "bmp",
            "cats": "jpg",
            "dogs": "jpg",
            "flowers": "png",
            "horses": "jpg",
            "human": "jpg"
        }
        extension=extensions[masterFolder][0:3]
        fileRoute=f"./data/{masterFolder}/{fileName}.{extension}"
        return fileRoute
    
    def verifyFileExists(self, fileName):
        fileRoute=self.getFileRoute(fileName)
        if not fileRoute:
            return False
        return os.path.exists(fileRoute)
    
    def getFileSize(self, fileName):
        fileRoute = self.getFileRoute(fileName)
        if not fileRoute:
            return None
        return os.path.getsize(fileRoute)
    
    # Using the above functions insert a node, verify first if 
    # the file exists and if it does, then insert the node
    # with the size and type included, use the key
    # as the file name
    def insert(self, root, key):
        fileType=self.verifyFileName(key)
        if not fileType:
            return None
        fileSize=self.getFileSize(key)
        if not fileSize:
            return None
        return self.insertNode(root, key, fileType, fileSize)
    
    def insertNode(self, root, key, fileType, fileSize):
        if not root:
            return TreeNode(key, fileType, fileSize)
        
        if key < root.key:
            root.left = self.insertNode(root.left, key, fileType, fileSize)
        else:
            root.right = self.insertNode(root.right, key, fileType, fileSize)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        balance = self.getBalance(root)
        
        if balance > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                return self.doubleRotateLeft(root)
        if balance < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                return self.doubleRotateRight(root)
        
        return root
    
    # A function that gets the father of a given node
    def getFather(self, root, key):
        if not root:
            return None
        if (root.left and root.left.key == key) or (root.right and root.right.key == key):
            return root
        if key < root.key:
            return self.getFather(root.left, key)
        return self.getFather(root.right, key)
    
    # A function that gets the grandfather of a given node
    def getGrandFather(self, root, key):
        father=self.getFather(root, key)
        if not father:
            return None
        return self.getFather(root, father.key)
    
    # A function that gets the siblings of a node
    def getSiblings(self, root, key):
        father=self.getFather(root, key)
        if not father:
            return None
        if father.left and father.left.key==key:
            return father.right
        return father.left
    
    # A function that gets the uncle of a node
    def getUncle(self, root, key):
        father=self.getFather(root, key)
        if not father:
            return None
        return self.getSiblings(root, father.key)
    
    # A function that gets the level of a node
    def getLevel(self, root, key):
        if not root:
            return None
        if root.key==key:
            return 0
        if key < root.key:
            return 1 + self.getLevel(root.left, key)
        return 1 + self.getLevel(root.right, key)
    
    # A function named getRelatives that returns the father, grandfather and uncle of a given node
    def getRelatives(self, root, key):
        father=self.getFather(root, key)
        grandFather=self.getGrandFather(root, key)
        uncle=self.getUncle(root, key)
        # return father.key, grandFather.key, uncle.key
        # if they have key
        if father:
            father=father.key
        if grandFather:
            grandFather=grandFather.key
        if uncle:
            uncle=uncle.key
        return father, grandFather, uncle
    
    # A function named getInfo that takes a node and returns
    # a list with [key, level, balance, father, grandfather, uncle]
    def getInfo(self, root, node):
        key=node.key
        level=self.getLevel(root, key)
        balance=self.getBalance(self.search(root, key))
        father, grandFather, uncle=self.getRelatives(root, key)
        return [key, level, balance, father, grandFather, uncle]
    
    # A function that receives a type and a 
    # size range and returns a list with all the nodes that
    # fit into that filter
    def filter(self, root, fileType, minSize, maxSize):
        if not root:
            return []
        nodes=[]
        if root.fileType==fileType and minSize<=root.fileSize<=maxSize:
            nodes.append(root)
        nodes+=self.filter(root.left, fileType, minSize, maxSize)
        nodes+=self.filter(root.right, fileType, minSize, maxSize)
        return nodes
    
    def getInfos(self, root, fileType, minSize, maxSize):
        nodes=self.filter(root, fileType, minSize, maxSize)
        infos=[]
        for node in nodes:
            infos.append(self.getInfo(root, node))
        return infos
    
    # A function to output the tree using graphviz
    # to the current folder using output.png
    def outputTree(self, root):
        if not root:
            return
        dot = gv.Digraph()
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            dot.node(node.key, label=f"{node.key}")
            if node.left:
                dot.edge(node.key, node.left.key)
                queue.append(node.left)
            if node.right:
                dot.edge(node.key, node.right.key)
                queue.append(node.right)
        dot.render("output", format="png", view=True)
    

    

# Ejemplo de uso
if __name__ == "__main__":
    myTree = AVLTree()
    root = None

    root = myTree.insert(root, "rider-1")
    root = myTree.insert(root, "horse-1")
    root = myTree.insert(root, "0001")
    root = myTree.insert(root, "dog.1")
    root = myTree.insert(root, "cat.1")
    root = myTree.insert(root, "carsgraz_001")
    root = myTree.insert(root, "bike_001")
    root = myTree.insert(root, "0002")
    root = myTree.insert(root, "bike_002")
    root = myTree.insert(root, "cat.2")

    print("Level order traversal of the constructed AVL tree is")
    print(myTree.printLevelOrder(root))
    print()
    root = myTree.delete(root, "cat.1")
    print(myTree.printLevelOrder(root))
