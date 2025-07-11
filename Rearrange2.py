import xml.etree.ElementTree as ET

desired_order = ["FIO", "SEX", "BIRTHDAY", "BIRTHPLACE", "PASNOM", "PASPLACE", "PASDAT", "RESIDENT", "CNTRYCONT",
                 "CORADDRESS", "CNTRYREG", "RESADDRESS", "CNTRYLIVE", "ADRESS", "PHONE", "CELLPHONE", "JOBPHONE",
                 "BRPART", "FINPROF", "GROUPCMD", "CURRENCYNO", "CARDPREFIX", "NAMEONCARD", "ACCOUNT", "EXTACCOUNT",
                 "OCCUPATION"]
tree = ET.parse("output.xml")
root = tree.getroot()

for person in root.findall("Record"):
    elements = {elem.tag: elem for elem in person}
    person.clear()
    for tag in desired_order:
        if tag in elements:
            person.append(elements[tag])


tree.write("sorted_output.xml", encoding="utf-8", xml_declaration=True)
print("process completed......")

