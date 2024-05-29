#!/usr/bin/env python3
import xml.etree.ElementTree as ET

""" Defines a method named serialize_to_xml that serializes the dictionary
    into XML and save it to the given filename.
"""


def serialize_to_xml(dictionary, filename):
    """ Creates a root element, iterates through the dictionary items, adds
        them as child elements to the root and writes the XML tree to the
        provided filename.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


""" Defines a method named deserialize_from_xml that reads the XML data from
    that file, and return a deserialized Python dictionary.
"""


def deserialize_from_xml(filename):
    """ Parses the XML file, navigates through the XML elements and returns a
        constructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        
        return dictionary
    except Exception as e:
        print(f"Error during deserialization of the xml file: {e}")
        return None
