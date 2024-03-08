python -m venv .venv
call .venv\Scripts\activate
pip install build
python -m build --outdir dist ..\ 
pip install dist\llamastore-0.0.3-py3-none-any.whl --force-reinstall