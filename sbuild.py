#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

def usage():
    print 'Usage:'
    print '$python sbuild.py path/to/strings.xml'
    print 'or to create a new strings.xml file, $python sbuild.py target/path/'


menu_items = {'1':('对话框', '_dialogue'), '2':('toast', '_toast'), '3':('通知烂的通知', '_notification'), '4':('listview功能或选项', '_menu'),'5':('桌面应用图标的标题', '_appname')}

#Create or append strings
def create_xml(path_to_strings):
    global strings
    if not os.path.isfile(path_to_strings):
        strings = open('strings.xml', 'w')
        strings.write('<?xml version="1.0" encoding="utf-8"?>\n')
        strings.write('<resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">\n\n')
    else:
        strings = open(path_to_strings,"r")
        lines = strings.readlines()
        strings.close()
        strings = open("strings.xml","w")
        for line in lines:
            if line!="</resources>" and line!="</resources>\n":
                strings.write(line)

#Functions
def write_xml(comment, string_name, child, plural):
    strings.write('    ' + '<!-- ' + comment + ' -->\n')
    if plural != True:
        strings.write('    ' + '<string name =\"' + string_name + '\">\"' + child + '\"</string>\n\n')
    else:
        strings.write('    ' + '<plurals name =\"' + string_name + '\">\n')
        strings.write('        ' + '<item quantity =\"other\">' + child + '</item>\n')
        strings.write('    ' + '</plurals>\n\n')

def namify(string):
    if string[len(string) - 1] == ' ':
        string = string[:len(string) - 1]
        string = namify(string)
    else:
        string = string.replace(" ","_")
        return string.lower()

def ask(choice, string_name, comment, string_type):
    string_types = {'1':('标题', '_title'), '2':('标题下面的内容', '_summary'), '3':( '对话框确认按钮的文字', '_positive'), '4':('对话框否认按钮的文字', '_negative',), '5':('桌面应用显示名', '_app_title'), '6':('内容', '')}
    print '输入你的%s显示的%s' % (choice, string_types.get(str(string_type))[0])
    child = raw_input('> ')
    string_name += str(string_types.get(str(string_type))[1])
    if '%d' in child:
        plural = True
    else:
        plural = False
    print string_name
    write_xml(comment, string_name, child, plural)

def menu():
    print '\n\nWhat are you building?'
    for key in iter(sorted(menu_items.iteritems())):
        print key[0] + '. ' + key[1][0]
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
    print '还有其它业务么？[yN]'
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
    dialogue_types = {'1':('警告', '_warning'), '2':('提示', '_notify'), '3':('更改权限', '_perms'), '4':('时定提示', '_remind')}
    print '\n\n'
    print 'OK, let\'s build a %s！ \n\n简单地描述一下你的%s在什么情况下出现：' % (choice[0], choice[0])
    comment = raw_input('> ')
    print 'Enter unique keyword for your %s:' % choice[0]
    unique1 = str(namify(raw_input('> ')))

    #Dialogue builder
    if choice[0] == '对话框':
        print '你在做什么样的对话框？'
        for key in iter(sorted(dialogue_types.iteritems())):
            print key[0] + '. ' + key[1][0]
        while True:
            try:
                dialogue_type = int(raw_input('> '))
            except ValueError:
                print 'Input invalid. Try again.'
                continue
            if dialogue_type in range(1, 4):
                string_name = unique1 + str(dialogue_types.get(str(dialogue_type))[1]) + choice[1]
                for n in range(1,5):
                    ask(choice[0], string_name, comment, n)
                done()
            else:
                print 'Input invalid. Try again.'

    #Everything else builder
    else:
        print 'Enter unique status for your %s:' % choice[0]
        unique2 = str(namify(raw_input('> ')))
        string_name = unique1 + '_' + unique2 + choice[1]
        if choice[0] == 'toast':
            ask(choice[0], string_name, comment, 6)
            done()
        if choice[0] == '通知烂的通知':
            for n in range(1,3):
                ask(choice[0], string_name, comment, n)
            done()
        if choice[0] == 'listview功能或选项':
            for n in range(1,3):
                ask(choice[0], string_name, comment, n)
            done()
        if choice[0] == 'listview功能或选项':
            for n in range(1,3):
                ask(choice[0], string_name, comment, n)
            done()
        if choice[0] == '桌面应用图标的标题':
            for n in range(1,3):
                ask(choice[0], string_name, comment, n)
            done()

def main():
    if len(sys.argv) < 1:
        usage()
    else:
        create_xml(sys.argv[1])
        menu()

if __name__ == "__main__":
    main()

