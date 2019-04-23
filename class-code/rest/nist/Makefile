define terminal
	osascript -e 'tell application "Terminal" to do script "cd $(PWD); $1"'
endef

install:
	pip install -r requirements.txt


demo:
	$(call terminal, python server.py)
	sleep 3
	@echo "==============================================================================="
	@echo "Get the info"
	@echo "==============================================================================="
	curl http://localhost:8080/cloudmesh/cpu
	@echo
	@echo "==============================================================================="

