def updated_damages(damages):
    return list(map(_updated_damage, damages))


def aggregated_hurricane_records_by_name(**kwargs):
    def _new_hurricane(hurricane_index):
        return {
            'Name': kwargs.get('names')[hurricane_index],
            'Month': kwargs.get('months')[hurricane_index],
            'Year': kwargs.get('years')[hurricane_index],
            'Max Sustained Wind': kwargs.get('max_sustained_winds')[hurricane_index],
            'Areas Affected': kwargs.get('areas_affected')[hurricane_index],
            'Damage': _updated_damage(kwargs.get('damages')[hurricane_index]),
            'Deaths': kwargs.get('deaths')[hurricane_index]
        }
    return dict((hurricane_name, _new_hurricane(hurricane_id))
                for hurricane_id, hurricane_name in enumerate(kwargs.get("names")))


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


def most_affected_area(affected_areas):
    return next(iter(affected_areas.items()))


def _updated_damage(damage):
    factors_per_suffix = {'B': 1000000000, 'M': 1000000}
    suffix = damage[-1]
    if suffix in factors_per_suffix:
        factor = factors_per_suffix.get(suffix)
        damage_value = damage.replace(suffix, "")
        return float(damage_value) * factor
    return damage
