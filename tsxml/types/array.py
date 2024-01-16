import pprint


def parse(path, key, value) -> dict:
    # Initialize result
    result = {"key": key, "value": value}

    # Parse key
    key_out = value["@Name"]

    # Parse value
    items = value["Value"]
    value_out = []
    for item in items:
        if "Prop" in item.keys():
            value_out.append(item["Prop"])
        elif "#text" in item.keys():
            value_out.append(item["#text"])
        else:
            value_out.append("")

    # Array element type
    array_element_type = value["@ElementType"]
    # Convert array elements based on element type
    if array_element_type == "Number":
        value_out = [float(item) for item in value_out]
    elif array_element_type == "Boolean":
        value_out = [item == "True" for item in value_out]

    # Consolidate Result
    result["key"] = key_out
    result["value"] = value_out

    return result
