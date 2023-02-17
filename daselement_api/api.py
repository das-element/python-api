#           __                   __                          __
#      ____/ /___ ______   ___  / /__  ____ ___  ___  ____  / /_
#     / __  / __ `/ ___/  / _ \/ / _ \/ __ `__ \/ _ \/ __ \/ __/
#    / /_/ / /_/ (__  )  /  __/ /  __/ / / / / /  __/ / / / /_
#    \__,_/\__,_/____/   \___/_/\___/_/ /_/ /_/\___/_/ /_/\__/
#
#                  Copyright (c) 2022 das element
'''
## Documentation for the API

API works for both Python 2 & 3

Available in version **1.2+**


---

### Install

[Download](https://github.com/das-element/python-api) folder: `daselement_api`

In the background the CLI version of _das element_ is exectued.  
Please link the correct executable **das-element-cli** in the file **daselement_api/manager.py**

```
from daselement_api import api as de
libraries = de.get_libraries()
for library, library_config_data in libraries.items():
   print(library)
   print(library_config_data)
```

---

The library information is taken from the config file that is set for the current workstation.  
Either defined in the `~/.das-element/setup.ini` file or by the environment variable `DASELEMENT_CONFIG_PATH`

'''

from .manager import execute_command, as_quoted_string, as_quoted_dict

config = None
'''
Variabel to define a custom config file path (.conf)

---
'''


def get_libraries():
    '''
    Get all libraries data for current config.

    **Returns**:
    > - Dict[str, Dict]: *Key is the library file path (.lib) - Value is the library data*

    **Example code**:
    ```
    from daselement_api import api as de

    libraries = de.get_libraries()
    for library, library_config_data in libraries.items():
        print(library)
        print(library_config_data)
    ```
    '''
    command = ['--config', config] if config else []
    command += ['get-libraries']
    return execute_command(command)


def get_library_template_mappings(library_path):
    '''
    Get all template mappings data for library.

    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*

    **Returns**:
    > - List[Dict]

    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'

    template_mappings = de.get_library_template_mappings(library_path)
    for template_mapping in template_mappings:
        print(template_mapping)
    ```

    **Example result**:
    `[{'key': 'copy & rename', 'value': {'extra': ['extra-job'], 'filmstrip': 'filmstrip', 'main': 'main', 'proxy': 'proxy mov', 'thumbnail': 'thumbnail'}}]`
    '''
    command = ['--config', config] if config else []
    command += [
        'get-library-template-mappings',
        as_quoted_string(library_path)
    ]
    return execute_command(command)


def get_categories(library_path):
    '''
    Get all categories from the database for the library.

    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*

    **Returns**:
    > - List[Dict]

    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'

    categories = de.get_categories(library_path)
    for category in categories:
        print(category)
    ```

    **Example result**:
    `[{'id': 'Q235544', 'type': 'default', 'name': 'flame', 'child_count': 5, 'child_counter': 5, 'parents': [{'description': 'rapid oxidation of a material; phenomenon that emits light and heat', 'id': 'Q3196', 'name': 'fire', 'synonyms': [{'language': 'en', 'value': 'fire'}, {'language': 'en', 'value': 'fires'}], 'type': 'default'}], 'children': [{'id': 'Q327954', 'name': 'torch'}], 'synonyms': [{'language': 'en', 'value': 'flame'}]}]`
    '''
    command = ['--config', config] if config else []
    command += ['get-categories', as_quoted_string(library_path)]
    return execute_command(command)


def get_category(library_path, category_value):
    '''
    Get category entity from the database for the library.

    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*
    > - **category_value** (str): *the ID ('Q3196') or name ('fire') of the category in the database*

    **Returns**:
    > - Dict[str, Union[str, int]]: *child_count: actual number of children - child_counter: increasing counter, even if children get deleted*



    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'

    category_entity = de.get_category(library_path, 'Q3196')
    category_entity = de.get_category(library_path, 'fire')
    ```

    **Example result**:
    `{"id": "Q3196", "type": "default", "name": "fire", "child_count": 130, "child_counter": 135}`
    '''
    command = ['--config', config] if config else []
    command += ['get-category', as_quoted_string(library_path), as_quoted_string(category_value)]
    return execute_command(command)


def get_tags(library_path):
    '''
    Get all tags from the database for the library.

    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*

    **Returns**:
    > - List[Dict]

    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'

    tags = de.get_tags(library_path)
    for tag in tags:
        print(tag)
    ```

    **Example result**:
    `[{'id': 'Q235544', 'name': 'flame', 'type': 'default', 'elements_count': 3, 'synonyms': [{'language': 'en', 'value': 'flame'}]}]`
    '''
    command = ['--config', config] if config else []
    command += ['get-tags', as_quoted_string(library_path)]
    return execute_command(command)

