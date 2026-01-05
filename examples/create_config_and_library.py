"""
# Optional: set custom paths to the CLI executables
# can also be done by settings environment variables DASELEMENT_CLI and DASELEMENT_CLI_FULL
from daselement_api import manager as de_manager

de_manager.EXECUTABLE_CLI = '/path/to/das-element-cli_2.2.2_lin'
de_manager.EXECUTABLE_CLI_FULL = '/path/to/das-element-cli-full_2.2.2_lin'
"""

from daselement_api import api as de

# file path to new config file
config_path = '/path/to/library/.daselement/config.conf'

# parameters for new library and database
library_name = 'My Library'
library_root = '/path/to/library'
library_path = '/path/to/library/.daselement/library.lib'
library_database = '/path/to/library/.daselement/library.db'
database_type = 'sqlite'  # options are: 'sqlite' | 'postgresql' | 'mysql'
create_defaults = False  # if True, default tags and categories will be created in the new library

# preset key for config and library for naming convention and transcoding templates
# options: 'blank' | 'preserve_structure' | 'restructure_comprehensive' | 'restructure_selective'
preset_key = 'preserve_structure'

print('> Create config file')
de.create_config(config_path, preset_key=preset_key)

print('> Create library and database')
result = de.create_library(
    library_path=library_path,
    name=library_name,
    root=library_root,
    preset_key=preset_key,
    db_type=database_type,
    db_path=library_database,
    create_defaults=create_defaults,
)

print('> Add library to config')
# after creating the library we need to add it to the config
# for a specific operating system, set the os_platform parameter: 'lin' | 'mac' | 'win'
de.add_library(library_path, os_platform=None)

print('Done')
