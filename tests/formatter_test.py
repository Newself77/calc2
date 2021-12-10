"""Test Unix Formatter"""
from datetime import datetime
from collections import namedtuple
import time
from calc.calculations.logger import UnixFormatter


def test_unix_format_time():
    """Testing unix format timestamp"""
    fmt = UnixFormatter()
    record = namedtuple("FakeRecord", ["created"])(time.time())
    timestamp = datetime.fromtimestamp(record.created)
    timestamp = datetime(*timestamp.timetuple()[:6]).timestamp()
    assert str(timestamp) == fmt.formatTime(record)
