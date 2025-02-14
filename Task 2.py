

def typeBasedTransformer(**kwargs):
    transformed = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transformed[key] = value ** 2
        elif isinstance(value, str):
            transformed[key] = value[::-1]
        elif isinstance(value, bool):
            transformed[key] = not value
        elif isinstance(value, (list, tuple)):
            transformed[key] = value[::-1]
        elif isinstance(value, dict):
            transformed[key] = {v: k for k, v in value.items()}
        else:
            transformed[key] = value

    return transformed

result = typeBasedTransformer(
    num=7,
    float_num=3.14,
    text="NewText",
    flag=False,
    items_list=[10, 20, 30],
    items_tuple=(5, 15, 25),
    data_dict={"a": 1, "b": 2}
)

print(result)
