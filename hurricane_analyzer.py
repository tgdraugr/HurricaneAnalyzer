def updated_damages(damages):
    return list(map(_converted_damage, damages))


def _converted_damage(damage):
    factors_per_suffix = {'B': 1000000000, 'M': 1000000}
    suffix = damage[-1]
    if suffix in factors_per_suffix:
        return float(damage.replace(suffix, "")) * factors_per_suffix.get(suffix)
    return damage
