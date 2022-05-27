from daselement_api import api as de

# [optional] overwrite config file path
# de.config = '/some/path/to/config/das-element.conf'

library_path = '/some/path/das-element.lib'
mapping = 'copy & rename'
path = '/some/folder/files.1001-1099#.exr'
category = 'Q235544'  #  or: 'flame'
tags = ['Q3196', 'foo', 'bar']

entity = de.ingest(library_path, mapping, path, category, tags)
print(entity)
print(entity.get('path'))