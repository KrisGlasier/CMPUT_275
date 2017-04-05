import hashlib 
def hash(obj):
    '''Calculates the md5 hash of the string representation
    of its argument.'''
    return hashlib.md5(bytes(str(obj),'utf-8')).hexdigest()
