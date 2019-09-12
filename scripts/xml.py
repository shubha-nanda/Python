import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()
print( root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)
    if child.tag=='country' and child.attrib=="{'name': 'UK1'}":
        print(child.tag)
    else:
        print(child.tag,"sd")




    