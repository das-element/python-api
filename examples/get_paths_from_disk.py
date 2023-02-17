from daselement_api import api as de

# [optional] overwrite config file path
# de.config = '/some/path/to/config/das-element.conf'

# recursively searches for file(s) and sequences for a given folder

path = '/mnt/media/some/folder'
as_sequence = True  # defines if files with a sequential naming should be detected as a file sequence or individual files
result = de.get_paths_from_disk(path, as_sequence)
print(result)
