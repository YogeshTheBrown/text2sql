# currently building for json file with structure

import json


def load_data():
    with open("../data/raw/db_sample_metadata.json") as f:
        data = json.load(f)
    rows = data[list(data.keys())[0]]

    docs = []
    for row in rows:
        doc = (
        f"Table {row["table_name"]} has column {row['column_name']} "
        f"of type {row["data_type"]}, "
        f"{'not null' if row ['not_null'] else 'nullable'}")


        if row["primary_key"]: # checking if primary key is 1 then add else don't
            doc += ", primary key."

        docs.append(doc)

    return docs



