VENV = venv
GENSON := $(VENV)/bin/genson
CODEGEN := $(VENV)/bin/datamodel-codegen

$(VENV):
	python3 -m venv $(VENV)
	venv/bin/pip install --upgrade pip wheel

$(VENV)/installed: $(VENV)
	$(VENV)/bin/pip install -r requirements.txt
	touch venv/installed

$(GENSON): $(VENV)/installed
$(CODEGEN): $(VENV)/installed

dump.json:
	kubectl exec -ti  `kubectl get pods | grep kafkacat | grep Running | awk '{print $1}'` -- kc -o end -q -t ces-enriched-items > dump.json

schema.json: $(GENSON) dump.json
	cat dump.json | $(GENSON) | jq > $@

schema.py: $(CODEGEN) schema.json
	$(CODEGEN)  --input schema.json --input-file-type jsonschema --output schema.py

