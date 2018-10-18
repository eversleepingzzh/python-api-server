def obj_from_model(object):
    if object is not None:
        obj = object.__dict__
        if obj["_id"] is not None:
            obj.pop('_id')
            return obj
    else:
        return {}

