. venv/bin/activate
mkdir -p docs
pdoc daselement_api/api.py --logo "https://github.com/das-element/python-api/raw/main/das-element_logo_docu_api.png" -o docs
