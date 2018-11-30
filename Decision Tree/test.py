def construct_new_tree(tree, routes, new_value):
    if len(routes) == 0:
        return new_value
    val = next(iter(tree.keys()))
    tmp_tree = {val:{'default': tree[val]['default'], 'values':{}}}
    for node in tree[val]['values'].items():
        if len(routes) > 0 and val == routes[0][0] and node[0] == routes[0][1]:
            routes.remove(routes[0])
            tmp_tree[val]['values'][node[0]] = construct_new_tree(node[1], routes, new_value)
        else:
            tmp_tree[val]['values'][node[0]] = tree[val]['values'][node[0]]
    return tmp_tree

a = {'A':{'default':'i','values':{'i':{'B':{'default':'x','values':{'x':{'M':{'default': 'r', 'r':'4'}}}}}, 'o':'9'}}}

r = construct_new_tree(a,[['A','i'],['B','x']],4)