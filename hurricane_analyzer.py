def updated_damages(damages):
    return list(map(_updated_damage, damages))


def aggregated_hurricane_records(**kwargs):
    total_records = len(kwargs.get('names'))
    result = []
    for hurricane_id in range(total_records):
        result.append(_single_hurricane_record(hurricane_id, kwargs))
    return result


def _updated_damage(damage):
    factors_per_suffix = {'B': 1000000000, 'M': 1000000}
    suffix = damage[-1]
    if suffix in factors_per_suffix:
        factor = factors_per_suffix.get(suffix)
        damage_value = damage.replace(suffix, "")
        return float(damage_value) * factor
    return damage


def _single_hurricane_record(hurricane_id, kwargs):
    return {
        'Name': _valueOf('names', hurricane_id, kwargs),
        'Month': _valueOf('months', hurricane_id, kwargs),
        'Year': _valueOf('years', hurricane_id, kwargs),
        'Max Sustained Wind': _valueOf('max_sustained_winds', hurricane_id, kwargs),
        'Areas Affected': _valueOf('areas_affected', hurricane_id, kwargs),
        'Damage': _updated_damage(_valueOf('damages', hurricane_id, kwargs)),
        'Deaths': _valueOf('deaths', hurricane_id, kwargs)
    }


def _valueOf(key, hurricane_id, kwargs):
    return kwargs.get(key)[hurricane_id]
