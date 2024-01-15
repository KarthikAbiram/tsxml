# Import the required modules
import xmltodict
import pprint


def postprocessor(path, key, value):
    return key, value


def parse(xml: str) -> dict:
    my_dict = xmltodict.parse(xml, postprocessor=postprocessor)
    return my_dict


if __name__ == "__main__":
    # For dev/debug
    # Open the file and read the contents
    with open(r"tests\inputs\sample.xml", "r", encoding="utf-8") as file:
        my_xml = file.read()

    # Use xmltodict to parse and convert XML to dict
    # XML document
    my_dict = parse(my_xml)

    # Print the dictionary
    pprint.pprint(my_dict, indent=2)
