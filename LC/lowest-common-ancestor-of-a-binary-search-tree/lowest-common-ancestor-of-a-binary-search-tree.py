# O(d) time | O(1) time
def lowestCommonAncestor(root, p, q):
    depth_p = get_depth(p, root)
    depth_q = get_depth(q, root)
    if depth_p > depth_q:
        backtrackAncestTree(p, q, p-q)
    else:
        backtrackAncestTree(q, p, q-p)

def get_depth(descendant, root):
    depth = 0
    while descendant != root:
        depth += 1
        descendant = descendant.parent
    return depth

def backtrackAncestTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant
