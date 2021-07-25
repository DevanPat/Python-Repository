import pandas as pd

csv_file = pd.read_csv("Positions_bluesurfincest_Page_2021_07_08.csv", sep=",", header=0, index_col=False)
csv_file.to_json("csvtojson2.json", orient="records", date_format="epoch,", double_precision=10, force_ascii=True, date_unit="ms", default_handler=None)