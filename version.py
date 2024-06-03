def get_release(self):
    import requests

    res_demix = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_demix.json")
    res_demix_weekly = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_demix_weekly.json")
    res_metadata = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_metadata.json")
    res_variants = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_variants.json")

    version = "_".join([
        "demix=" + res_demix.headers["Last-Modified"],
        "demix-weekly=" + res_demix_weekly.headers["Last-Modified"],
        "metadata=" + res_metadata.headers["Last-Modified"],
        "variants=" + res_variants.headers["Last-Modified"]
    ]).replace(',', '').replace(':', '').replace(' ', '-')

    return version
