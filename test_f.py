import re
from os import walk
from os.path import join


def get_filepaths(directory, desired_format):
    """
    This function will generate the file names in a directory tree by walking the tree either top-down or bottom-up.
    For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple
    (dirpath, dirnames, filenames).
    """
    file_paths = []
    for root, directories, files in walk(directory):
        for filename in files:
            if filename != 'log.txt':
                filepath = join(root, filename)
                regex = '.' + desired_format + '$'
                if re.search(regex, filepath.lower()) is not None:
                    file_paths.append(filepath)
    return file_paths
print(get_filepaths('H:\Fronts\fronts_json','json'))
