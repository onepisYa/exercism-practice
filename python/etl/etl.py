def transform(legacy_data):
    data = {}
    for score,keys in legacy_data.items():
        for key in keys:
            data.update({key.lower():score})
    return data


def _transform(legacy_data):
    return dict(sum([[(key.lower(), score) for key in keys] for score, keys in legacy_data.items()], []))
