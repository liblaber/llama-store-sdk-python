# Llamastore Services
A list of all services and services methods.
- Services

    - [LlamaPicture](#llamapicture)

    - [Llama](#llama)

    - [Token](#token)

    - [User](#user)
- [All Methods](#all-methods)


## LlamaPicture

| Method    | Description|
| :-------- | :----------| 
| [create_llama_picture](#create_llama_picture) | Create Llama Picture |
| [get_llama_picture_by_llama_id](#get_llama_picture_by_llama_id) | Get Llama Picture |
| [delete_llama_picture](#delete_llama_picture) | Delete Llama Picture |
| [update_llama_picture](#update_llama_picture) | Update Llama Picture |


## Llama

| Method    | Description|
| :-------- | :----------| 
| [create_llama](#create_llama) | Create Llama |
| [get_llamas](#get_llamas) | Get Llamas |
| [get_llama_by_id](#get_llama_by_id) | Get Llama |
| [delete_llama](#delete_llama) | Delete Llama |
| [update_llama](#update_llama) | Update Llama |


## Token

| Method    | Description|
| :-------- | :----------| 
| [create_api_token](#create_api_token) | Create Api Token |


## User

| Method    | Description|
| :-------- | :----------| 
| [get_user_by_email](#get_user_by_email) | Get User By Email |
| [register_user](#register_user) | Register User |




## All Methods


### **create_llama_picture**
Create Llama Picture
- HTTP Method: POST
- Endpoint: /llama/{llama_id}/picture

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| llama_id | int | Required | The ID of the llama that this picture is for |
| request_input | object | Optional | Request body. |

**Return Type**

[LlamaId](/src/llamastore/models/README.md#llamaid) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
request_body = {}
results = sdk.llama_picture.create_llama_picture(
	request_input = request_body,
	llama_id = 1
)

pprint(vars(results))

```

### **get_llama_picture_by_llama_id**
Get Llama Picture
- HTTP Method: GET
- Endpoint: /llama/{llama_id}/picture

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| llama_id | int | Required | The ID of the llama to get the picture for |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
results = sdk.llama_picture.get_llama_picture_by_llama_id(llama_id = 2)

pprint(vars(results))

```

### **delete_llama_picture**
Delete Llama Picture
- HTTP Method: DELETE
- Endpoint: /llama/{llama_id}/picture

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| llama_id | int | Required | The ID of the llama to delete the picture for |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
results = sdk.llama_picture.delete_llama_picture(llama_id = 1)

pprint(vars(results))

```

### **update_llama_picture**
Update Llama Picture
- HTTP Method: PUT
- Endpoint: /llama/{llama_id}/picture

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| llama_id | int | Required | The ID of the llama that this picture is for |
| request_input | object | Optional | Request body. |

**Return Type**

[LlamaId](/src/llamastore/models/README.md#llamaid) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
request_body = {}
results = sdk.llama_picture.update_llama_picture(
	request_input = request_body,
	llama_id = 1
)

pprint(vars(results))

```


### **create_llama**
Create Llama
- HTTP Method: POST
- Endpoint: /llama

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [LlamaCreate](/src/llamastore/models/README.md#llamacreate) | Required | Request body. |

**Return Type**

[Llama](/src/llamastore/models/README.md#llama) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
request_body = {
	'age': 5,
	'color': 'brown',
	'name': 'libby the llama',
	'rating': 4
}
results = sdk.llama.create_llama(request_input = request_body)

pprint(vars(results))

```

### **get_llamas**
Get Llamas
- HTTP Method: GET
- Endpoint: /llama

**Parameters**

This method has no parameters.

**Return Type**

[GetLlamasResponse](/src/llamastore/models/README.md#getllamasresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
results = sdk.llama.get_llamas()

pprint(vars(results))

```

### **get_llama_by_id**
Get Llama
- HTTP Method: GET
- Endpoint: /llama/{llama_id}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| llama_id | int | Required | The llama's ID |

**Return Type**

[Llama](/src/llamastore/models/README.md#llama) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
results = sdk.llama.get_llama_by_id(llama_id = 1)

pprint(vars(results))

```

### **delete_llama**
Delete Llama
- HTTP Method: DELETE
- Endpoint: /llama/{llama_id}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| llama_id | int | Required | The llama's ID |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
results = sdk.llama.delete_llama(llama_id = 1)

pprint(vars(results))

```

### **update_llama**
Update Llama
- HTTP Method: PUT
- Endpoint: /llama/{llama_id}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| llama_id | int | Required | The llama's ID |
| request_input | [LlamaCreate](/src/llamastore/models/README.md#llamacreate) | Required | Request body. |

**Return Type**

[Llama](/src/llamastore/models/README.md#llama) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
request_body = {
	'age': 5,
	'color': 'brown',
	'name': 'libby the llama',
	'rating': 4
}
results = sdk.llama.update_llama(
	request_input = request_body,
	llama_id = 1
)

pprint(vars(results))

```


### **create_api_token**
Create Api Token
- HTTP Method: POST
- Endpoint: /token

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ApiTokenRequest](/src/llamastore/models/README.md#apitokenrequest) | Required | Request body. |

**Return Type**

[ApiToken](/src/llamastore/models/README.md#apitoken) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
request_body = {
	'email': 'noone@example.com',
	'password': 'Password123!'
}
results = sdk.token.create_api_token(request_input = request_body)

pprint(vars(results))

```


### **get_user_by_email**
Get User By Email
- HTTP Method: GET
- Endpoint: /user/{email}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| email | str | Required | The user's email address |

**Return Type**

[User](/src/llamastore/models/README.md#user) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
results = sdk.user.get_user_by_email(email = 'sK?q(A7@@%@cs.*./ape3qG%')

pprint(vars(results))

```

### **register_user**
Register User
- HTTP Method: POST
- Endpoint: /user

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [UserRegistration](/src/llamastore/models/README.md#userregistration) | Required | Request body. |

**Return Type**

[User](/src/llamastore/models/README.md#user) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from llamastore import Llamastore
sdk = Llamastore()
sdk.set_access_token(getenv("LLAMASTORE_ACCESS_TOKEN"))
request_body = {
	'email': 'noone@example.com',
	'password': 'Password123!'
}
results = sdk.user.register_user(request_input = request_body)

pprint(vars(results))

```




