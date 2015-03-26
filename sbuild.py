#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, string

class bcolors:
    NOTE = '\033[91m'
    ENDC = '\033[0m'


def usage():
    print '\n\nUsage:'
    print '$python sbuild.py path/to/values/strings.xml'
    print '或如果想建新的strings.xml文件的话就用$python sbuild.py target/path/to/values/'
    print bcolors.NOTE +'注意：你所输入的内容也会被自动地拷贝到target/path/to/values-zh-rCN/strings.xml' + bcolors.ENDC

menu_items = {'1':('对话框', '_dialogue'), '2':('toast', '_toast'), '3':('通知烂的通知', '_notification'), '4':('listview功能或选项', '_menu'),'5':('桌面应用图标的标题', '_appname')
}


#Create or append strings in values
def create_xml(raw_path):
    global dir_path, f
    dir_path, f = os.path.split(raw_path)
    os.chdir(dir_path)
    global strings
    if not os.path.isfile(raw_path):
        strings = open('strings.xml', 'w')
        strings.write('<?xml version="1.0" encoding="utf-8"?>\n')
        strings.write('<resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">\n\n')
    else:
        strings = open(raw_path,"r")
        lines = strings.readlines()
        strings.close()
        strings = open("strings.xml","w")
        for line in lines:
            if line!="</resources>" and line!="</resources>\n":
                strings.write(line)

#Create or append strings in values-zh-rCN
def create_zh_xml(raw_path):
    global zh_dir_path 
    zh_dir_path = str(dir_path).replace('values', 'values-zh-rCN')
    print zh_dir_path
    print os.path.join(zh_dir_path, f)
    os.chdir(zh_dir_path)
    global zh_strings
    if not os.path.isfile(os.path.join(zh_dir_path, f)):
        zh_strings = open('strings.xml', 'w')
        zh_strings.write('<?xml version="1.0" encoding="utf-8"?>\n')
        zh_strings.write('<resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">\n\n')
    else:
        zh_strings = open(os.path.join(zh_dir_path, f),"r")
        lines = zh_strings.readlines()
        zh_strings.close()
        zh_strings = open("strings.xml","w")
        for line in lines:
            if line!="</resources>" and line!="</resources>\n":
                zh_strings.write(line)

#Functions
def write_xml(comment, string_name, child, plural):
    strings.write('    ' + '<!-- ' + comment + ' -->\n')
    if plural != True:
        os.chdir(dir_path)
        strings.write('    ' + '<string name =\"' + string_name + '\">\"' + child + '\"</string>\n\n')

        os.chdir(zh_dir_path)
        zh_strings.write('    ' + '<string name =\"' + string_name + '\">\"' + child + '\"</string>\n\n')

    else:
        os.chdir(dir_path)
        strings.write('    ' + '<plurals name =\"' + string_name + '\">\n')
        strings.write('        ' + '<item quantity =\"other\">' + child + '</item>\n')
        strings.write('    ' + '</plurals>\n\n')

        os.chdir(zh_dir_path)
        zh_strings.write('    ' + '<plurals name =\"' + string_name + '\">\n')
        zh_strings.write('        ' + '<item quantity =\"other\">' + child + '</item>\n')
        zh_strings.write('    ' + '</plurals>\n\n')

def var_check(string):
    if '%s' in string:
        string = string.replace('%s', var_ask(str('%s')))
        return string
    if '%1$s' in string:
        string = string.replace('%1$s', var_ask(str('%1$s')))
    if '%2$s' in string:
        string = string.replace('%2$s', var_ask(str('%2$s')))
    if '%3$s' in string:
        string = string.replace('%3$s', var_ask(str('%3$s')))
    return string

def var_ask(var_type):
    print '%s参数代表什么？（一个词描述）：' % (var_type)
    xliff_id = raw_input('> ')
    print '输入一下%s显示例子？：'
    xliff_example = raw_input('> ')
    xliff_format = '<xliff:g id=\"' + xliff_id +'\" ' + 'example=\"' + xliff_example + '\">' + var_type + '</xliff:g>'
    return xliff_format

def namify(string):
    if string[len(string) - 1] == ' ':
        string = string[:len(string) - 1]
        string = namify(string)
    else:
        string = string.replace(" ","_")
        return string.lower()

def name_check(string_name):
    for letter in string_name:
        if letter not in string.lowercase and letter != '_':
            return False
        else:
            return True

def ask(choice, string_name, comment, string_type):

    string_types = {'1':('标题', '_title', 'Title text for '), '2':('标题下面的内容', '_summary', 'Summary text for '), '3':( '对话框确认按钮的文字', '_positive', 'Positive button text for dialogue '), '4':('对话框否认按钮的文字', '_negative', 'Negative button text for dialogue '), '5':('桌面应用显示名', '_app_title', 'App title displayed on Home screen for '), '6':('内容', '', 'Toast message for ')
}

    print '输入你的%s显示的%s' % (choice, string_types.get(str(string_type))[0])
    child = raw_input('> ')
    string_name += str(string_types.get(str(string_type))[1])
    comment = str(string_types.get(str(string_type))[2]) + comment
    if '%d' in child:
        plural = True
    else:
        plural = False
    write_xml(comment, string_name, var_check(str(child)), plural)

def menu():
    print '\n\nWhat are you building?'
    for key in iter(sorted(menu_items.iteritems())):
        print key[0] + '. ' + key[1][0]
    while True:
        try:
            choice = int(raw_input('> '))
        except ValueError:
            print bcolors.FAIL + 'Input invalid. Try again.'
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
            os.chdir(dir_path)
            strings.write('</resources>')
            strings.close()
            os.chdir(zh_dir_path)
            zh_strings.write('</resources>')
            zh_strings.close()
            print '下次光临'
            exit(1)
        else:
            print 'Input invalid. Try again.'

def builder(choice):
    dialogue_types = {'1':('警告', '_warning'), '2':('提示', '_notify'), '3':('更改权限', '_perms'), '4':('时定提示', '_remind')
}
    print 'OK, let\'s build a %s！ \n\n简单地描述一下你的%s在什么情况下出现：' % (choice[0], choice[0])
    comment = raw_input('> ')
    print '\n\n'
    while True:
        print '给你的%s配一个关键词（例如：\'email\'）:' % choice[0]
        unique1 = str(namify(raw_input('> ')))
        if name_check(unique1) is False:
            print 'string name限制用非英文字母. Try again.'
        else:
            break

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
        while True:
            print '给你的%s配一个状态（例如：\'sent\'）:' % choice[0]
            unique2 = str(namify(raw_input('> ')))
            if name_check(unique1) is False:
                print 'string name限制用非英文字母. Try again.'
            else:
                break
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
    while True:
        try:
            create_xml(sys.argv[1])
            create_zh_xml(sys.argv[1])
            menu()
        except IndexError:
            usage()
            exit(-1)

if __name__ == "__main__":
    main()

