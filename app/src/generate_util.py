def convertSnackToPascal(snake_str):
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return ''.join(x.title() for x in snake_str.split('_'))


def convertSnackToCamel(snake_str):
    pascal = convertSnackToPascal(snake_str)
    return pascal[0].lower() + pascal[1:]