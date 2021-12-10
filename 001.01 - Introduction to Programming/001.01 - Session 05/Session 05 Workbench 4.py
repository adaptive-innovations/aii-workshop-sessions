import json

# Create the dictionary
theFamily = {}
theFamily['dad'] = {"name":{"first":"Bob","middle":"Joseph","last":"Dole"},"age":98}
theFamily['mom'] = {"name":{"first":"Jane","middle":"Sally","last":"Dole"},"age":96}
theFamily['kids'] = []
theFamily['kids'].append({"name":{"first":"Bill","middle":"Robert","last":"Dole"},"age":46})
theFamily['kids'].append({"name":{"first":"Bobby","middle":"Shaq","last":"Dole"},"age":44})
theFamily['kids'].append({"name":{"first":"Jill","middle":"Sally-Mae","last":"Clinton"},"age":41})
theFamily['kids'].append({"name":{"first":"Charlie","middle":"Day","last":"Dole"},"age":35})

# Cast the dictionary as JSON
theFamilyJson = json.dumps(theFamily)
print(theFamilyJson)