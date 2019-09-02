import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">

    +1 734 303 4456

  </phone>
  <email hide="yes" />
</person>'''
                           #here white space matters as it is displayed on screen as is
tree = ET.fromstring(data)
#print(tree)
print('Name:', tree.find('name').text)  #see here u r getting directly because all tags are undre one main tag person but if there are several child tags under which also there are tags as in next xml2.py then u have to specify to which sub tag the tag u wants belon to
print('Attr:', tree.find('email').get('hide'))
print('Attr:', tree.find('phone').text)
