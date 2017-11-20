class Tree(object):
    """Abstract class for Tree"""

    class Position:
        """Abstraction to location the position of single element"""

        def element(self):
            """return the element stored at this position"""
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other):
            """returns True if position represents the same location"""
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            """return True id position doesn not represent the same location"""
            return not (self == other)

    # ------------ Abstract methods to be Implemented by concrete subclasses --
    def root(self):
        """Return the position representing the root else None if empty"""
        raise NotImplementedError('Must be implemented by subclass')

    def parent(self, node):
        """Return the position node representing the node's parent Else None"""
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, node):
        """Return the number of child that position node have"""
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, node):
        """Generate an iteration of Positions representing node's children"""
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        """Return the total number of nodes in the tree"""
        raise NotImplementedError('Must be implemented by subclass')

    # ------------ concrete methods to be Implemented in this class -----------
    def is_root(self, node):
        """Return True if Position node represents the root of the
        tree"""
        return self.root() == node

    def is_leaf(self, node):
        """Return True if Position node does not have any children"""
        return self.num_children(node) == 0

    def is_empty(self):
        """Return True if tree is empty"""
        return self.__len__() == 0

    def depth(self, node):
        """Return the depth of a node present at Position"""
        if self.is_leaf(node):
            return 0
        else:
            return 1 + self.depth(self.parent(node))

    def height(self, node):
        """Return the height of a node present at Position"""
        if self.is_root(node):
            return 0
        else:
            return 1 + max(self.height(child_node) for child_node in
                           self.children(node))
