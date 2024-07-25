

def get_release(self):
    from google.cloud import storage
    from google.oauth2 import service_account
    from .credentials import GOOGLE_APPLICATION_CREDENTIALS

    # key_path = '.credentials'
    bucket_name = 'outbreak-ww-data'
    # credentials = service_account.Credentials.from_service_account_file(key_path)
    credentials = service_account.Credentials.from_service_account_info(GOOGLE_APPLICATION_CREDENTIALS)

    def blob_metadata(bucket_name, blob_name):
        """Prints out a blob's metadata."""
        storage_client = storage.Client(credentials=credentials)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.get_blob(blob_name)

        return blob.updated

    res_demix = blob_metadata(bucket_name, "aggregate/aggregate_demix.json")
    res_demix_weekly = blob_metadata(bucket_name, "aggregate/aggregate_demix_weekly.json")
    res_metadata = blob_metadata(bucket_name, "aggregate/aggregate_metadata.json")
    res_variants = blob_metadata(bucket_name, "aggregate/aggregate_variants.json")

    version = "_".join([
        "demix=" + str(res_demix),
        "demix-weekly=" + str(res_demix_weekly),
        "metadata=" + str(res_metadata),
        "variants=" + str(res_variants)
    ]).replace(',', '').replace(':', '').replace(' ', '-')

    return version
