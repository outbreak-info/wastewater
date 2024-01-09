def get_release(self):
    import requests

    res_demix = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_demix.json")
    res_variants_by_acc = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_variants_by_acc.json")
    res_variants_by_mut = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_variants_by_mut.json")

    version = " - ".join([
        "demix at " + res_demix.headers["Last-Modified"],
        "acc at " + res_variants_by_acc.headers["Last-Modified"],
        "mut at " + res_variants_by_mut.headers["Last-Modified"]
    ])

    return version
