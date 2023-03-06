import os


def the_way(path):
    """
    the function gets a path and returns a list of files that start  with "deep" located in the given path.
    :param path: path of the directory to be searched
    :return: a list of files that start with "deep" and located in the given path.
    """
    deep_files = []
    for file in os.listdir(path):
        if file.startswith("deep"):
            deep_files.append(file)
    return deep_files
