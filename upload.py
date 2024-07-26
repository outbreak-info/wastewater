from biothings.hub.dataload.uploader import BaseSourceUploader
from .parse import (
    WastewaterDemixParse,
    WastewaterDemixWeeklyParse,
    WastewaterMetadataParse,
    WastewaterVariantsParse,
)
from .mapping import (
    WastewaterDemixMapping,
    WastewaterDemixWeeklyMapping,
    WastewaterMetadataMapping,
    WastewaterVariantsMapping,
)


class WastewaterDemixUploader(BaseSourceUploader):
    name = "wastewater_demix"
    main_source = "wastewater"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return WastewaterDemixParse().load_data(data_folder)

    @classmethod
    def get_mapping(klass):
        return WastewaterDemixMapping().mapping()


class WastewaterDemixWeeklyUploader(BaseSourceUploader):
    name = "wastewater_demix_weekly"
    main_source = "wastewater"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return WastewaterDemixWeeklyParse().load_data(data_folder)

    @classmethod
    def get_mapping(klass):
        return (
            WastewaterDemixWeeklyMapping().mapping()
        )


class WastewaterMetadataUploader(BaseSourceUploader):
    name = "wastewater_metadata"
    main_source = "wastewater"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return WastewaterMetadataParse().load_data(data_folder)

    @classmethod
    def get_mapping(klass):
        return WastewaterMetadataMapping().mapping()


class WastewaterVariantsUploader(BaseSourceUploader):
    name = "wastewater_variants"
    main_source = "wastewater"

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return WastewaterVariantsParse().load_data(data_folder)

    @classmethod
    def get_mapping(klass):
        return WastewaterVariantsMapping().mapping()
