pip3 install -r requirements.txt
pip3 install -e src/llamastore/
python3 -m unittest discover -p "test*.py" 
