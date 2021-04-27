"""Anything whose name may change should be in an enum rather than hard-coded."""
# Python imports
from enum import Enum


class TableName(Enum):
    """Names of tables in MySQL database"""
    employee = 'employee'
    department = 'department'
    job = 'job'
