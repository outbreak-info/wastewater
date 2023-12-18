def get_release(self):
    import requests

    res = requests.head("https://media.githubusercontent.com/media/dylanpilz/Freyja-SRA/main/outputs/aggregate/aggregate_demix.json")
    return res.headers["Last-Modified"]
