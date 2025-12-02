#           __                   __                          __
#      ____/ /___ ______   ___  / /__  ____ ___  ___  ____  / /_
#     / __  / __ `/ ___/  / _ \/ / _ \/ __ `__ \/ _ \/ __ \/ __/
#    / /_/ / /_/ (__  )  /  __/ /  __/ / / / / /  __/ / / / /_
#    \__,_/\__,_/____/   \___/_/\___/_/ /_/ /_/\___/_/ /_/\__/
#
#                  Copyright (c) 2025 das element
'''
## Das Element Python API

API works for both Python 2 & 3


---
<br/>
### Install

In your Python environment run the command:

```bash
pip install daselement-api
```

<br/>

### Configuration

In the background the CLI version of Das Element is executed.  
Set the environment variables to point to the CLI executable files:
<br/><br/>
`DASELEMENT_CLI` (for the small CLI version)  
`DASELEMENT_CLI_FULL` (for the full CLI version)  
<br/><br/>

### Usage

```python
from daselement_api import api as de
libraries = de.get_libraries()
for library, library_config_data in libraries.items():
   print(library)
   print(library_config_data)
```

<br/>
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


def create_config(config_path, preset_key='blank', preset_path=None):
    '''
    Create a new config file. Provide the preset key or file path to a config preset.

    **Args**:
    > - **config_path** (str): *File path to the config .conf file*
    > - **preset_key** (str): *[optional] Default preset key. Options: blank | preserve_structure | restructure_comprehensive | restructure_selective*
    > - **preset_path** (str): *[optional] File path to config preset file*

    **Returns**:
    > - bool: *Result of config creation*

    **Example code**:
    ```
    from daselement_api import api as de

    config_path = '/some/path/my-config.conf'
    preset_key = 'blank'  # or 'preserve_structure', 'restructure_comprehensive', 'restructure_selective'
    preset_path = '/some/path/preset.conf'  # optional

    result = de.create_config(config_path, preset_key=preset_key)

    # with custom preset file
    result = de.create_config(config_path, preset_path=preset_path)
    ```

    **Example result**:
    `true`

    **Example command line command**:
    `das-element-cli create-config /some/path/my-config.conf --preset_key blank`
    `das-element-cli create-config /some/path/my-config.conf --preset_path /some/path/preset.conf`
    '''
    command = ['create-config']
    command += ['--preset_key', as_quoted_string(preset_key)]

    if preset_path:
        command += ['--preset_path', as_quoted_string(preset_path)]

    command += [as_quoted_string(config_path)]

    return execute_command(command, cli_full=True)


def get_config_presets():
    '''
    Get all available config presets.

    **Returns**:
    > - List[Dict]: *List of available config presets*

    **Example code**:
    ```
    from daselement_api import api as de

    presets = de.get_config_presets()
    for preset in presets:
        print(preset)
    ```

    **Example result**:
    `[{'key': 'blank', 'name': 'Blank Config', 'description': 'Creates a blank configuration file'}, {'key': 'preserve_structure', 'name': 'Preserve Structure', 'description': 'Preserves existing folder structure'}, {'key': 'restructure_comprehensive', 'name': 'Comprehensive Restructure', 'description': 'Complete restructuring of the library'}, {'key': 'restructure_selective', 'name': 'Selective Restructure', 'description': 'Selective restructuring based on criteria'}]`

    **Example command line command**:
    `das-element-cli get-config-presets`
    '''
    command = ['get-config-presets']
    return execute_command(command, cli_full=True)


def get_library_presets():
    '''
    Get all available library presets.

    **Returns**:
    > - List[Dict]: *List of available library presets*

    **Example code**:
    ```
    from daselement_api import api as de

    presets = de.get_library_presets()
    for preset in presets:
        print(preset)
    ```

    **Example result**:
    `[{'key': 'basic', 'name': 'Basic Library', 'description': 'Basic library setup with standard templates'}, {'key': 'advanced', 'name': 'Advanced Library', 'description': 'Advanced library setup with comprehensive templates'}, {'key': 'custom', 'name': 'Custom Library', 'description': 'Custom library setup for specific workflows'}]`

    **Example command line command**:
    `das-element-cli get-library-presets`
    '''
    command = ['get-library-presets']
    return execute_command(command, cli_full=True)


def create_library(library_path,
                   name=None,
                   path_lin=None,
                   path_mac=None,
                   path_win=None,
                   root=None,
                   root_lin=None,
                   root_mac=None,
                   root_win=None,
                   preset_key='blank',
                   preset_path=None,
                   create_defaults=True,
                   db_type=None,
                   db_path=None,
                   db_path_lin=None,
                   db_path_mac=None,
                   db_path_win=None,
                   db_user=None,
                   db_password=None,
                   db_uri=None,
                   db_port=None,
                   db_name=None,
                   db_sslmode='disable',
                   db_sslcert=None,
                   db_sslcert_lin=None,
                   db_sslcert_mac=None,
                   db_sslcert_win=None,
                   db_sslkey=None,
                   db_sslkey_lin=None,
                   db_sslkey_mac=None,
                   db_sslkey_win=None,
                   db_sslrootcert=None,
                   db_sslrootcert_lin=None,
                   db_sslrootcert_mac=None,
                   db_sslrootcert_win=None,
                   db_sslca=None,
                   db_sslca_lin=None,
                   db_sslca_mac=None,
                   db_sslca_win=None):
    '''
    Create a new library and database.

    **Args**:
    > - **library_path** (str): *File path to library (.lib) file for current OS*
    > - **name** (str): *[optional] Library name*
    > - **path_lin** (str): *[optional] File path to library (.lib) file for Linux*
    > - **path_mac** (str): *[optional] File path to library (.lib) file for MacOS*
    > - **path_win** (str): *[optional] File path to library (.lib) file for Windows*
    > - **root** (str): *[optional] Library root path for current OS*
    > - **root_lin** (str): *[optional] Library root path for Linux*
    > - **root_mac** (str): *[optional] Library root path for MacOS*
    > - **root_win** (str): *[optional] Library root path for Windows*
    > - **preset_key** (str): *[optional] Default preset key. Options: blank | preserve_structure | restructure_comprehensive | restructure_selective*
    > - **preset_path** (str): *[optional] File path to library preset file*
    > - **create_defaults** (bool): *[optional] Create default tags and categories*
    > - **db_type** (str): *Type of database. Options: sqlite | postgres | mysql*
    > - **db_path** (str): *[optional] SQLite only: Database path for current OS*
    > - **db_path_lin** (str): *[optional] SQLite only: Database path for Linux*
    > - **db_path_mac** (str): *[optional] SQLite only: Database path for MacOS*
    > - **db_path_win** (str): *[optional] SQLite only: Database path for Windows*
    > - **db_user** (str): *[optional] Server-side database: Database user name*
    > - **db_password** (str): *[optional] Server-side database: Database user password*
    > - **db_uri** (str): *[optional] Server-side database: Database host URI*
    > - **db_port** (int): *[optional] Server-side database: Database host port*
    > - **db_name** (str): *[optional] Server-side database: Database name of library*
    > - **db_sslmode** (str): *[optional] SSL encryption mode*
    > - **db_sslcert** (str): *[optional] Client certificate/public key for current OS*
    > - **db_sslcert_lin** (str): *[optional] Client certificate/public key for Linux*
    > - **db_sslcert_mac** (str): *[optional] Client certificate/public key for MacOS*
    > - **db_sslcert_win** (str): *[optional] Client certificate/public key for Windows*
    > - **db_sslkey** (str): *[optional] Client certificate key/private key for current OS*
    > - **db_sslkey_lin** (str): *[optional] Client certificate key/private key for Linux*
    > - **db_sslkey_mac** (str): *[optional] Client certificate key/private key for MacOS*
    > - **db_sslkey_win** (str): *[optional] Client certificate key/private key for Windows*
    > - **db_sslrootcert** (str): *[optional] PostgreSQL only: Root certificate file for current OS*
    > - **db_sslrootcert_lin** (str): *[optional] PostgreSQL only: Root certificate file for Linux*
    > - **db_sslrootcert_mac** (str): *[optional] PostgreSQL only: Root certificate file for MacOS*
    > - **db_sslrootcert_win** (str): *[optional] PostgreSQL only: Root certificate file for Windows*
    > - **db_sslca** (str): *[optional] MySQL/MariaDB only: Certificate Authority file for current OS*
    > - **db_sslca_lin** (str): *[optional] MySQL/MariaDB only: Certificate Authority file for Linux*
    > - **db_sslca_mac** (str): *[optional] MySQL/MariaDB only: Certificate Authority file for MacOS*
    > - **db_sslca_win** (str): *[optional] MySQL/MariaDB only: Certificate Authority file for Windows*

    **Returns**:
    > - bool: *Result of library creation*

    **Example code**:
    ```
    from daselement_api import api as de

    # SQLite example
    result = de.create_library(
        library_path='/mnt/library/das-element.lib',
        name='My Library',
        root='/mnt/library',
        db_type='sqlite',
        db_path='/mnt/library/das-element.db',
        preset_key='preserve_structure'
    )

    # PostgreSQL example
    result = de.create_library(
        library_path='/mnt/library/das-element.lib',
        name='My Library',
        root='/mnt/library',
        db_type='postgres',
        db_user='user',
        db_password='password',
        db_uri='my-database',
        db_port=5432,
        db_name='my_library'
    )
    ```

    **Example result**:
    `true`

    **Example command line command**:
    `das-element-cli create-library --path /mnt/library/das-element.lib --root /mnt/library --db_type sqlite --db_path /mnt/library/das-element.db --preset_key preserve_structure`
    '''
    command = ['create-library']

    if name:
        command += ['--name', as_quoted_string(name)]

    command += ['--path', as_quoted_string(library_path)]

    if path_lin:
        command += ['--path_lin', as_quoted_string(path_lin)]
    if path_mac:
        command += ['--path_mac', as_quoted_string(path_mac)]
    if path_win:
        command += ['--path_win', as_quoted_string(path_win)]

    if root:
        command += ['--root', as_quoted_string(root)]
    if root_lin:
        command += ['--root_lin', as_quoted_string(root_lin)]
    if root_mac:
        command += ['--root_mac', as_quoted_string(root_mac)]
    if root_win:
        command += ['--root_win', as_quoted_string(root_win)]

    command += ['--preset_key', as_quoted_string(preset_key)]

    if preset_path:
        command += ['--preset_path', as_quoted_string(preset_path)]

    if create_defaults is not None:
        command += ['--create_defaults', str(create_defaults).lower()]

    if db_type:
        command += ['--db_type', as_quoted_string(db_type)]

    # SQLite database options
    if db_path:
        command += ['--db_path', as_quoted_string(db_path)]
    if db_path_lin:
        command += ['--db_path_lin', as_quoted_string(db_path_lin)]
    if db_path_mac:
        command += ['--db_path_mac', as_quoted_string(db_path_mac)]
    if db_path_win:
        command += ['--db_path_win', as_quoted_string(db_path_win)]

    # Server-side database options
    if db_user:
        command += ['--db_user', as_quoted_string(db_user)]
    if db_password:
        command += ['--db_password', as_quoted_string(db_password)]
    if db_uri:
        command += ['--db_uri', as_quoted_string(db_uri)]
    if db_port:
        command += ['--db_port', str(db_port)]
    if db_name:
        command += ['--db_name', as_quoted_string(db_name)]

    # SSL options / ignore for SQLite
    if db_sslmode and db_type.lower() != 'sqlite':
        command += ['--db_sslmode', as_quoted_string(db_sslmode)]

    if db_sslcert:
        command += ['--db_sslcert', as_quoted_string(db_sslcert)]
    if db_sslcert_lin:
        command += ['--db_sslcert_lin', as_quoted_string(db_sslcert_lin)]
    if db_sslcert_mac:
        command += ['--db_sslcert_mac', as_quoted_string(db_sslcert_mac)]
    if db_sslcert_win:
        command += ['--db_sslcert_win', as_quoted_string(db_sslcert_win)]

    if db_sslkey:
        command += ['--db_sslkey', as_quoted_string(db_sslkey)]
    if db_sslkey_lin:
        command += ['--db_sslkey_lin', as_quoted_string(db_sslkey_lin)]
    if db_sslkey_mac:
        command += ['--db_sslkey_mac', as_quoted_string(db_sslkey_mac)]
    if db_sslkey_win:
        command += ['--db_sslkey_win', as_quoted_string(db_sslkey_win)]

    # PostgreSQL SSL options
    if db_sslrootcert:
        command += ['--db_sslrootcert', as_quoted_string(db_sslrootcert)]
    if db_sslrootcert_lin:
        command += [
            '--db_sslrootcert_lin',
            as_quoted_string(db_sslrootcert_lin)
        ]
    if db_sslrootcert_mac:
        command += [
            '--db_sslrootcert_mac',
            as_quoted_string(db_sslrootcert_mac)
        ]
    if db_sslrootcert_win:
        command += [
            '--db_sslrootcert_win',
            as_quoted_string(db_sslrootcert_win)
        ]

    # MySQL/MariaDB SSL options
    if db_sslca:
        command += ['--db_sslca', as_quoted_string(db_sslca)]
    if db_sslca_lin:
        command += ['--db_sslca_lin', as_quoted_string(db_sslca_lin)]
    if db_sslca_mac:
        command += ['--db_sslca_mac', as_quoted_string(db_sslca_mac)]
    if db_sslca_win:
        command += ['--db_sslca_win', as_quoted_string(db_sslca_win)]

    return execute_command(command, cli_full=True)


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
    command += [
        'get-category',
        as_quoted_string(library_path),
        as_quoted_string(category_value)
    ]
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
    command += [
        'get-tag',
        as_quoted_string(library_path),
        as_quoted_string(tag_value)
    ]
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
    `[{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","rating": "3","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}]`
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
    `{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","rating": "3","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}`
    '''
    command = ['--config', config] if config else []
    command += [
        'get-element-by-id',
        as_quoted_string(library_path), element_id
    ]
    return execute_command(command)


