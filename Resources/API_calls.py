# coding=utf-8
import requests
import json

proxies = {
    'http': 'http://127.0.0.1:8080'
}

s = requests.Session()
s.proxies = proxies

# test_data, network = msisdngeneration.generate_msisdn('CA','Virgin Mobile')


def set_charge_behaviour():

    headers = {'Content-Type': 'application/xml'}
    url = "http://smrt.boku.com/testapi/msisdn/"+str(test_data)+"/chrge-behavior"
    data = """<?xml version='1.0' encoding='utf-8'?>
    <charge-behavior error-code="0"/>"""

    req = s.put(url=url, data=data, headers=headers)
    print(test_data)
    print(req.status_code)
    print(req.reason)


def send_mo():
    headers = {'Content-Type': 'application/json'}
    url = "http://smrt.boku.com/smarty/mo";
    data = {
        "type": "MO",
        "source": {"type":"msisdn", "networkCode":network, "countryCode":"CA"},
        "destination": {"type": "shortcode", "number": "43026"},
        "mappedData": {"MSG_BODY": "Y"}
        }
    req = s.post(url=url, data=json.dumps(data), headers=headers)
    print(test_data)
    print(req.status_code)
    print(req.reason)
    print(req.text)


# send_mo()
# set_charge_behaviour()
