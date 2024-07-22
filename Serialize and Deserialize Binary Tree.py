class Codec:

    def serialize(self, root):
        def doit(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            doit(node.left)
            doit(node.right)
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