def get_element_by_uuid(element_uuid, library_path=None):
    '''
    Get element entity based on the **element UUID** from the database for the library.
    If no library path is provided, all libraries of the current config will be searched.

    **Args**:
    > - **library_path** (str): *[optional] File path to the library file (.lib)*
    > - **element_uuid** (str): *Element UUID (unique ID) in the database*

    **Returns**:
    > - Dict

    **Example code**:
    ```
    from daselement_api import api as de

    element_uuid = '9947c549c6014a3ca831983275884051'
    library_path = '/some/path/das-element.lib'  # optional

    element = de.get_element_by_uuid(element_uuid, library_path=library_path)

    # without the library path each linked library in the config file will searched
    element = de.get_element_by_uuid(element_uuid)

    print(element)
    print(element.get('path'))
    ```

    **Example result**:
    `{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","rating": "3","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}`
    '''
    command = ['--config', config] if config else []
    command += ['get-element-by-uuid', element_uuid]
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
    `{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","rating": "3","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}`
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
                'tags': ['flame', 'fire', 'torch', 'something custom tag'],
                'metadata': {'foo': 'bar'}}

    entity = de.update(library_path, entity_type, entity_id, new_data)
    print(entity)
    print(entity.get('rating'))
    ```

    **Example result**:
    `{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","rating": "3","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}, {"id": "something","name": "something custom tag", "type": "custom", "elements_count": 1}],"uuid": "9947c549c6014a3ca831983275884051","width": 3342}`

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


def delete_element(element_uuid,
                   delete_from_database=False,
                   delete_from_disk=False,
                   delete_proxy=False,
                   library_path=None):
    '''
    Deletes an element entity based on the **element UUID**.
    The options define what gets deleted. Either the database record, main and/or proxy files on disk, or both.

    **Args**:
    > - **element_uuid** (str): *Element UUID (unique ID) in the database*
    > - **delete_from_database** (bool): *[optional] delete data from the database*
    > - **delete_from_disk** (bool): *[optional] delete all element files from disk*
    > - **delete_proxy** (bool): *[optional] delete only element proxy files from disk*
    > - **library_path** (str): *[optional] File path to the library file (.lib)*

    **Returns**:
    > - bool

    **Example code**:
    ```
    from daselement_api import api as de

    element_uuid = '9947c549c6014a3ca831983275884051'
    delete_from_database = True
    delete_from_disk = True
    delete_proxy = True
    library_path = '/some/path/das-element.lib'  # optional

    de.delete_element(element_uuid, delete_from_database, delete_from_disk, delete_proxy, library_path=library_path)

    ```

    **Example result**:
    `true`
    '''
    command = ['--config', config] if config else []
    command += [
        'delete-element',
        element_uuid,
    ]
    if delete_from_database:
        command += ['--database']
    if delete_from_disk:
        command += ['--disk']
    if delete_proxy:
        command += ['--proxy']
    if library_path:
        command += ['--library', as_quoted_string(library_path)]
    return execute_command(command, cli_full=True)


def delete_elements(element_uuids,
                    delete_from_database=False,
                    delete_from_disk=False,
                    delete_proxy=False,
                    library_path=None):
    '''
    Deletes multiple element entities based on a list of **element UUIDs**.
    The options define what gets deleted. Either the database record, main and/or proxy files on disk, or both.

    **Args**:
    > - **element_uuids** (List[str]): *List of Element UUIDs (unique IDs) in the database*
    > - **delete_from_database** (bool): *[optional] delete data from the database*
    > - **delete_from_disk** (bool): *[optional] delete all element files from disk*
    > - **delete_proxy** (bool): *[optional] delete only element proxy files from disk*
    > - **library_path** (str): *[optional] File path to the library file (.lib)*

    **Returns**:
    > - bool

    **Example code**:
    ```
    from daselement_api import api as de

    element_uuids = ['8747c549ab344a3798405135ca831288', '9947c549c6014a3ca831983275884051']
    delete_from_database = True
    delete_from_disk = True
    delete_proxy = True
    library_path = '/some/path/das-element.lib'  # optional

    de.delete_elements(element_uuids, delete_from_database, delete_from_disk, delete_proxy, library_path=library_path)

    ```

    **Example result**:
    `true`
    '''
    command = ['--config', config] if config else []
    command += ['delete-elements']
    if delete_from_database:
        command += ['--database']
    if delete_from_disk:
        command += ['--disk']
    if delete_proxy:
        command += ['--proxy']
    if library_path:
        command += ['--library', as_quoted_string(library_path)]
    command += [as_quoted_string(','.join(element_uuids))]
    return execute_command(command, cli_full=True)


def ingest(library_path,
           mapping,
           path,
           category,
           colorspace='',
           path_thumbnail='',
           path_proxy='',
           tags=[],
           media_type='',
           permission='111',
           metadata={},
           additionals=[]):
    '''
    Ingest a new element to the library

    Ingesting a file sequence requires the path to be in a [fileseq.FileSequence notation](https://github.com/justinfx/fileseq#filesequence)  
    Thank you to the developers of [fileseq](https://github.com/justinfx/fileseq)!

    Example: `/some/folder/files.1001-1099#.exr`


    **Args**:
    > - **library_path** (str): *File path to the library file (.lib)*
    > - **mapping** (str): *Name of the transcoding mapping used to ingest*
    > - **path** (str): *File path to the new element*
    > - **path_thumbnail** (str): *[optional] File path to custom thumbnail*
    > - **path_proxy** (str): *[optional] File path to custom proxy. Movie file, OBJ or FBX*
    > - **category** (str): *Category name of new element (can be WikiData-ID or human-readable text)*
    > - **colorspace** (str): *[optional] Colorspace name*
    > - **tags** (List[str]): *[optional] List of tags*
    > - **media_type** (str): *[optional] Media type of element. Valid options: image, sequence, movie, sphere, pdf, project-file, 3d-model, 3d-scene, generic*
    > - **permission** (str): *[optional] Permission flag*
    > - **metadata** (Dict[str, str]): *[optional] List of metadata as: {key:value}*
    > - **additionals** (List[Dict[str, str]]): *[optional] List of additionals. Provide additional as: /path type name*

    **Returns**:
    > - Dict: *Element entity for the newly created element*

    **Example code**:
    ```
    from daselement_api import api as de

    library_path = '/some/path/das-element.lib'
    mapping = 'copy & rename'
    path = '/some/folder/files.1001-1099#.exr'
    path_thumbnail = '/some/folder/custom_thumbnail.jpg'
    path_proxy = '/some/folder/custom_proxy.mov'
    category = 'Q235544'  #  or: 'flame'
    colorspace = 'ACES2065-1'
    tags = ['Q3196', 'foo', 'bar']
    media_type = 'sequence'
    permission = '110'
    metadata = {'foo': 'bar', 'bar': 'buz huz'}
    additionals = [{'path': '/file/additional.exr', 'type': 'texture', 'name': 'alpha'}]

    entity = de.ingest(library_path, mapping, path, category, colorspace=colorspace, path_thumbnail=path_thumbnail, path_proxy=path_proxy, tags=tags, media_type=media_type, permission=permission, metadata=metadata, additionals=additionals)
    print(entity)
    print(entity.get('path'))
    ```

    **Example result**:
    `{"category": {"child_counter": 1,"description": "stick with a flaming end used as a source of light","id": "Q327954","name": "torch","type": "default"},"category_id": "Q327954","channel": 3,"colorspace": "sRGB","colorspace_source": "sRGB","created_at": "2022-05-16T08:26:52.854774","feature_id": 1,"frame_count": 1,"frame_first": 1,"frame_last": 1,"frame_rate": "","height": 5413,"id": 1,"media_type": "image","name": "fire_00001","number": "00001","path": "/mnt/library/fire/fire_00001/main_3342x5413_source/fire_00001.jpg","path_filmstrip": "/mnt/library/fire/fire_00001/filmstrip_11520x270_srgb/fire_00001.jpg","path_proxy": "/mnt/library/fire/fire_00001/proxy_1920x1080_srgb/fire_00001.mov","path_source": "/mnt/source/lication/some-image.jpg","path_thumbnail": "/mnt/library/fire/fire_00001/thumb_960x540_srgb/fire_00001.jpg","pixel_aspect": "1","rating": "3","tags": [{"elements_count": 3,"id": "Q235544","name": "flame","type": "default"},{"elements_count": 56,"id": "Q3196","name": "fire","type": "default"},{"elements_count": 3,"id": "Q327954","name": "torch","type": "default"}],"uuid": "9947c549c6014a3ca831983275884051", "permission": "110", "width": 3342}`

    **Example command line command**:
    `das-element-cli ingest --library /mnt/library/das-element.lib --mapping "copy & rename" --path /some/file/path.%04d.exr --category Q3196 --tags foo,bar,baz --colorspace ACES2065-1 --media_type sequence --metadata foo bar -m lens "70 mm" --path_thumbnail /file/path/thumbnail.jpg --path_proxy /file/path/proxy.mov --additional /path/additional.exr texture alpha`
    '''
    command = ['--config', config] if config else []
    command += [
        'ingest', '--library',
        as_quoted_string(library_path), '--mapping',
        as_quoted_string(mapping), '--path',
        as_quoted_string(path), '--path_thumbnail',
        as_quoted_string(path_thumbnail), '--path_proxy',
        as_quoted_string(path_proxy), '--category',
        as_quoted_string(category), '--colorspace',
        as_quoted_string(colorspace), '--tags',
        as_quoted_string(','.join(tags)), '--media_type',
        as_quoted_string(media_type), '--permission',
        as_quoted_string(permission)
    ] + [
        item for key_value in metadata.items() for item in
        ['-m',
         as_quoted_string(key_value[0]),
         as_quoted_string(key_value[1])]
    ] + [
        item for additional in additionals for item in [
            '-a',
            as_quoted_string(additional.get('path', '')),
            as_quoted_string(additional.get('type', '')),
            as_quoted_string(additional.get('name', ''))
        ]
    ]

    return execute_command(command, cli_full=True)


def predict(path, model, top=2, filmstrip_frames=36):
    '''
    Predict the category for a give file path.

    The give path can be a file or a directory.  
    If a directory is provided, all sub-directories will be searched for files and sequences.


    **Args**:

    > - **model** (str): *Define a custom model file path (.wit)*
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
    command += ['--model', as_quoted_string(model)]
    command += ['--filmstrip_frames', filmstrip_frames]
    command += ['--top', top]
    command += [as_quoted_string(path)]
    return execute_command(command, cli_full=True)


