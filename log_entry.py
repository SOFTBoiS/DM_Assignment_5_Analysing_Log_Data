from enum import Enum

# Level = Enum('Information', 'Warning', 'Error')


class LogEntry:

    def __init__(self, level, system, instance, action, timestamp):
        self.level = level
        self.system = system
        self.instance = instance
        self.action = action
        self.timestamp = timestamp
