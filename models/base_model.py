#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttttttt"""
import uuid
import datetime
import sys
import json


class BaseModel:
    """commenttttttttttttttttttttttttttttttttttt"""
    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        """commenttttttttttttttttttttttttttttttttttt"""
        pass

    def __str__(self):
        """commenttttttttttttttttttttttttttttttttttt"""
        pass

    def save(self):
        """commenttttttttttttttttttttttttttttttttttt"""
        pass

    def to_dict(self):
        """commenttttttttttttttttttttttttttttttttttt"""
        pass
