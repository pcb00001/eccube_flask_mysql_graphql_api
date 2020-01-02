def isset(var):
    try:
        var
    except NameError:
        var = None
    return var