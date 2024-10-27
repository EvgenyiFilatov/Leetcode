"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
            self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        # Проход по обоим спискам, пока есть элементы в обоих
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # добавляем узел list1
                list1 = list1.next    # перемещаемся к следующему узлу в list1
            else:
                current.next = list2  # добавляем узел list2
                list2 = list2.next    # перемещаемся к следующему узлу в list2
            # перемещаемся к следующему узлу в результирующем списке
            current = current.next
        # Если у одного из списков остались элементы, добавляем их
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Возвращаем начальный узел результирующего списка
        return dummy.next


# Определение узлов списка
def create_linked_list(values):
    head = ListNode()
    current = head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return head.next


# Создание двух списков
list1_values = [1, 2, 4]
list2_values = [1, 3, 4]

list1 = create_linked_list(list1_values)
list2 = create_linked_list(list2_values)

# Вызов метода
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)


# Функция для печати связанного списка
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=", ")
        current = current.next
    print("None")


# Печать результата
print_linked_list(merged_list)
