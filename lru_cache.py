# coding: utf-8
"""
设计并实现一个支持近期最少使用缓存的数据结构。要支持存和取两个操作。根据键取值时，如果键对应的值不存在，则返回-1。存键值对时，如果容量已经满了，
要把最近最少使用的键值对去除后再插入。

解题思路

首先明确最少使用缓存是指我们要缓存最近使用的数据，如果一个数据长时间没有使用，且又有新的数据加入，那么应该将最长时间没有使用的数据去除。
为此我们可以通过一个双向链表完成这样的数据结构，表头表示最近使用过的数据，越接近表尾表示越久没有使用过。
当要将旧数据删除时，我们只需要将链表尾部的节点去除，并在头部插入新的节点。而更新节点时，我们只需要将原来的节点删除，改变节点的内容，
再插入到链表头部。而最简单的插入，即还没有达到容量上限时，我们只要在头部直接插入。
我们知道链表的查找操作速度较慢，为了提高查找的速度，我们可以通过一个键值对的字典来记录数据。查找时先判断是否在字典中，
如果在则需要更新节点的使用情况并返回结果，如果不在则直接返回-1。这样插入数据时也可以通过字典来判断是首次插入还是数据的更新。
"""
class LRUCache(object):

    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev, self.next = None, None

    def __init__(self, capacity):

        self.capacity, self.size = capacity, 0
        self.cache = {}
        self.head, self.tail = self.Node(-1, -1), self.Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def __remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next =None

    def __insert(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.__remove(node)
        self.__insert(node)
        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.__remove(node)
            node.value = value
            self.__insert(node)
        else:
            if self.size == self.capacity:
                discard = self.tail.prev
                self.__remove(discard)
                del self.cache[discard.key]
            node = self.Node(key, value)
            self.cache[key] = node
            self.__insert(node)
            self.size += 1

if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.set(1, 1)
    lru_cache.set(2, 2)
    lru_cache.set(3, 3)
    assert lru_cache.get(0) == -1
    assert lru_cache.get(1) == 1
    lru_cache.set(1, 10)
    assert lru_cache.get(1) == 10
    lru_cache.set(4, 4)
    assert lru_cache.get(2) == -1