"""
time complexity of binary search tree.
        Avarage |   Worst case
Space    O(n)           O(n)
Search   O(logn)           O(n)
Insert   O(logn)           O(n)
Delete   O(logn)           O(n)
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # 挿入の時に使う関数。もし根(root)が空ならrootに、空じゃないなら_insertを呼び出して追加処理。
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    # 挿入の時にrootがからじゃなかったら呼ばれる。現在のノードの値と引数で与えられた値を比較して大きいなら右に、それ以外なら左。同値ならもうあるよ！って教えてあげる
    def _insert(self,data,cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data,cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data,cur_node.right)
        else:
            print("Value is already present in tree.")

    # 二分探索木の中に特定の値が存在するかを確認してくれる関数。存在するならTrue,存在しないならFalse。そもそもrootが存在しない場合はNoneを返す。rootがあるけど違う値の場合は_findを呼んで追加処理。
    def find(self,data):
        if self.root:
            is_found = self._find(data,self.root)
            if is_found:
                return True
            return False
        else:
            return None

    # dataとcur_nodeを比較してdataが大きいなら右に、小さいなら左に遷移するように呼び出す関数。
    def _find(self,data,cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data,cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data,cur_node.left)
        if data == cur_node.data:
            return True



bst = BST()

bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find(11))

