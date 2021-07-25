import json
import pandas

with open('csvtojson1.json') as f:
    json_dict = json.load(f)
for key in json_dict:
    if json_dict[key] is Null:
        json_dict.pop(key

        moddata.to_json("csvtojson2.json", orient="records", date_format="epoch,", double_precision=10,
                        force_ascii=True, date_unit="ms", default_handler=None)