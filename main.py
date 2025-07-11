import pandas as pd
import xml.etree.ElementTree as ET

exel_file = "vis_data.xlsx"
df = pd.read_excel(exel_file, dtype={"PASDAT": str})
root = ET.Element("ROOT")

for _, row in df.iterrows():
    record = ET.SubElement(root, "Record")

    birthday = ET.SubElement(record, "BIRTHDAY")
    resident = ET.SubElement(record, "RESIDENT")
    cntrycont = ET.SubElement(record, "CNTRYCONT")
    coraddress = ET.SubElement(record, "CORADDRESS")
    cntryreg = ET.SubElement(record, "CNTRYREG")
    resaddress = ET.SubElement(record, "RESADDRESS")
    cntrylive = ET.SubElement(record, "CNTRYLIVE")
    address = ET.SubElement(record, "ADRESS")
    brpart = ET.SubElement(record, "BRPART")
    finprof = ET.SubElement(record, "FINPROF")
    groupcmd = ET.SubElement(record, "GROUPCMD")
    currencyno = ET.SubElement(record, "CURRENCYNO")
    cardprefix = ET.SubElement(record, "CARDPREFIX")
    occupation = ET.SubElement(record, "OCCUPATION")
    nameoncard = ET.SubElement(record, "NAMEONCARD")
    cellphone = ET.SubElement(record, "CELLPHONE")
    jobphone = ET.SubElement(record, "JOBPHONE")
    extaccount = ET.SubElement(record, "EXTACCOUNT")

    birthday.text = "01011960"
    resident.text = "T"
    cntrycont.text = "270"
    coraddress.text = "56,KAIRABA AVENUE"
    cntryreg.text = "270"
    resaddress.text = "56,KAIRABA AVENUE"
    cntrylive.text = "270"
    address.text = "56,KAIRABA AVENUE"
    brpart.text = "201"
    finprof.text = "1"
    groupcmd.text = "1"
    currencyno.text = "270"
    cardprefix.text = "458537"
    occupation.text = "21"

    for col_name in df.columns:
        element = ET.SubElement(record, col_name)
        element.text = str(row[col_name])
        if col_name == "FIO":
            nameoncard.text = str(row[col_name])
        if col_name == "PHONE":
            cellphone.text = str(row[col_name])
            jobphone.text = str(row[col_name])
        if col_name == "ACCOUNT":
            extaccount.text = str(row[col_name])

tree = ET.ElementTree(root)
output_file = "output.xml"
tree.write(output_file, encoding="utf-8", xml_declaration=True)
print(f"The XML {output_file} file have been created")
