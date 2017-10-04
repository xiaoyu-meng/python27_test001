def story(**kwds):
    return 'Once upon a time, there was a %(job)s called %(name)s.' % kwds
def power(x,y,*others):
    if others:
        print 'Received redundant parameters;',others
    return pow(x,y)
def interval(start,stop=None,step=1):
    'Imitates range() for step>0'
    if stop is None:
        start,stop=0,start
    result=[]
    i=start
    while i<stop:
        result.append(i)
        i+=step
    return result


print story(job='king',name='Gumby')
pa1={'job':'language','name':'Python'}
print story(**pa1)

del pa1['job']
print story(job='language',**pa1)

print power(y=2,x=5)
print power(3,3,'Hello,World')


print interval(10)
print interval(1,5)
print interval(3,12,4)