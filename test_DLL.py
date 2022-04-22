from unittest import TestCase
from DLL import DoubleLL


class TestDoubleLinkedList(TestCase):
    def setUp(self):
        self.DLL = DoubleLL()

    def test_first_push(self):
        self.DLL.first_push(4)
        self.assertEqual(4, 4)
        self.DLL.output()

    def test_push_front(self):
        self.DLL.first_push(4)
        self.DLL.push_front(8)
        self.assertEqual(8, 8)
        print(self.DLL.output())

    def test_push_end(self):
        self.DLL.first_push(4)
        self.DLL.push_end(9)
        self.assertEqual(9, 9)
        print(self.DLL.output())

    def test_push_after(self):
        self.DLL.first_push(10)
        self.DLL.insert_after(10, 38)
        self.assertEqual(38, 38)
        print(self.DLL.output())

    def test_push_before(self):
        self.DLL.first_push(55)
        self.DLL.insert_after(55, 29)
        self.DLL.insert_before(29, 100)
        self.assertEqual(100, 100)
        print(self.DLL.output())

    def test_delete_end(self):
        self.DLL.first_push(1)
        self.DLL.push_end(2)
        self.DLL.push_end(3)
        print(self.DLL.output())
        self.DLL.delete_end()
        print(self.DLL.output())

    def test_delete_by_value(self):
        self.DLL.first_push(10)
        self.DLL.push_end(20)
        self.DLL.push_end(30)
        print(self.DLL.output())
        self.DLL.delete_by_value(20)
        self.assertEqual(20, 20)
        print(self.DLL.output())

    def test_reverse(self):
        self.DLL.first_push(10)
        self.DLL.push_end(20)
        self.DLL.insert_before(20, 40)
        print(self.DLL.output())
        self.DLL.reverse_list()
        self.assertEqual(self.DLL.head, self.DLL.head)
        print(self.DLL.output())

    def test_output(self):
        self.DLL.first_push(10)
        self.DLL.push_end(15)
        self.DLL.push_end(20)
        self.DLL.output()
