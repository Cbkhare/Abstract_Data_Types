from Abstract_Data_Types.adt_tree_binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = ('_elements', '_parent', '_left', '_right')
        def __init__(self, element=None, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An Abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by user"""

            self._container = container
            self._node = node

        def element(self):
            """return the element stored stored at this position"""

            return self._node._element

        def __eq__(self,other):
            """Return True if other is a Position representing the same
            location"""

            return type(other) is type(self) and other._node is self._node

    def _validate(self, pos):
        """Return associated node, if position is valid."""

        if not isinstance(pos, self.Position):
            raise TypeError("node must be proper position type")

        if pos._container is not self:
            raise ValueError("node does not belong to this container")

        if pos._node._parent is pos._node:  # convention for deprecated nodes
            raise ValueError("node is no longer valied")

        return pos._node

    def _make_position(self, pos):
        """Return Position instance for given node (or None if no node)"""

        return self.Position(self, pos) if pos else None

    # -------------------------- binary tree constructor -----------------------

    def __init__(self):
        """Create an empty binary tree"""
        self._root = None
        self._size = 0

    # -------------------------- public accessors --------------------------
    def __len__(self):
        """Return total number of element in the Tree"""
        return self._size

    def root(self):
        """Return the Root position of tree ( or None if tree is empty)."""
        return self._make_position(self.root)

    def parent(self, pos):
        """Return the position of nodes parent else None if node is root"""
        node = self._validate(pos)
        return self.Position(node._parent)

    def left(self, pos):
        """Return the position of Left child of the node else None"""
        node = self._validate(pos)
        return self._make_position(node._left)

    def right(self, pos):
        """Return the position of the Right child of the node else None """
        node = self._validate(pos)
        return  self._make_position(node._right)

    def num_children(self, pos):
        """Return the number of children node at pos have"""
        node = self._validate(pos)
        count = 0
        if node.left:   count +=1
        if node.right:  count +=1
        return count

    def _add_root(self, elem):
        """Place element elem at the root of the tree and Return New Position
        if root already exist raise Value Error"""

        if self._root:
            raise ValueError(" Root Already exist")
        self._size = 1
        self._root = self._Node(elem)
        return self._make_position(self._root)

    def _add_left_(self, pos, elem):
        """Add left child for the position pos with element elem, Return the
        position of newly created node

        raise ValueError if position pos has already a left child"""

        node = self._validate(pos)
        if node._left:  raise ValueError('Left Child Already exists')
        self._size += 1
        node._left = self._Node(element=elem, parent=node)
        return self._make_position(node._left)

    def _add_right(self, pos, elem):
        """Add right child for the position pos with element elem, Return the
        position of newly created node

        raise ValueError if position pos has already a right child"""

        node = self._validate(pos)
        if node._right:  raise ValueError('Right Child Already exists')
        self._size += 1
        node._right = self._Node(element=elem, parent=node)
        return self._make_position(node._right)

    def _replace(self, pos, new_elem):
        """Replace old element with new element"""
        node = self._validate(pos)
        if not node:
            raise ValueError('Position doesnot exists')
        old_elem = node._element
        node._element = new_elem
        return old_elem

    def _delete(self, pos):
        """Delete the node at the position pos and replace it with its child, if
        any.
        Return the element that has been delete
        Raise ValueError if pos is not valid or node has two children"""

        node = self._validate(pos)
        if self.num_children(pos) > 1:
            raise ValueError("Multiple child exists")
        child = node._right if node._right else node._left

        # Changing parentship
        if child is not None:
            child._parent = node._parent

        # Changing off-springs
        if node is self._root:
            self.root = child
        else:
            node_parent = self._validate(pos._parent)
            if node == node_parent._left:
                node_parent._left = child
            else:
                node_parent._right = child
        self._size -=1
        node.parent = node       # This fails during validation
        return node._element

    def _attach(self, pos, tree1, tree2):
        """Attach trees tree1 and tree2 as left and right child for position pos
        """

        node = self._validate(pos)
        if not self.is_leaf(node):
            raise ValueError("Position must be a leaf")

        if not type(self) is type(tree1) is type(tree2):
            raise TypeError("Trees type must match")

        # len will get value from self._size
        self._size = len(tree1) + len(tree2)

        if not tree1.is_empty():
            tree1._root._parent = node
            node._left = tree1
            tree1._root = None
            tree1._size = 0

        if not tree2.is_empty():
            tree2._root._parent = node
            node._left = tree2
            tree2._root = None
            tree2._size = 0
