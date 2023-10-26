def get_release(self):
    import requests

    res = requests.head("http://su13/outbreak/wastewater/wastewater_agg_demix.json")
    return res.headers["Last-Modified"]
