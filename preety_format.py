import xml.etree.ElementTree as ET
from xml.dom import minidom


def prettify(element):
    rough_string = ET.tostring(element, 'utf-8')
    parsed = minidom.parseString(rough_string)
    return parsed.toprettyxml(indent="  ")


tree = ET.parse('sorted_output.xml')
root = tree.getroot()

formatted_xml = prettify(root)

with open('prettyformatted.xml', "w", encoding="utf-8") as f:

    f.write(formatted_xml)
print("process completed.....")

