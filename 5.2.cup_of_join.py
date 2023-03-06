def join(*lists, sep='-'):
    """
    Concatenates multiple lists together using a separator.

    Args:
    *lists: one or more lists to concatenate.
    sep: a string separator used to join the lists. Defaults to '-'.

    Returns:
    A new list that contains all of the items from the input lists,
    joined together with the specified separator.
    """
    if not lists:
        return None
    else:
        concat_lists = lists[0]
        for lst in lists[1:]:
            concat_lists = concat_lists + [sep] + lst
    return concat_lists

