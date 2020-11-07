# Group: Yannik Suhre, Doyeon Kim, Yue Hou, Zhongzhou Yang
from classes import Student, Node, Time_complexity, BST
from sorting_algorithms import reduce, merge_sort

if __name__ == '__main__':
    bst = BST()
    bm = Time_complexity()
    bst_get = bm.time_complexity_get(bst.create_tree, Node.get, "student_id")
    print(bst_get)
    bm.plot()