def get_tag(library_path, tag_value):
    '''
    Get tag entity from the database for the library.

    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*
    > - **tag_value** (str): *the ID ('Q3196') or name ('fire') of the tag in the database*

    **Returns**:
    > - Dict[str, Union[str, int]]

    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'

    tag_entity = de.get_tag(library_path, 'Q3196')
    tag_entity = de.get_tag(library_path, 'fire')
    ```

    **Example result**:
    `{"id": "Q3196", "name": "fire", "type": "default", "elements_count": 130}`
    '''
    command = ['--config', config] if config else []
    command += ['get-tag', as_quoted_string(library_path), as_quoted_string(tag_value)]
    return execute_command(command)


def get_elements(library_path):
    '''
    Get all elements from the database for the library.

    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*

    **Returns**:
    > - List[Dict]

    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'

    elements = de.get_elements(library_path)
    for element in elements:
        print(element)
        print(element.get('path'))
    ```

    **Example result**:
    `[{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","popularity": "None","rating": "None","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}]`
    '''
    command = ['--config', config] if config else []
    command += ['get-elements', as_quoted_string(library_path)]
    return execute_command(command)


def get_element_by_id(library_path, element_id):
    '''
    Get element entity based on the **element ID** from the database for the library.

    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*
    > - **element_id** (int): *Element ID in the database*

    **Returns**:
    > - Dict

    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'
    element_id = 1

    element = de.get_element_by_id(library_path, element_id)
    print(element)
    print(element.get('path'))
    ```

    **Example result**:
    `{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","popularity": "None","rating": "None","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}`
    '''
    command = ['--config', config] if config else []
    command += [
        'get-element-by-id',
        as_quoted_string(library_path), element_id
    ]
    return execute_command(command)


def get_element_by_uuid(library_path, element_uuid):
    '''
    Get element entity based on the **element UUID** from the database for the library.
    If no library path is provided, all libraries of the current config will be searched.

    **Args**:
    > - **element_uuid** (str): *Element UUID (unique ID) in the database*
    > - **library_path** (str): **[optional] File path to the library file (.lib)*

    **Returns**:
    > - Dict

    **Example code**:
    ```
    from daselement_api import api as de

    element_uuid = '9947c549c6014a3ca831983275884051'
    library_path = '/some/path/das-element.lib'  # optional

    element = de.get_element_by_uuid(element_uuid, library_path=library_path)
    print(element)
    print(element.get('path'))
    ```

    **Example result**:
    `{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","popularity": "None","rating": "None","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}`
    '''
    command = ['--config', config] if config else []
    command += ['get-element-by-uuid', element_uuid,]
    if library_path:
        command += ['--library', as_quoted_string(library_path)]
    return execute_command(command)


def get_element_by_name(library_path, element_name):
    '''
    Get element entity based on the **element name** from the database for the library.

    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*
    > - **element_name** (str): *Element name in the database*

    **Returns**:
    > - Dict

    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'
    element_name = 'fire_00001'

    element = de.get_element_by_name(library_path, element_name)
    print(element)
    print(element.get('path'))
    ```

    **Example result**:
    `{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","popularity": "None","rating": "None","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}`
    '''
    command = ['--config', config] if config else []
    command += [
        'get-element-by-name',
        as_quoted_string(library_path), element_name
    ]
    return execute_command(command)


def update(library_path, entity_type, entity_id, data):
    '''
    Updates database entity with new data


    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*
    > - **entity_type** (str): *Type of entity to update. Options: [Category, Element, Tag]*
    > - **entity_id** (Union[str, int]): *the ID of the entity to update in the database*
    > - **data** (Dict): *data to update. Dictionary with key/value pairs formated as JSON.*  
        *Example:* `"{\\\"rating\\\": 3}"`

    **Returns**:
    > - Dict: *Entity of the updated entity*

    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'
    entity_type = 'Element'
    entity_id = 23
    new_data = {'category_id': 'Q327954',  # or: 'category': 'torch',
                'tags': ['flame', 'fire', 'torch', 'something custom tag']}

    entity = de.update(library_path, entity_type, entity_id, new_data)
    print(entity)
    print(entity.get('rating'))
    ```

    **Example result**:
    `{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","popularity": "None","rating": "None","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}, {"id": "something","name": "something custom tag", "type": "custom", "elements_count": 1}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}`

    **Example command line command**:  
    ##### Windows  
    `das-element-cli.exe update C:\\mnt\\library\\das-element.lib element 1 "{\\\"rating\\\": 3}"`  
    ##### Linux/MacOS  
    `das-element-cli update /mnt/library/das-element.lib element 1 '{\"rating\": 3}'`
    '''
    command = ['--config', config] if config else []
    command += [
        'update',
        as_quoted_string(library_path),
        as_quoted_string(entity_type),
        as_quoted_string(entity_id),
        as_quoted_dict(data)
    ]
    return execute_command(command)


