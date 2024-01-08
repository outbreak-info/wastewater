import json
import os


def load_data_aggregate_demix(data_folder):
    json_path = os.path.join(data_folder, "aggregate_demix.json")
    with open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['sra_accession']
            yield datum


def load_data_aggregate_variants_by_acc(data_folder):
    json_path = os.path.join(data_folder, "aggregate_variants_by_acc.json")
    with open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['sra_accession']
            yield datum


def load_data_aggregate_variants_by_mut(data_folder):
    json_path = os.path.join(data_folder, "aggregate_variants_by_mut.json")
    with open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['mut_hash']
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


def custom_data_mapping_aggregate_variants_by_acc(cls):
    return {
        "sra_accession": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "mutations": {
            "type": "nested",
            "properties": {
                "mut_name": {
                    "type": "keyword",
                    "normalizer": "keyword_lowercase_normalizer"
                },
                "frequency": {
                    "type": "double"
                },
                "depth": {
                    "type": "double"
                }
            }
        },
        "collection_date": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
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
        "site_id": {
            "type": "keyword"
        }
    }


def custom_data_mapping_aggregate_variants_by_mut(cls):
    return {
        "mut_hash": {
            "type": "keyword"
        },
        "mut_name": {
            "type": "keyword"
        },
        "samples": {
            "type": "nested",
            "properties": {
                "sra_accession": {
                    "type": "keyword"
                },
                "frequency": {
                    "type": "double"
                },
                "depth": {
                    "type": "double"
                },
                "collection_date": {
                    "type": "keyword"
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
                "site_id": {
                    "type": "keyword"
                }
            }
        }
    }
