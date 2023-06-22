"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest

from src.stack import Node, Stack

class TestNode(unittest.TestCase):


    def test_node(self):
        # Пишем нужное количество проверок
        self.assertEqual(Node(5, None).data, 5)


class TestStack(unittest.TestCase):


    def test_stack(self):
        # Пишем нужное количество проверок
        stack = Stack()
        stack.push('data5')
        self.assertEqual(stack.pop(), 'data5')