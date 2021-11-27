"""
    Hurricane Analyzer.
"""

_FACTORS_BY_SUFFIX = {
    'B': 1000000000,
    'M': 1000000
}


def updated_damages(damages):
    return _transformed(damages, mapper=_updated_damage)


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
    years = _transformed(hurricanes_by_name.values(), lambda h: h["Year"])
    hurricanes_by_year = dict((year, []) for year in years)
    for hurricane in hurricanes_by_name.values():
        hurricanes_by_year[hurricane["Year"]].append(hurricane)
    return hurricanes_by_year


def total_areas_affected(hurricanes_by_name):
    areas = sum(_transformed(hurricanes_by_name.values(), lambda h: h["Areas Affected"]), [])
    return dict((area, areas.count(area)) for area in areas)


def most_affected_area(affected_areas):
    return _top_most_of(affected_areas)


def most_deadly_hurricane(hurricanes_by_name):
    deaths_by_hurricane = dict(_transformed(hurricanes_by_name.values(), lambda h: (h["Name"], h["Deaths"])))
    return _top_most_of(deaths_by_hurricane)


def _updated_damage(damage):
    suffix = damage[-1]
    if suffix in _FACTORS_BY_SUFFIX:
        factor = _FACTORS_BY_SUFFIX.get(suffix)
        damage_value = damage.replace(suffix, "")
        return float(damage_value) * factor
    return damage


def _top_most_of(tuples, count_field=1):
    descending_values = \
        sorted(list(iter(tuples.items())),
               key=lambda a: a[count_field], reverse=True)
    return descending_values[0]


def _transformed(iterable, mapper):
    return list(map(mapper, iterable))
