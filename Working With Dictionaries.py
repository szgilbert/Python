#dictionaries are like lists with keys that are assigned values
google = {'name': 'Google', 'address': '1600 Amphitheatre Parkway Mountain View, CA 94043', 'phone': '1-650-253-0000'}

print google.items()

#you can modify the values, add pairs, or delete them
google['phone'] = '0-000-0000'
google['web address'] = 'www.google.com'
del google['address']

print '\n', google.items()
print '\n', google.keys()
print '\n', google.values()
