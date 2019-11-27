
def get_field_rel(field):
    try:
        return field.rel
    except AttributeError:
        return field.remote_field
