import os


def logo_whisperer(path):
    """
    A generator function that reads a file and extracts lowercase character strings five or more characters long
    followed by an exclamation mark (!). Each such string is returned as a separate
    item of the generator.
    :param path: the path to the file to be read.
    :yields strings that containing lowercase characters followed by an exclamation mark (!).
    Only strings with at least 5 characters are yielded.
    """
    if os.path.exists(path):
        file = open(path, 'rb')
        message = ""
        while True:
            b = file.read(20)
            if not b:
                break
            for char in str(b):
                if char.islower():
                    message += char
                elif char == "!" and len(message) >= 5:
                    yield message
                    message = ""
                else:
                    message = ""


