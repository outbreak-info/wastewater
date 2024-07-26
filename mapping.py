class WastewaterDemixMapping():
    def mapping(self):
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


class WastewaterDemixWeeklyMapping():
    def mapping(self):
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
            },
            "epiweek": {
                "type": "integer"
            }
        }


class WastewaterMetadataMapping():
    def mapping(self):
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


class WastewaterVariantsMapping():
    def mapping(self):
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
