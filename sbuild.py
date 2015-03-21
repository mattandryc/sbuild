#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import exit, argv
import os

menu_items = {'1':'toast', '2':'对话框', '3':'通知烂的通知', '4':'menu item','5':'Home screen app name'}

#Create strings.xml
if not os.path.isfile(argv[1]):
    strings = open('strings.xml', 'w')
    strings.write('<?xml version="1.0" encoding="utf-8"?>\n')
    strings.write('<resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">\n\n')
else:
	strings = open(argv[1],"r")
	lines = strings.readlines()
	strings.close()
	strings = open("strings.xml","w")
	for line in lines:
  		if line!="</resources>":
			strings.write(line)

#Functions
def write_xml(comment, string_name, child, tail):
    suffix =  {'1':'_title', '2':'_summary', '3':'_positive', '4':'_negative'}
    char_limit = {}
    if tail in range(1, 5):
        string_name += str(suffix.get(str(tail)))
    strings.write('    ' + '<!-- ' + comment + ' -->\n')
    strings.write('    ' + '<string name =\"' + string_name + '\">' + child + '</string>\n\n')


def namify(string):
    if string[len(string) - 1] == ' ':
        string = string[:len(string) - 1]
        string = namify(string)
    else:
        string = string.replace(" ","_")
        return string.lower()

def ask(): 


def menu():
    print '\n\nWhat are you building?'
    for key in iter(sorted(menu_items.iteritems())):
        print key[0] + '. ' + key[1]
    while True:
        try:
            choice = int(raw_input('> '))
        except ValueError:
            print 'Input invalid. Try again.'
            continue
        if choice in range(1, 7):
            builder(menu_items.get(str(choice)))
            break
        else:
            print 'Input invalid. Try again.'


def done():
    print '还有其它业务么？[y/N]'
    while True:
        try:
            dchoice = str(raw_input('> '))
        except ValueError:
            print 'Input invalid. Try again.'
            continue
        if dchoice.lower() ==  'y':
            menu()
        elif dchoice.lower() ==  'n':
            strings.write('</resources>')
            strings.close()
            print '下次光临'
            exit(1)
        else:
            print 'Input invalid. Try again.'


def builder(choice):

    d_types = {1:'warning', 2:'notify', 3:'perms', 4:'remind'}

    print '\n\n'
    print 'OK, let\'s build a %s！ \n\n简单地描述一下你的%s在什么情况下出现：' % (choice, choice)
    comment = raw_input('> ')
    print 'Enter unique keyword for your %s:' % choice
    unique1 = str(namify(raw_input('> ')))

    if choice == '对话框':
        while True:
            try:
                print 'Choose type for dialogue box'
                print '1. Warning'
                print '2. Notification'
                print '3. Permissions' 
                print '4. Reminder'
                unique2 = int(raw_input('> '))
                if unique2 in range(1, 4):
                    unique2 = d_types.get(unique2)
                    break
            except ValueError:
                print 'Input invalid. Try again.'
                continue

    else:
        print 'Enter unique status for your %s:' % choice
        unique2 = str(namify(raw_input('> ')))
    string_name = unique1 + '_' + unique2

    if choice == 'toast':
        string_name += '_toast'
        print '输入toast显示内容：'
        child = str(raw_input('> '))
        write_xml(comment, string_name, child, 0)
        done()

    if choice == '对话框':
        string_name += '_dialogue'
        print '输入对话框显示的标题：'
        child = str(raw_input('> '))
        write_xml(comment, string_name, child, 1)
        print '输入对话框显示的内容：'
        summary = str(raw_input('> '))
        write_xml(comment, string_name, summary, 2)
        print '输入对话框确认按钮的文字：'
        positive = str(raw_input('> '))
        write_xml(comment, string_name, positive, 3)
        print '输入对话框否认按钮的文字：'
        negative = str(raw_input('> '))
        write_xml(comment, string_name, negative, 4)
        done()

    if choice == '通知烂的通知':
        string_name += '_notification'
        print '输入通知烂的通知显示的标题：'
        child = str(raw_input('> '))
        write_xml(comment, string_name, child, 1)
        print '输入通知烂的通知显示的标题：'
        summary = str(raw_input('> '))
        write_xml(comment, string_name, summary, 2)
        done()

    if choice == 'menu item':
        string_name += '_menu'
        print '输入通知烂的通知显示的标题：'
        child = str(raw_input('> '))
        write_xml(comment, string_name, child, 1)
        print '输入通知烂的通知显示的标题：'
        summary = str(raw_input('> '))
        write_xml(comment, string_name, summary, 2)
        done()

    if choice == 'Home screen app name':
        string_name += '_app_name'
        print '输入Home screen app name显示的标题：'
        child = str(raw_input('> '))
        done()

if __name__ == "__main__":
    menu()
	