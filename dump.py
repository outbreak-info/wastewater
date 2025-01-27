import os
from google.cloud import storage
from google.oauth2 import service_account

from biothings.hub.dataload.dumper import HTTPDumper
from config import DATA_ARCHIVE_ROOT
from .credentials import GOOGLE_APPLICATION_CREDENTIALS
from .version import WastewaterVersion


class WastewaterDumper(HTTPDumper):

    SRC_NAME = "wastewater"
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)
    SCHEDULE = "0 1 * * *"
    UNCOMPRESS = False
    FILES_TO_DUMP = [
        "aggregate_demix.json",
        "aggregate_demix_weekly.json",
        "aggregate_metadata.json",
        "aggregate_variants.json",
    ]

    def get_current_version(self):
        self.release = WastewaterVersion().get_release()
        current_release = self.src_doc.get("download", {}).get("release")
        if not current_release or self.release > current_release:
            self.logger.info("New release '%s' found", self.release)
            return True
        self.logger.debug("No new release found")
        return False

    def create_todump_list(self, force=False, **kwargs):
        newrelease = self.get_current_version()
        for file_name in self.__class__.FILES_TO_DUMP:
            local_path = os.path.join(
                self.new_data_folder,
                os.path.basename(file_name)
            )
            remote_path = os.path.join("aggregate/", file_name)
            if force or not os.path.exists(local_path) or newrelease:
                self.to_dump.append({
                    "remote": remote_path,
                    "local": local_path
                })

    def gc_download(self, blob_name, destination_file_name):
        bucket_name = "outbreak-ww-data"
        credentials = service_account.Credentials.from_service_account_info(
            GOOGLE_APPLICATION_CREDENTIALS
        )
        storage_client = storage.Client(credentials=credentials)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.download_to_filename(destination_file_name)

    def download(self, remotefile, localfile):
        self.prepare_local_folders(localfile)
        self.logger.debug("Downloading '%s'", os.path.basename(localfile))
        self.gc_download(remotefile, localfile)
