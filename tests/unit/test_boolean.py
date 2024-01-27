import pprint
from tsxml.types import boolean


def test_boolean_true():
    path = [("Prop", {"Flags": "0x0", "Name": "MyBoolean", "Type": "Boolean"})]
    key = "Prop"
    value = {"@Flags": "0x0", "@Name": "MyBoolean", "@Type": "Boolean", "Value": "True"}
    result = boolean.parse(path, key, value)

    exp_result = {"key": "MyBoolean", "value": True}
    assert result == exp_result


def test_boolean_false():
    path = [("Prop", {"Flags": "0x0", "Name": "MyBoolean", "Type": "Boolean"})]
    key = "Prop"
    value = {
        "@Flags": "0x0",
        "@Name": "MyBoolean",
        "@Type": "Boolean",
        "Value": "False",
    }
    result = boolean.parse(path, key, value)

    exp_result = {"key": "MyBoolean", "value": False}
    assert result == exp_result
