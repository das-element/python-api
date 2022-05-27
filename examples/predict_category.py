from daselement_api import api as de

# [optional] overwrite config file path
# de.config = '/some/path/to/config/das-element.conf'

path = '/mnt/media/some/folder'
result = de.predict(path)
print(result)
