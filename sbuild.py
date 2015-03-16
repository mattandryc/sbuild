#!/usr/bin/python
# -*- coding: utf-8 -*-

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
#Set up output
#strings = open('strings.xml', 'w')




class Element(object):

    def __init__(self, name, comment, child):
        self.name = name
        self.comment = comment
        self.child = child

    def xml_format(self):
        self.comment = '<!--' + self.comment + '-->'
        self.name = '<string name="' + self.name + '">'





choice = 0

def main_menu():
    print 'What are you building?'
    print '1. Toast'
    print '2. Dialogue box'
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
        if unique1.isalpha() and unique2.isalpha():
            break
    string_name = unique1.lower() + '_' + unique2.lower() + '_toast'
    toast_xml = Element(string_name, comment)
    toast_xml.xml_format()

if __name__ == "__main__":
    main()










