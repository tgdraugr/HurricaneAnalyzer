def updated_damages(damages):
    return list(map(_updated_damage, damages))


def aggregated_hurricane_records_by_name(**kwargs):
    result = {}
    for hurricane_id, context in enumerate(kwargs.get("names")):
        result[context] = _single_hurricane_record(hurricane_id, kwargs)
    return result


def aggregated_hurricane_records_by_year(hurricanes_by_name):
    years = list(map(lambda h: h["Year"], hurricanes_by_name.values()))
    records_by_year = dict((year, []) for year in years)
    for hurricane in hurricanes_by_name.values():
        records_by_year[hurricane["Year"]].append(hurricane)
    return records_by_year


def total_areas_affected(hurricanes_by_name):
    areas_per_hurricane = \
        list(map(lambda h: h["Areas Affected"], hurricanes_by_name.values()))
    areas = sum(areas_per_hurricane, [])
    return dict((area, areas.count(area)) for area in areas)


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
        'Name': kwargs.get('names')[hurricane_id],
        'Month': kwargs.get('months')[hurricane_id],
        'Year': kwargs.get('years')[hurricane_id],
        'Max Sustained Wind': kwargs.get('max_sustained_winds')[hurricane_id],
        'Areas Affected': kwargs.get('areas_affected')[hurricane_id],
        'Damage': _updated_damage(kwargs.get('damages')[hurricane_id]),
        'Deaths': kwargs.get('deaths')[hurricane_id]
    }