def get_paths_from_disk(path, as_sequence=True):
    '''
    Recursivly searches for files and sequences in a given directory. Since version 1.2.5

    The give path can be a file or a directory.  
    If a directory is provided, all sub-directories will be searched for files and sequences.


    **Args**:

    > - **as_sequence / as_single_files** (bool): [optional] defines if files with a sequential naming should be detected as a file sequence or individual files


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
    return execute_command(command, cli_full=True)


def get_meaningful_frame(path):
    '''
    Validate meaningful thumbnail frame number for movie file or image sequence


    **Args**:

    > - **path** (str): *file path to movie file or image sequence - single frame of a file sequence can be provided*


    **Returns**:
    > - int: *Returns frame number of meaningful thumbnail frame*


    **Example result**:
    `1042`


    **Example command line command**:
    `das-element-cli get-meaningful-frame /folder/some_file.mov`
    `das-element-cli get-meaningful-frame /folder/frame_sequence.1001.exr`
    `das-element-cli get-meaningful-frame /folder/frame_sequence.####.exr`
    `das-element-cli get-meaningful-frame /folder/frame_sequence.%04d.exr`

    '''
    command = ['get-meaningful-frame', path]

    return execute_command(command, cli_full=True)


def render_element_proxies(element_uuid, mapping, library_path=None):
    '''
    Render the proxy files for an element based on a template mapping

    If the library is provided it will directly try to get to element for that library.
    Otherwise it tries to get the entity each library that's defined in the config.

    **Args**:
    > - **element_uuid** (str): *Element UUID (unique ID) in the database*
    > - **mapping** (str): *name of the template mapping that gets rendered*
    > - **library_path** (str): *[optional] File path to the library file (.lib)*

    **Returns**:
    > - bool: *Result of render jobs*


    **Example result**:
    `true`


    **Example command line command**:
    `das-element-cli render-element-proxies 9947c549c6014a3ca831983275884051 "render proxies" --library /some/path/das-element.lib`

    '''
    command = ['render-element-proxies', element_uuid, mapping]

    if library_path:
        command += ['--library', library_path]

    return execute_command(command, cli_full=True)
