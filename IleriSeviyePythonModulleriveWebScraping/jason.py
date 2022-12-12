import json
person_string='{"name":"Alp","surname":"Varna","language": ["C#","Python"]}'
person_dict={"name":"Alp","language":["C#","Python"]
}

# JSON string to Dict
# result = json.loads(person_string)
# # result  =result["name"]
# result = result["language"]

# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["language"])



#Dict to Json string
# result = json.dumps(person_dict)
# print(type(result))

# with open("person.json","w") as f:
#     json.dump(person_dict,f)

person_dict = json.loads(person_string)

result = json.dumps(person_dict,indent=4,sort_keys=True)

print(person_dict)
print(result)