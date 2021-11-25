def updated_damages(damages):
    return list(map(_updated_damage, damages))


def _updated_damage(damage):
    factors_per_suffix = {'B': 1000000000, 'M': 1000000}
    suffix = damage[-1]
    if suffix in factors_per_suffix:
        factor = factors_per_suffix.get(suffix)
        damage_value = damage.replace(suffix, "")
        return float(damage_value) * factor
    return damage
