def updated_damages(damages):
    return list(map(_updated_damage, damages))


def aggregated_records(**kwargs):
    return [_single_node(kwargs, 0)]


def _single_node(kwargs, hurricane_index):
    keys_per_arg = {
        'names': 'Name',
        'months': 'Month',
        'years': 'Year',
        'max_sustained_winds': 'Max Sustained Wind',
        'areas_affected': 'Areas Affected',
        'damages': 'Damage',
        'deaths': 'Deaths'
    }
    return {
        keys_per_arg.get('names'): kwargs.get('names')[hurricane_index],
        keys_per_arg.get('months'): kwargs.get('months')[hurricane_index],
        keys_per_arg.get('years'): kwargs.get('years')[hurricane_index],
        keys_per_arg.get('max_sustained_winds'): kwargs.get('max_sustained_winds')[hurricane_index],
        keys_per_arg.get('areas_affected'): kwargs.get('areas_affected')[hurricane_index],
        keys_per_arg.get('damages'): kwargs.get('damages')[hurricane_index],
        keys_per_arg.get('deaths'): kwargs.get('deaths')[hurricane_index]
    }


def _updated_damage(damage):
    factors_per_suffix = {'B': 1000000000, 'M': 1000000}
    suffix = damage[-1]
    if suffix in factors_per_suffix:
        factor = factors_per_suffix.get(suffix)
        damage_value = damage.replace(suffix, "")
        return float(damage_value) * factor
    return damage
