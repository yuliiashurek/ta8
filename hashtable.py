import time

from additional.RedBlackTree import MyRedBlackTree
from adress import *

class HashTableBT:
    def __init__(self):
        self.storage = MyRedBlackTree()

    def insert(self, key_adress: adress, value):
        data = key_adress.generate_hashcode()
        node = self.storage.contains_node(data)
        if node is not None:
            node.key_value_pairs_list.append([key_adress, value])
        else:
            self.storage.insert(data, [key_adress, value])

    def contain(self, key_adress: adress):
        node = self.storage.contains_node(key_adress.generate_hashcode())
        if node is not None:
            person_list = node.key_value_pairs_list
            node = person_list.head
            if node.data[0] is key_adress:
                return True
            while node.next_element is not None:
                if node.data[0] is key_adress:
                    return True
                node = node.next_element
        return False
