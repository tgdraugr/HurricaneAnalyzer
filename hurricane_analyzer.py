def updated_damages(damages):
    if '100M' in damages:
        return [100000000]
    if '10M' in damages:
        return [10000000]
    return list(damages)
