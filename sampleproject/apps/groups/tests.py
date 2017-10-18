from django.test import TestCase
import unittest
from .models import Category, Section, Group


class CategoryModelTests(TestCase):

    def test_str(self):
        category = Category(name="foo")
        self.assertEqual('foo', str(category))

    def test_str2(self):
        category = Category(name="foo")
        self.assertEqual('foo', category.str())


class SectionModelTests(unittest.TestCase):

    def setUp(self):
        self.super = Category.objects.create(name="hoge")
        self.obj = Section.objects

    def test_str(self):
        section = self.obj.create(name="foo", category=self.super)
        self.assertEqual('foo', str(section))


class GroupModelTests(unittest.TestCase):

    def setUp(self):
        self.super = Category.objects.create(name="hoge")
        self.section = Section.objects.create(name="foo", category=self.super)
        self.obj = Group.objects

    def test_str(self):
        group = self.obj.create(name="bar", section=self.section)
        self.assertEqual('bar', str(group))
