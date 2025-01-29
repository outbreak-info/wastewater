import json
import os


class WastewaterDemixParse():
    def load_data(self, data_folder):
        json_path = os.path.join(data_folder, "aggregate_demix.json")
        with open(json_path) as f:
            for line in f:
                datum = json.loads(line)
                datum['_id'] = datum['sra_accession'] + datum['name']
                yield datum


class WastewaterDemixWeeklyParse():
    def load_data(self, data_folder):
        json_path = os.path.join(data_folder, "aggregate_demix_weekly.json")
        with open(json_path) as f:
            for line in f:
                datum = json.loads(line)
                datum['_id'] = datum['id']
                yield datum


class WastewaterMetadataParse():
    def load_data(self, data_folder):
        json_path = os.path.join(data_folder, "aggregate_metadata.json")
        with open(json_path) as f:
            for line in f:
                datum = json.loads(line)
                datum['_id'] = datum['sra_accession']
                yield datum


class WastewaterVariantsParse():
    def load_data(self, data_folder):
        json_path = os.path.join(data_folder, "aggregate_variants.json")
        with open(json_path) as f:
            for line in f:
                datum = json.loads(line)
                datum['_id'] = datum['sra_accession'] + '_' + str(datum['site']) + '_' + str(datum['alt_base'])
                yield datum
