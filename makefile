.PHONY: all install start clean

all: install start

install:
	touch petitprince.txt
	@if [ ! -d ".venv" ]; then \
		python3 -m venv .venv; \
	fi
	. .venv/bin/activate && \
	pip install boto3 pdfplumber ollama openai torch dropbox && \
	ollama pull llama3.2 &&\
	ollama pull mxbai-embed-large &&\
	python3 upload.py

start:
	. .venv/bin/activate && \
	python3 localrag.py

clean:
	rm -rf .venv petitprince.txt