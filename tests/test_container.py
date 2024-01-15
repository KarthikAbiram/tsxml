from tsxml import main
import pprint


def test_simple_container():
    input_xml = """
    <?TS version="2019 (19.0.0.170)"?>
    <Prop Name='MyContainer' Type='Obj' Flags='0x4'>
        <Prop Name='MyNumber' Type='Number' Flags='0x0'>
            <Value>5</Value>
        </Prop>
        <Prop Name='MyString' Type='String' Flags='0x0'>
            <Value>Pi Genie!</Value>
        </Prop>
        <Prop Name='MyBoolean' Type='Boolean' Flags='0x0'>
            <Value>True</Value>
        </Prop>
    </Prop>
    """

    # Parse
    result = main.parse(input_xml)
    # pprint.pprint(result, indent=2)

    exp_result = {
        "MyContainer": {"MyBoolean": "True", "MyNumber": "5", "MyString": "Pi Genie!"}
    }

    assert result == exp_result
