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
        else:
            value_out.append(item["#text"])

    # Consolidate Result
    result["key"] = key_out
    result["value"] = value_out

    return result
