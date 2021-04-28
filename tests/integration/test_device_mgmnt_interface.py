import re
import json
from conftest import Helper


def test_querying_basic_information_in_plain_text_format(lwm2mserver, lwm2mclient):
    """LightweightM2M-1.1-int-201
    Querying the following data on the client (Device Object: ID 3) using Plain
    Text data format
    """

    # TODO: rework so use command line argument instead of CLI command "setformat"

    server = Helper(lwm2mserver)
    assert server.commandresponse("setformat 0 0", "OK")
    assert server.commandresponse("read 0 /3/0/0", "OK")
    text = server.waitforpacket()
    #print(text)
    assert text.find("COAP_205_CONTENT") > 0
    assert text.find("text/plain") > 0
    assert text.find("Open Mobile Alli") > 0
    assert text.find("ance") > 0


def test_querying_basic_information_in_JSON_format(lwm2mserver, lwm2mclient):
    """LightweightM2M-1.1-int-204
    Querying the Resources Values of Device Object ID:3 on the Client using
    JSON data format"""

    # TODO: rework so use command line argument instead of CLI command "setformat"

    server = Helper(lwm2mserver)
    assert server.commandresponse("setformat 0 11543", "OK")
    assert server.commandresponse("read 0 /3/0", "OK")
    text = server.waitforpacket()
    #print(text)
    assert text.find("COAP_205_CONTENT") > 0
    assert text.find("lwm2m+json") > 0

    # TODO: cleanup!
    l = re.findall(r"({.*})", text)
    a = json.loads("["+l[0]+"]")[0]
    assert a['bn'] == "/3/0/"    
    parsed = a['e']
    #print(json.dumps(parsed, indent = 3))
    assert next(item for item in parsed if item["n"] == "0")["sv"] == "Open Mobile Alliance"
    assert next(item for item in parsed if item["n"] == "1")["sv"] == "Lightweight M2M Client"
    assert next(item for item in parsed if item["n"] == "2")["sv"] == "345000123"
    assert next(item for item in parsed if item["n"] == "3")["sv"] == "1.0"
    assert next(item for item in parsed if item["n"] == "11/0")["v"] == 0
    assert next(item for item in parsed if item["n"] == "16")["sv"] == "U"
    