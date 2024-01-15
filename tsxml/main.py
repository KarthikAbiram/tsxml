# Import the required modules
import xmltodict
import pprint

from .types import basic, object, array


def postprocessor(path, key, value):
    """
    Post processor callback of xmltodict, which we use to further process the TestStand XML.

    This would be called several times while parsing the XML.
    We are only interested in manipulating the data when we get the key as "Prop"
    """
    # Initialize
    result = {"key": key, "value": value}

    if key == "Prop":
        data_type = value["@Type"]
        if data_type in ["String", "Number", "Boolean"]:
            result = basic.parse(path, key, value)
        elif data_type in ["Obj"]:
            result = object.parse(path, key, value)
        elif data_type in ["Array"]:
            result = array.parse(path, key, value)

    return result["key"], result["value"]


def parse(xml: str) -> dict:
    tsxml_dict = xmltodict.parse(xml, postprocessor=postprocessor)
    return tsxml_dict
