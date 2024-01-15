from tsxml import main
import pprint


def test_sample():
    with open(r"tests\inputs\sample.xml", "r", encoding="utf-8") as file:
        my_xml = file.read()

    # Use xmltodict to parse and convert the
    # XML document
    my_dict = main.parse(my_xml)

    # Print the dictionary
    pprint.pprint(my_dict, indent=2)
