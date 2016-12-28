#!/usr/bin/env python3
#binaryrecordfile_ans.py

"""
>>> import shutil
>>> import sys

>>> S = struct.Struct("<15s")
>>> fileA = os.path.join(tempfile.gettempdir(), "fileA.dat")
>>> fileB = os.path.join(tempfile.gettempdir(), "fileB.dat")
>>> for name in (fileA, fileB):
...     try:
...         os.remove(name)
...     except EnvironmentError:
...         pass

>>> brf = BinaryRecordFile(fileA, S.size)
>>> for text in ("Alpha", "Bravo", "Charlie", "Delta", "Echo"
...         "Foxtrot", "Golf", "Hotel", "India", "Juliet", 
...         "Kilo", "Lima", "Mike", "November", "Oscar", 
...         "Papa", "Quebec", "Romeo", "Sierra", "Tango", 
...         "Uniform", "Victor", "Whisky", "XRay", "Yankee", "Zulu"):
...     brf.append(S.pack(text.encode("utf8")))
>>> assert len(brf) == 26
>>> brf.append(S.pack(b"Extra at the end"))
>>> assert len(brf) == 27
>>> shutil.copy(fileA, fileB)
>>> del brf[12]
>>> del brf[0]
>>> del brf[24]
>>> assert len(brf) == 24, len(brf
>>> brf.close()

>>> if ((os.path.getsize(fileA) + (3 * S.size)) != os.path.getsize(fileB)):
...     print("FAIL#1: expected file sizes are wrong")
...     sys.exit()


>>> shutil.copy(fileB, fileA)
>>> if os.path.getsize(fileA) != os.path.getsize(fileB):
...     print("FAIL#2: expected file sizes differ")
...     sys.exit()

>>> for name in (fileA, fileB):
...     try:
...         os.remove(name)
...     except EnvironmentError:
...         pass
"""

import os
import struct 
import tempfile


_DELETED = b"\x01"
_OKAY = b"\x02"


class BinaryRecordFile:

    def __init__(self, filename, record_size, auto_flush=True):
        """A random access binary file that behaves like a list with each item a bytes or
        bytesarray object of record_size.
        """
        self.__record_size = record_size + 1
        mode = "w+b" if not os.path.exists(filename) else "r+b"
        self.__fh = open(filename, mode)
        self.auto_flush = auto_flush


    @property
    def record_size(self):
        "The size of each item"
        return self.__record_size -1 


    @property
    def name(self):
        "The name of the file"
        return self.__fh.name


    def flush(self):
        """Flush writes to disk. 
        Done automatically if auto_flush is True
        """
        self.__fh.flush()


    def close(self):
        self.__fh.close()


    def append(self, record):                   #new
        """Adds a new record
        """
        assert isinstance(record, (bytes, bytearray)), "binary data required"
        assert len(record) == self.record_size, ("record must be exactly {0} bytes".format(self.record_size))
        self.__fh.seek(0, os.SEEK_END)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()

 
    def __setitem__(self, index, record):       #new
        """Sets the item at position index to be the given record.
        The index position can be beyond the current end of the file."""
        assert isinstance(record, (bytes, bytearray)), \
            "binary data required"
        assert len(record) == self.record_size, ("record must be exactly {0} bytes".format(self.record_size))
        self.__fh.seek(index)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()


    def __getitem(self, index):                 #reduced code
        """Returns the item at the given index position
        If there is no item at the given index position, raises an IndexError exception.
        If the item at the given position has been deleted, returns None."""
        self.__seek_to_index(index)
        return self.__fh.read(self.record_size)


    def __seek_to_index(self, index):
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        offset = index * self.__record_size
        if offset >= end:
            raise IndexError("no record at index position {0}".format(index))
        self.__fh.seek(offset)


    def __delitem__(self, index):
        """Delete the item at the given index position and moves the following records up
        """
        length = len(self)
        for following in range(index + 1, length:
            self[index] = self[following]
            index += 1
        self.__fh.truncate((length - 1) * self.record_size)
        self.__fh.flush()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
