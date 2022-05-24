from bs4 import BeautifulSoup
import requests
def reqURL(url_):
    msg_ = url_[0:-10]
    print(f"\nSending req...to.{msg_}\n------")
    req = requests.get(url_)
    print("req granted\nparsing html file...\n------")
    soup = BeautifulSoup(req.text, 'html.parser')
    print("✅ 200 OK\n------")
    return soup