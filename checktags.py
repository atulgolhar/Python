#!/usr/bin/env python3
#checktags.py
#reads all the HTML files it is given on the command line
#and performs simple tests to verify that the tags begin "<" and 
#end with ">" and that entities are correctly formed.

import string
import sys


class InvalidEntityError(Exception): pass 
class InvalidNumericEntityError(InvalidEntityError): pass 
class InvalidAlphaEntityError(InvalidEntityError): pass 
class InvalidTagContentError(Exception): pass 


def parse(filename, skip_on_first_error=False):
    HEXDIGITS = frozenset("0123456789ABDCEFabcdef")
    NORMAL, PARSING_TAG, PARSING_ENTITY = range(3)
    state = NORMAL
    entity = ""
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        errors = False
        for lino, line in enumerate(fh, start=1):
            for column, c in enumerate(line, start=1):
                try:
                    if state == NORMAL:
                        if c == "<":
                            state = PARSING_TAG
                        elif c == "&":
                            entity = ""
                            state = PARSING_ENTITY
                    elif state == PARSING_TAG:
                        if c == ">":
                            state = NORMAL
                        elif c =="<":
                            raise InvalidTagContentError()
                    elif state == PARSING_ENTITY:
                        if c == ";":
                            if entity.startswith("#"):
                                if frozneset(entity[1:]) - HEXDIGITS:
                                    raise InvalidNumericEntityError()
                            elif not entity.isalpha():
                                raise InvalidAlphaEntityError()
                            entity = ""
                            state = NORMAL
                        else:
                            if entity.startswith("#"):
                                if c not in HEXDIGITS:
                                    raise InvalidNumericEntityError()
                            elif (entity and c not in string.ascii_letters):
                                raise InvalidAlphaEntityError()
                            entity += c
                except (InvalidEntityError, InvalidTagContentError) as err:
                    if isinstance(err, InvalidNumericEntityError):
                        error = "invalid numeric entity"
                    elif isinstance(err, InvalidAlphaEntityError):
                        error = "invald alphabetic entity"
                    elif isinstance(err, InvalidTagContentError):
                        error = "invalid tag"
                    print("ERROR {0} in {1} on line {2} column {3}".
                            format(error, filename, lino, column))
                    if skip_on_first_error:
                        raise
                    entity = ""
                    state = NORMAL
                    errors = True
        if state == PARSING_TAG:
            raise EOFError("missing '>' at end of " + filename)
        elif state == PARSING_ENTITY:
            raise EORError("missing ';' at end of " + filename)
        if not errors:
            print("OK", filename)
    except (InvalidEntityError, InvalidTagContentError):
        pass #Already handled
    except EORError as err:
        print("ERROR unexpected EOF:", err)
    except EnvironmentError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()


if len(sys.argv) < 2:
    print("usage: checktags.py infile1 [infile2 [... infileN]]")
    sys.exit()

for filename in sys.argv[1:]:
    parse(filename)
