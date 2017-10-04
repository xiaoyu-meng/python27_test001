# -*- coding: utf-8 -*-

# .find  从左到右第一个字母的位置，找不到返回-1
print 'With a moo-moo here,and a moo-moo there'.find('moo')

title="Monty Python's Flying Circue"
print title.find('Monty')
print title.find('monty')

subject = """$$$ Get rich now !!!$$$"""
print subject.find("$$$")
print subject.find("""$$$""",4)


# .join  从左到右第一个字母的位置，找不到返回-1


seq=["1",'2','3']
sep='+'
print sep.join(seq)

dips = ('','usr','bin','evv')
print dips
print 'C:'+'/'.join(dips)

# .lower()   大写转小写
print 'Trondheim Hammer Dance'.lower()

if 'Gumby' in ['gumby','smith','jones']:
    print 'Found it'
else: print 'Not Found'

if 'Gumby'.lower() in ['gumby','smith','jones']:
    print 'Found it'

# .replace()   替换
print 'This is a test'.replace('s','y',2)
print 'This is a test'.replace('s','y')

# .split()   .rsplit('s') 替换
print '1+2+3+4+5'.split('+')
print 'using the default'.split()
print 'using the default'.split('s')
print 'using the default'.rsplit('s')

# .strip() 删除字符串两边的空格 字符
print "   sdf  sdf  sdf  sdf  sdfs  ysdh     ".strip()

print "*** SPAM * * *for * everyone !!!*******".strip('*!')

# .translate()
from string import maketrans

table = maketrans('cs','kz')
# print table
print len(table)
print 'this is an incredible test'.translate(table)
#转换加删除功能
print 'this is an incredible test'.translate(table,' ')