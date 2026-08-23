class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode() for _ in range(1000)]

    def get_hash(self, key):
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        hash = self.get_hash(key)
        curr = self.hashmap[hash]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            
            curr = curr.next
        
        curr.next = ListNode(key, value)


    def get(self, key: int) -> int:
        hash = self.get_hash(key)
        curr = self.hashmap[hash] # curr.next becasue curr is dummy node
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            
            curr = curr.next
        
        return -1
        

    def remove(self, key: int) -> None:
        hash = self.get_hash(key)
        curr = self.hashmap[hash]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            
            curr = curr.next
        
