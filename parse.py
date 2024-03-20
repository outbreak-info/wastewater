import json
import os


def load_data_aggregate_demix(data_folder):
    json_path = os.path.join(data_folder, "aggregate_demix.json")
    with open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['sra_accession']
            yield datum


def load_data_aggregate_metadata(data_folder):
    json_path = os.path.join(data_folder, "aggregate_metadata.json")
    with open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['sra_accession']
            yield datum


def load_data_aggregate_variants(data_folder):
    json_path = os.path.join(data_folder, "aggregate_variants.json")
    with open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['sra_accession'] + '_' + str(datum['site'])
            yield datum


def custom_data_mapping_aggregate_demix(cls):
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
        "viral_load": {"type": "double"},
        "site_id": {"type": "keyword"},
    }


def custom_data_mapping_aggregate_metadata(cls):
    return {
        "site": {
            "type": "integer"
        },
        "sra_accession": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },

        "ref_base": {
            "type": "keyword"
        },
        "variants": {
            "type": "nested",
            "properties": {
                "alt_base": {
                    "type": "keyword"
                },
                "depth": {
                    "type": "double"
                },
                "frequency": {
                    "type": "double"
                }
            }
        }
    }


def custom_data_mapping_aggregate_variants(cls):
    return {
        "sra_accession": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "collection_date": {
            "type": "date",
            "format": "yyyy-MM-dd"
        },
        "geo_loc_country": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "geo_loc_region": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "ww_population": {
            "type": "double"
        },
        "viral_load": {
            "type": "double"
        },
        "collection_site_id": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        }
    }