def ingest(library_path, mapping, path, category, tags=[]):
    '''
    Ingest a new element to the library

    Ingesting a file sequence requires the path to be in a [fileseq.FileSequence notation](https://github.com/justinfx/fileseq#filesequence)  
    Thank you to the developers of [fileseq](https://github.com/justinfx/fileseq)!

    Example: `/some/folder/files.1001-1099#.exr`


    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*
    > - **mapping** (str): *Name of the transcoding mapping used to ingest*
    > - **path** (str): *File path to the new element*
    > - **category** (str): *Category name of new element (can be WikiData-ID or human-readable text)*
    > - **tags** (List[str]): *[optional] List of tags*

    **Returns**:
    > - Dict: *Element entity for the newly created element*

    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'
    mapping = 'copy & rename'
    path = '/some/folder/files.1001-1099#.exr'
    category = 'Q235544'  #  or: 'flame'
    tags = ['Q3196', 'foo', 'bar']

    entity = de.ingest(library_path, mapping, path, category, tags)
    print(entity)
    print(entity.get('path'))
    ```

    **Example result**:
    `{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","popularity": "None","rating": "None","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}`

    **Example command line command**:
    `das-element-cli ingest --library /mnt/library/das-element.lib --mapping "copy & rename" --path /some/file/path.1001-1099#.exr --category Q235544 --tags Q3196,foo,bar`
    '''
    command = ['--config', config] if config else []
    command += [
        'ingest', '--library',
        as_quoted_string(library_path), '--mapping',
        as_quoted_string(mapping), '--path',
        as_quoted_string(path), '--category',
        as_quoted_string(category), '--tags',
        as_quoted_string(','.join(tags))
    ]
    return execute_command(command)


def predict(path, model=None, top=2, filmstrip_frames=36):
    '''
    Predict the category for a give file path.

    The give path can be a file or a directory.  
    If a directory is provided, all sub-directories will be searched for files and sequences.


    **Args**:

    > - **model** (str): [optional] *Define a custom model file path (.wit)*
    > - **filmstrip_frames** (int): [optional] *Number of frames to validated for a movie file or sequence. The higher the number, the better the result might be, but it also takes longer*
    > - **top** (int): [optional] *Return the top X predictions*


    **Returns**:
    > - Dict[str, List[Dict]]: *Key is the file path. The value a list of predicted categories*


    **Example result**:
    `{"/some/file/path.1001-1099#.exr": [{"tag": "flame", "description": "visible, gaseous part of a fire", "id": "Q235544", "value": "Q235544", "parents": [{"description": "rapid oxidation of a material; phenomenon that emits light and heat", "id": "Q3196", "name": "fire", "synonyms": [{"language": "en", "value": "fire"}, {"language": "en", "value": "fires"}}]}]}`


    **Example command line command**:
    `das-element-cli predict --top=2 /some/file/path`

    '''
    command = ['predict', '--top', top, '--filmstrip_frames', filmstrip_frames]

    if model:
        command += ['--model', as_quoted_string(model)]

    command += [path]
    return execute_command(command)


def get_paths_from_disk(path, as_sequence=True):
    '''
    Recursivly searches for files and sequences in a given directory. Since version 1.2.5

    The give path can be a file or a directory.  
    If a directory is provided, all sub-directories will be searched for files and sequences.


    **Args**:

    > - **as_sequence / as_single_files** (bool): [optional] defines if files with a sequential naming should be detected as a file sequence or individual files**


    **Returns**:
    > - List[str]: *List of file paths found in the give directory*


    **Example result**:
    `["/some/file/path.1001-1099#.exr", "/other/path.mov"]`


    **Example command line command**:
    `das-element-cli get-paths-from-disk --as_sequence /some/file/path`

    '''
    command = ['get-paths-from-disk']

    if as_sequence:
        command += ['--as_sequence']
    else:
        command += ['--as_single_files']

    command += [path]
    return execute_command(command)
