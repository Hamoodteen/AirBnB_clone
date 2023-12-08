#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
to retrieve all objects from JSON file and store them in 
a dictionary(class FileStorage 's attribute).
so all objects are stored in a dictionary in class FileStorage
and can be accessed by instance of class FileStorage"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
