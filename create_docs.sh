. venv/bin/activate
mkdir -p docs
cp docs_template/das-element_logo_docu_api_b.png docs/
cp docs_template/das-element_logo_docu_api_w.png docs/
pdoc daselement_api/api.py --logo "das-element_logo_docu_api_b.png" -t docs_template -o docs
