import json
data={"name":"Johnny","Job":"Network manager","Years of expertise":12}
y=json.dumps(data, indent=4)
print(json.dumps(data,indent=4))
python_to_J=json.loads(y)
print(python_to_J)