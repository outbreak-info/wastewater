import biothings
import config

biothings.config_for_app(config)

import biothings.hub.dataload.uploader
from .parse import (
    load_data_aggregate_demix,
    load_data_aggregate_demix_weekly,
    load_data_aggregate_metadata,
    load_data_aggregate_variants,
    custom_data_mapping_aggregate_demix,
    custom_data_mapping_aggregate_demix_weekly,
    custom_data_mapping_aggregate_metadata,
    custom_data_mapping_aggregate_variants,
)


class WastewaterDemixUploader(biothings.hub.dataload.uploader.BaseSourceUploader):
    name = "wastewater_demix"
    main_source = "wastewater"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return load_data_aggregate_demix(data_folder)

    @classmethod
    def get_mapping(klass):
        return custom_data_mapping_aggregate_demix()


class WastewaterDemixWeeklyUploader(biothings.hub.dataload.uploader.BaseSourceUploader):
    name = "wastewater_demix_weekly"
    main_source = "wastewater"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return load_data_aggregate_demix_weekly(data_folder)

    @classmethod
    def get_mapping(klass):
        return custom_data_mapping_aggregate_demix_weekly()


class WastewaterMetadataUploader(biothings.hub.dataload.uploader.BaseSourceUploader):
    name = "wastewater_metadata"
    main_source = "wastewater"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return load_data_aggregate_metadata(data_folder)

    @classmethod
    def get_mapping(klass):
        return custom_data_mapping_aggregate_metadata()


class WastewaterVariantsUploader(biothings.hub.dataload.uploader.BaseSourceUploader):
    name = "wastewater_variants"
    main_source = "wastewater"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return load_data_aggregate_variants(data_folder)

    @classmethod
    def get_mapping(klass):
        return custom_data_mapping_aggregate_variants()
