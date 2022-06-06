str = 'Lyft $10 121050  Lux $15 181050  LuxBlack $21 241050  LyftXL $21 241050  LuxBlackXL $28 321050'

#str = str.replace('- ', '').replace(':', '').replace('Lyft XL', 'LyftXL').replace('Lux Black XL', 'LuxBlackXL').replace('Lux Black', 'LuxBlack')

resp = {}

keys = []
values = []

key = ''
value = ''
newKey = False

print(str)

for i in str:
    if (not newKey):
        if (i.isalpha()):
            key += i
        if (i == ' ' and len(key) > 0):
            newKey = True
            if (key != ''):
                keys.append(key)
            key = ''
    if (newKey):
        if (i.isalnum() or i == '$'):
            value += i
        if (i == ' ' and len(value) > 0):
            newKey = False
            if (value != ''):
                values.append(value)
            value = ''


for i in range(len(keys)):
    for j in keys[i]:
        if (j.isupper() and keys[i].index(j) > 0):
            keys[i] = keys[i].replace(j, ' {}'.format(j)).strip()

for i in range(len(keys)):
    resp[keys[i]] = values[i]

print(resp)