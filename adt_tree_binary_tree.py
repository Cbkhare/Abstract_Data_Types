from Abstract_Data_Types.adt_tree import Tree


class BinaryTree(Tree):
    """Abstract base class for Binary Tree"""

    # ----------- Abstract Methods ----------------------
    def left(self, node):
        """Return the Position representing the left child Else None"""
        raise NotImplementedError('Must be implemented by subclass')

    def right(self, node):
        """Return the Position representing the right child Else None"""
        raise NotImplementedError('Must be implemented by subclass')

    # --------- Concrete Methods  ----------------------
    def sibling(self, node):
        """Return the Position representing the nodes sibling, None if there is
        no sibling or if it is the parent"""

        parent = self.parent(node)
        if parent is None:
            return None
        else:
            if node == self.left(parent):
                # The node is the left child of the parent
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, node):
        """Return Left and Right child's Position, None if there is no child"""
        if self.left(node) is not None:
            yield self.left(node)
        if self.right(node) is not None:
            yield self.right(node)
