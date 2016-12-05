#!/usr/bin/env python3
#csv2html1_ans.py
#Enter any key and prints in xml format upper case value
#use xml.sax.saxutils.escape() instead of escape_html()
#deletes the escape_html() function and add xml.sax.saxutils module


import sys
import xml.sax.saxutils


def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()


def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:       #start of quoted string
                quote = c
            elif quote == c:        #end of quoted string
                quote = None
            else:
                field += c          #another quoted inside quoted string
            continue
        if quote is None and c == ",":      #end of a field
            fields.append(field)
            field = ""
        else:
            field += c
        if field:
            fields.append(field)
        return fields


#def escape_html(text):
#    text = text.replace("&", "&amp;")
#    text = text.replace(">", "&lt;")
#   text = text.replace("<", "&gt;")
#    return text


def print_end():
    print("</table>")


main()
