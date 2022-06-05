str = 'Lyft $9 - 126:36  Lux $12 - 156:36  Lyft XL $20 - 256:36  Lux Black $20 - 256:36  Lux Black XL $35 - 426:36'

str = str.replace('- ', '').replace(':', '')

resp = {}

key = ''
value = ''
pos = 0

for i in str:
    if (i == ' '):
        for k in range(pos, len(str)):
            key += str[k]
        for k in range(pos + 1, len(str)):
            if (str[k] == ' '): break
            value += str[k]
        resp[key] = value

print(str)
#print(resp)