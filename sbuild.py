#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import exit

'''
*Engine
*Output
*Objects
-a toast
-a dialogue box
-a notification in the notification shade
-a menu item or a function
-app name
-action bar
-other
'''
#Set strings.xml
strings = open('strings.xml', 'w')
strings.write('<?xml version="1.0" encoding="utf-8"?>\n')
strings.write('<resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">\n')

#Elements below this line

class Element(object):

    def __init__(self, name, comment, child):
        self.name = name
        self.comment = comment
        self.child = child

    def xml_format(self):
        self.comment = '<!-- ' + self.comment + ' -->'
        self.name = '<string name=\"' + self.name + '\">'

    def xml_writeto(self):
        strings.write('    ' + self.comment + '\n')
        strings.write('    ' + self.name + self.child + '</strings>\n\n')

class DialogueBox(Element):

    def __init__(self, name, comment, child, body, positive, negative):
        self.name = name
        self.comment = comment
        self.child = child
        self.body = body
        self.positive = positive
        self.negative = negative

    def xml_format(self):
        self.comment = '<!-- ' + self.comment + ' -->'
        self.name = '<string name=\"' + self.name

    def xml_writeto(self):
        strings.write('    ' + self.comment + '\n')
        strings.write('    ' + self.name + '_title\">'  + self.child + '</strings>\n')
        strings.write('    ' + self.name + '_body\">'  + self.body + '</strings>\n')
        strings.write('    ' + self.name + '_positive\">'  + self.positive + '</strings>\n')
        strings.write('    ' + self.name + '_negative\">'  + self.negative + '</strings>\n')

#Functions below this line

def done():
    print '还有其它业务么？ （y/N）'
    while True:
        try:
            dchoice = str(raw_input('> '))
        except ValueError:
            print 'Input invalid. Try again.'
            continue
        if dchoice.lower() ==  'y':
            main()
        elif dchoice.lower() ==  'n':
            strings.write('</resources>')
            strings.close()
            print '下次光临'
            exit(1)
        else:
            print 'Input invalid. Try again.'

def namify(string_name):
    if string_name[len(string_name) - 1] == ' ':
        string_name = string_name[:len(string_name) - 1]
        string_name = namify(string_name)
    else:
        string_name = string_name.replace(" ","_")
        return string_name.lower()

choice = 0

def main_menu():
    print 'What are you building?'
    print '1. Toast'
    print '2. 对话框'
    print '3. Notification' 
    print '4. Menu item'
    print '5. Action bar' 
    print '6. Other' 
    while True:
        try:
            choice = int(raw_input('> '))
        except ValueError:
            print 'Input invalid. Try again.'
            continue
        if choice in range(1, 7):
            return choice
            break
        else:
            print 'Input invalid. Try again.'

def main():
    choice = main_menu()
    if choice == 1:
        toast()
    if choice == 2:
        dialogue()


def toast ():
    print '\n\n\n'
    print 'let\'s build a toast'
    print '简单地描述一下你的toast什么时候出现'
    comment = raw_input('> ')
    while True:
        try:
            print 'Enter object for toast'
            unique1 = str(raw_input('> '))
            print 'Enter status for toast'
            unique2 = str(raw_input('> '))
        except ValueError:
            print 'Input invalid. Try again.'
            continue
        else:
            unique1 = namify(unique1)
            unique2 = namify(unique2)
            break
    string_name = unique1 + '_' + unique2 + '_toast'
    print '输入toast显示内容'
    child = str(raw_input('> '))
    toast_xml = Element(string_name, comment, child)
    toast_xml.xml_format()
    toast_xml.xml_writeto()
    done()


def dialogue ():
    d_types = {1:'warning', 2:'notify', 3:'perms', 4:'remind'}
    print '\n\n\n'
    print 'let\'s build a 对话框'
    print '简单地描述一下你的对话框在什么情况下出现'
    comment = raw_input('> ')
    while True:
        try:
            print 'Enter unique keyword for dialogue box'
            unique1 = str(raw_input('> '))
            print 'Choose type for dialogue box'
            print '1. Warning'
            print '2. Notification'
            print '3. Permissions' 
            print '4. Reminder'
            unique2 = int(raw_input('> '))
            if unique2 in range(1, 4):
                unique2 = d_types.get(unique2)
        except ValueError:
            print 'Input invalid. Try again.'
            continue
        else:
            unique1 = namify(unique1)
            break
    string_name = unique1 + '_' + unique2 + '_dialogue'
    print '输入对话框显示的标题'
    child = str(raw_input('> '))
    print '输入对话框显示的内容'
    body = str(raw_input('> '))
    print '输入对话框确认按钮的文字'
    positive = str(raw_input('> '))
    print '输入对话框否认按钮的文字'
    negative = str(raw_input('> '))
    dialogue = DialogueBox(string_name, comment, child, body, positive, negative)
    dialogue.xml_format()
    dialogue.xml_writeto()
    done()


if __name__ == "__main__":
    main()
