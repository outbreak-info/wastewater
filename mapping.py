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
            "epiweek": {
                "type": "integer"
            },
            "week_start": {
                "type": "date",
                "format": "yyyy-MM-dd"
            },
            "week_end": {
                "type": "date",
                "format": "yyyy-MM-dd"
            },
            "geo_loc_region": {
                "type": "keyword"
            },
            "num_samples": {
                "type": "integer"
            },
            "num_sites": {
                "type": "integer"
            },
            "name": {
                "type": "keyword"
            },
            "mean_lineage_prevalence": {
                "type": "double"
            },
            "crumbs": {
                "type": "keyword"
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
            "collected_by": {
                "type": "keyword",
                "normalizer": "keyword_lowercase_normalizer"
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
