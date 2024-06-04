import json
import os


def load_data_aggregate_demix(data_folder):
    json_path = os.path.join(data_folder, "aggregate_demix.json")
    with open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['sra_accession'] + datum['name']
            yield datum


def load_data_aggregate_demix_weekly(data_folder):
    json_path = os.path.join(data_folder, "aggregate_demix_weekly.json")
    with open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['id']
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
        "sra_accession": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "name": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "prevalence": {
            "type": "double"
        },
        "crumbs": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "coverage": {
            "type": "double"
        },
        "spike_coverage": {
            "type": "double"
        }
    }


def custom_data_mapping_aggregate_demix_weekly(cls):
    return {
        "date_start": {
            "type": "date",
            "format": "yyyy-MM-dd"
        },
        "date_end": {
            "type": "date",
            "format": "yyyy-MM-dd"
        },
        "total_population": {
            "type": "integer"
        },
        "num_collection_sites": {
            "type": "integer"
        },
        "num_samples": {
            "type": "integer"
        },
        "geo_loc_region": {
            "type": "keyword"
        },
        "name": {
            "type": "keyword"
        },
        "mean_lineage_prevalence": {
            "type": "double"
        }
    }


def custom_data_mapping_aggregate_metadata(cls):
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
        },
        "demix_success": {
            "type": "boolean"
        },
        "variants_success": {
            "type": "boolean"
        },
        "coverage_intervals": {
            "type": "nested",
            "properties": {
                "start": {
                    "type": "integer"
                },
                "end": {
                    "type": "integer"
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
        "site": {
            "type": "integer"
        },
        "ref_base": {
            "type": "keyword"
        },
        "alt_base": {
            "type": "keyword"
        },
        "depth": {
            "type": "double"
        },
        "prevalence": {
            "type": "double"
        }
    }
