## Python API

API works for both Python 2 & 3

Available in version **1.2+**

## Install

Download folder: `daselement_api`

In the background the CLI version of _das element_ is exectued.  
Please link the correct executable CLI versions with **EXECUTABLE_CLI** and **EXECUTABLE_CLI_FULL** in the file **daselement_api/manager.py**

```
from daselement_api import api as de
libraries = de.get_libraries()
for library, library_config_data in libraries.items():
   print(library)
   print(library_config_data)
```

## Documentation

Check out the documentation at:
[docu.api.das-element.com](http://docu.api.das-element.com)
