import biothings
import config

biothings.config_for_app(config)

import biothings.hub.dataload.uploader
from .parse import (
    load_data_aggregate_demix,
    load_data_aggregate_demix_weekly,
    load_data_aggregate_metadata,
    load_data_aggregate_variants,
)


class WastewaterDemixUploader(biothings.hub.dataload.uploader.BaseSourceUploader):
    name = "wastewater_demix"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return load_data_aggregate_demix(data_folder)


class WastewaterDemixWeeklyUploader(biothings.hub.dataload.uploader.BaseSourceUploader):
    name = "wastewater_demix_weekly"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return load_data_aggregate_demix_weekly(data_folder)


class WastewaterMetadataUploader(biothings.hub.dataload.uploader.BaseSourceUploader):
    name = "wastewater_metadata"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return load_data_aggregate_metadata(data_folder)


class WastewaterVariantsUploader(biothings.hub.dataload.uploader.BaseSourceUploader):
    name = "wastewater_variants"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return load_data_aggregate_variants(data_folder)
