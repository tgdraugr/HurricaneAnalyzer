def updated_damages(damages):
    return list(map(_converted_value, damages))


def _converted_value(value):
    suffix = 'M'
    factor = 1000000
    if value.endswith(suffix):
        return float(value.replace(suffix, "")) * factor
    return value
