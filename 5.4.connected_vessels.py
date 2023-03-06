def interleave(*iterables):
    """
    Interleaves the elements of multiple iterables into a single list.
    :param iterables:one or more iterables to interleave.
    :return:A list of the interleaved elements.
    """
    # Determine the length of the longest iterable
    max_length = max(len(it) for it in iterables)
    connected_vessels_lst = []
    for i in range(max_length):
        for it in iterables:
            if len(it) > i:
                connected_vessels_lst.append(it[i])
    return connected_vessels_lst


def interleave_generator(*iterables):
    """
    Interleaves the elements of multiple iterables into one list using generator.
    :param iterables: one or more iterables to interleave.
    :yields:A generator that produces the interleaved elements.
    """
    max_length = max(len(it) for it in iterables)
    connected_vessels_lst = []
    for i in range(max_length):
        for it in iterables:
            if len(it) > i:
                connected_vessels_lst.append(it[i])
                yield connected_vessels_lst



