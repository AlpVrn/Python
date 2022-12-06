import json

person_string='{"name":"Alp","surname":"Varna","language": ["C#","Python"]}'
# JSON string to Dict
result = json.loads(person_string)
# result  =resulct["name"]
result = result["language"]
print(type(result))
print(result)