# coding: utf-8

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def myPrint(self):
        print self.val
        if self.next:
            self.next.myPrint()


class Solution(object):

    def add_two_numbers(self, l1, l2):
        result = ListNode(0)
        cur = result
        while l1 or l2:
            cur.val += self.add_two_nodes(l1, l2)
            if cur.val >= 10:
                cur.val -= 10
                cur.next = ListNode(1)
            else:
                if l1 and l1.next or l2 and l2.next:
                    cur.next = ListNode(0)

            cur = cur.next
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return result


    def add_two_nodes(self, n1, n2):
        if not n1 and not n2:
            pass

        if not n1:
            return n2.val

        if not n2:
            return n1.val

        return n1.val + n2.val



# l1 = ListNode(8)
# l1.next = ListNode(9)
# l1.next.next = ListNode(10)
if __name__ == "__main__":
    list = ListNode(9)
    list.next = ListNode(8)
    print(Solution().add_two_numbers(list, ListNode(1)).myPrint())