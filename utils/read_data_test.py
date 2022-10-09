import yaml


f = open("../data/data.yaml", encoding="utf8")
data = yaml.safe_load(f)
print(data)
print(data['hero'])
print(data['heros_name'])
print(data['heros'])
print(data['mobile_belong_post'])
print(data['mobile_belong_get'])
