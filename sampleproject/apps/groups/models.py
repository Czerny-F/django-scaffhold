"""
One-line Docstring.

sampleproject.apps.groups.models Docstring
sampleproject.apps.groups.models Docstring
sampleproject.apps.groups.models Docstring
"""
from django.db import models


class Category(models.Model):
    """
    Category Docstring
    カテゴリ Docstring
    Category Docstring
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    description = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    updated = models.DateTimeField(editable=False, auto_now=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.name
