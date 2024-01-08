def get_release(self):
    import requests

    res = requests.head("https://storage.googleapis.com/outbreak-ww-data/aggregate/aggregate_demix.json")
    return res.headers["Last-Modified"]
