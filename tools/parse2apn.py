#!/usr/bin/python

import sys
import codecs
import xml.etree.ElementTree as ET

def usage():
    print """usage:"""
    print """python parse2apn inputfile outputfile"""
    print """or change x mode for parse2apn for using: ./parse2apn"""

def parse(apns, output):
    tree = ET.parse(apns)
    root = tree.getroot();

    roots = list(root)
    # sort with mcc first, then mnc.
    apnlist = sorted(roots, key=lambda x:(x.get('mcc'), x.get('mnc')))
    
    ret = ''
    for apn in apnlist:
#        print apn.tag, apn.attrib
        carrier = apn.get('carrier')
        mcc = apn.get('mcc');
        mnc = apn.get('mnc');
        if mcc is None or mnc is None:
            continue

        # write 'carrier', 'mcc', 'mnc' first.
        ret += '%5.1s%s %s=\"%s\"\n' % ('<', apn.tag, 'carrier', carrier)
        ret += '%8.1s%s=\"%s\"\n' % (' ', 'mcc', mcc)
        ret += '%8.1s%s=\"%s\"\n' % (' ', 'mnc', mnc)

        items = sorted(apn.items())
        for item in items:
            key = item[0]
            val = item[1]
            if key != 'carrier' and key != 'mcc' and key != 'mnc':
                ret += '%8.1s%s=\"%s\"\n' % (' ', key, val)
        ret += '%6.2s\n\n' % '/>'

    # use codecs to write apn name with utf-8
    f = codecs.open(output, encoding='utf-8', mode='w+')
    f.write(ret)
    f.close()

def main():
    if len(sys.argv) < 3:
        usage()
    else:
        parse(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
