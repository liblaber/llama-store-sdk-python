from os import getenv
from pprint import pprint
from llamastore import Llamastore

sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))

results = sdk.llama.get_llamas()

pprint(vars(results))
