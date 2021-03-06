# _*_ coding: utf-8 _*_

"""
util_fetch.py by xianhu
"""

import re
import sys
import traceback

__all__ = [
    "extract_error_info",
    "parse_error_info",
]


def extract_error_info():
    """
    extract error information from exception, return a string
    """
    _type, _value, _traceback = sys.exc_info()
    tb_list = traceback.extract_tb(_traceback)
    error_info = "-->".join(["【filename=%s, line=%s, function=%s】" % (tb.filename, tb.lineno, tb.name) for tb in tb_list])
    return "error_info=%s, error_type=%s, error=%s" % (error_info, _type, _value)


def parse_error_info(line):
    """
    parse error information based on CONFIG_***_MESSAGE, return a tuple(priority, keys, deep, url)
    """
    regu = re.search(r"priority=(?P<priority>\d+?),\s*?keys=(?P<keys>.+?),\s*?deep=(?P<deep>\d+?),\s*?(repeat=\d+,)?\s*?url=(?P<url>.+?)$", line)
    return int(regu.group("priority")), eval(regu.group("keys").strip()), int(regu.group("deep")), regu.group("url").strip()
