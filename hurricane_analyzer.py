def updated_damages(damages):
    return list(map(_updated_damage, damages))


def aggregated_hurricane_records(aggregation_key='names', **kwargs):
    total_records = len(kwargs.get(aggregation_key))
    result = {}
    for hurricane_id in range(total_records):
        record = _single_hurricane_record(hurricane_id, kwargs)
        result[_value_of(aggregation_key, hurricane_id, kwargs)] = record
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
        'Name': _value_of('names', hurricane_id, kwargs),
        'Month': _value_of('months', hurricane_id, kwargs),
        'Year': _value_of('years', hurricane_id, kwargs),
        'Max Sustained Wind': _value_of('max_sustained_winds', hurricane_id, kwargs),
        'Areas Affected': _value_of('areas_affected', hurricane_id, kwargs),
        'Damage': _updated_damage(_value_of('damages', hurricane_id, kwargs)),
        'Deaths': _value_of('deaths', hurricane_id, kwargs)
    }


def _value_of(key, hurricane_id, kwargs):
    return kwargs.get(key)[hurricane_id]
