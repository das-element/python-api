from daselement_api import api as de

# [optional] overwrite config file path
# de.config = '/some/path/to/config/das-element.conf'

library_path = '/some/path/das-element.lib'

# get element by database ID
element_id = 1
entity = de.get_element_by_id(library_path, element_id)
print(entity)

# get element by element name
element_name = 'fire_00001'
entity = de.get_element_by_name(library_path, element_name)
print(entity)

# get element by element unique ID (uuid)
element_uuid = '33f685064c1740b1986932cf8f3cf1f4'
entity = de.get_element_by_uuid(library_path, element_uuid)
print(entity)
