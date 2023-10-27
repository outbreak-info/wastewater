import json
import os


def load_data(data_folder):
    json_path = os.path.join(data_folder, "wastewater_agg_demix.json")
    with open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['sra_accession']
            yield datum


def custom_data_mapping(cls):
    return {
        "sra_accession": {"type": "keyword"},
        "lineages": {
            "type": "nested",
            "properties": {
                "name": {
                    "type": "keyword",
                    "normalizer": "keyword_lowercase_normalizer"
                },
                "abundance": {
                    "type": "double"
                },
                "crumbs": {
                    "type": "keyword",
                    "normalizer": "keyword_lowercase_normalizer"
                },
            }
        },
        "collection_date": {"type": "keyword"},
        "geo_loc_country": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "geo_loc_region": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "ww_population": {"type": "double"},
        "viral_load": {"type": "keyword"},
        "site_id": {"type": "keyword"},
    }
