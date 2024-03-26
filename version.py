def get_release(self):
    import requests

    res_demix = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_demix.json")
    res_metadata = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_metadata.json")
    res_variants = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_variants.json")

    version = " - ".join([
        "demix at " + res_demix.headers["Last-Modified"],
        "metadata at " + res_metadata.headers["Last-Modified"],
        "variants at " + res_variants.headers["Last-Modified"]
    ]).replace(',', '').replace(':', '').replace(' ', '-')

    return version
