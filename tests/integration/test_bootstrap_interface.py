import re
import json
from time import sleep
from conftest import Helper

# ----- bootstrap server ---------------------------------------------------------------------------------------------------------------
# qleisan_wakaama git:(github-ci-integration-test_newer) ✗ build-wakaama/examples/bootstrap_server/bootstrap_server -f examples/bootstrap_server/bootstrap_server.ini
# LWM2M Bootstrap Server now listening on port 5685.

# > 26 bytes received from [::1]:56830
# 44 02 B2 68  68 B2 AF 5C  B2 62 73 46  65 70 3D 61   D..hh..\.bsFep=a
# 70 61 07 70  63 74 3D 31  31 30                      pa.pct=110

# Bootstrap request from "apa"
# Sending DELETE /0 to "apa" OK.
# 8 bytes received from [::1]:56830
# 64 42 D9 D9  D9 D9 AF 5C   dB.....\

#  Received status 2.02 (COAP_202_DELETED) for URI /0 from endpoint apa.
# Sending DELETE /1 to "apa" OK.
# 8 bytes received from [::1]:56830
# 64 42 D9 DA  DA D9 AF 5C   dB.....\

#  Received status 2.02 (COAP_202_DELETED) for URI /1 from endpoint apa.
# Sending WRITE /0/1 to "apa" OK.
# 8 bytes received from [::1]:56830
# 64 44 D9 DB  DB D9 AF 5C   dD.....\

#  Received status 2.04 (COAP_204_CHANGED) for URI /0/1 from endpoint apa.
# Sending WRITE /1/1 to "apa" OK.
# 8 bytes received from [::1]:56830
# 64 44 D9 DC  DC D9 AF 5C   dD.....\

#  Received status 2.04 (COAP_204_CHANGED) for URI /1/1 from endpoint apa.
# Sending BOOTSTRAP FINISH  to "apa" OK.
# 8 bytes received from [::1]:56830
# 64 44 D9 DD  DD D9 AF 5C   dD.....\

#  Received status 2.04 (COAP_204_CHANGED) for URI / from endpoint apa.

# ----- server -------------------------------------------------------------------------------------------------------------------------
# qleisan_wakaama git:(github-ci-integration-test_newer) ✗ build-wakaama/examples/server/lwm2mserver> 172 bytes received from [::1]:56830
# 44 02 B2 69  69 B2 AF 5C  B2 72 64 11  28 39 6C 77   D..ii..\.rd.(9lw
# 6D 32 6D 3D  31 2E 31 06  65 70 3D 61  70 61 03 62   m2m=1.1.ep=apa.b
# 3D 55 06 6C  74 3D 33 30  30 C1 0B FF  3C 2F 3E 3B   =U.lt=300...</>;
# 72 74 3D 22  6F 6D 61 2E  6C 77 6D 32  6D 22 3B 63   rt="oma.lwm2m";c
# 74 3D 31 31  30 2C 3C 2F  31 3E 3B 76  65 72 3D 31   t=110,</1>;ver=1
# 2E 31 2C 3C  2F 31 2F 31  3E 2C 3C 2F  32 2F 30 3E   .1,</1/1>,</2/0>
# 2C 3C 2F 33  2F 30 3E 2C  3C 2F 34 2F  30 3E 2C 3C   ,</3/0>,</4/0>,<
# 2F 35 2F 30  3E 2C 3C 2F  36 2F 30 3E  2C 3C 2F 37   /5/0>,</6/0>,</7
# 2F 30 3E 2C  3C 2F 33 31  30 32 34 3E  3B 76 65 72   /0>,</31024>;ver
# 3D 31 2E 30  2C 3C 2F 33  31 30 32 34  2F 31 30 3E   =1.0,</31024/10>
# 2C 3C 2F 33  31 30 32 34  2F 31 31 3E                ,</31024/11>
# 56 bytes received from [::1]:56830
# 44 02 B2 6A  69 B2 AF 5C  B2 72 64 11  28 39 6C 77   D..ji..\.rd.(9lw
# 6D 32 6D 3D  31 2E 31 06  65 70 3D 61  70 61 03 62   m2m=1.1.ep=apa.b
# 3D 55 06 6C  74 3D 33 30  30 C1 13 FF  2C 3C 2F 33   =U.lt=300...,</3
# 31 30 32 34  2F 31 32 3E                             1024/12>

# New client #0 registered.
# Client #0:
#         name: "apa"
#         version: "1.1"
#         binding: "UDP"
#         lifetime: 300 sec
#         objects: /1 (1.1), /1/1, /2/0, /3/0, /4/0, /5/0, /6/0, /7/0, /31024 (1.0), /31024/10, /31024/11, /31024/12, 

# > 

# ----- client -------------------------------------------------------------------------------------------------------------------------
# qleisan_wakaama git:(github-ci-integration-test_newer) ✗ build-wakaama/examples/client/lwm2mclient -b -n apa
# Trying to bind LWM2M Client to port 56830
# LWM2M Client "apa" started on port 56830
# > Opening connection to server at ::1:5685
#  -> State: STATE_BOOTSTRAPPING
#  -> State: STATE_BOOTSTRAPPING
# 8 bytes received from [::1]:5685
# 64 44 B2 68  68 B2 AF 5C   dD.hh..\
#  -> State: STATE_BOOTSTRAPPING
# 10 bytes received from [::1]:5685
# 44 04 D9 D9  D9 D9 AF 5C  B1 30  D......\.0
#  -> State: STATE_BOOTSTRAPPING
# 10 bytes received from [::1]:5685
# 44 04 D9 DA  DA D9 AF 5C  B1 31  D......\.1
#  -> State: STATE_BOOTSTRAPPING
# 122 bytes received from [::1]:5685
# 44 03 D9 DB  DB D9 AF 5C  B1 30 01 31  11 6E FF 5B   D......\.0.1.n.[
# 7B 22 62 6E  22 3A 22 2F  30 2F 31 2F  22 2C 22 6E   {"bn":"/0/1/","n
# 22 3A 22 30  22 2C 22 76  73 22 3A 22  63 6F 61 70   ":"0","vs":"coap
# 3A 2F 2F 6C  6F 63 61 6C  68 6F 73 74  3A 35 36 38   ://localhost:568
# 33 22 7D 2C  7B 22 6E 22  3A 22 31 22  2C 22 76 62   3"},{"n":"1","vb
# 22 3A 66 61  6C 73 65 7D  2C 7B 22 6E  22 3A 22 31   ":false},{"n":"1
# 30 22 2C 22  76 22 3A 31  7D 2C 7B 22  6E 22 3A 22   0","v":1},{"n":"
# 32 22 2C 22  76 22 3A 33  7D 5D                      2","v":3}]
#  -> State: STATE_BOOTSTRAPPING
# 103 bytes received from [::1]:5685
# 44 03 D9 DC  DC D9 AF 5C  B1 31 01 31  11 6E FF 5B   D......\.1.1.n.[
# 7B 22 62 6E  22 3A 22 2F  31 2F 31 2F  22 2C 22 6E   {"bn":"/1/1/","n
# 22 3A 22 30  22 2C 22 76  22 3A 31 7D  2C 7B 22 6E   ":"0","v":1},{"n
# 22 3A 22 31  22 2C 22 76  22 3A 33 30  30 7D 2C 7B   ":"1","v":300},{
# 22 6E 22 3A  22 36 22 2C  22 76 62 22  3A 66 61 6C   "n":"6","vb":fal
# 73 65 7D 2C  7B 22 6E 22  3A 22 37 22  2C 22 76 73   se},{"n":"7","vs
# 22 3A 22 55  22 7D 5D                                ":"U"}]
#  -> State: STATE_BOOTSTRAPPING
# 11 bytes received from [::1]:5685
# 44 02 D9 DD  DD D9 AF 5C  B2 62 73  D......\.bs
#  -> State: STATE_BOOTSTRAPPING
# Opening connection to server at localhost:5683
#  -> State: STATE_REGISTERING
# 11 bytes received from [::1]:5683
# 64 5F B2 69  69 B2 AF 5C  D1 0E 0B  d_.ii..\...
#  -> State: STATE_REGISTERING
# 16 bytes received from [::1]:5683
# 64 41 B2 6A  69 B2 AF 5C  82 72 64 01  30 D1 06 13   dA.ji..\.rd.0...
#  -> State: STATE_READY
#  -> State: STATE_READY
#  -> State: STATE_READY


def test_client_initiated_bootstrap(lwm2mbootstrapserver, lwm2mclient_boot):
    """LightweightM2M-1.1-int-0
    Test the Client capability to connect the Bootstrap Server according to the
    Client Initiated Bootstrap Mode"""

    # Possible improvements:
    # - remove (if possible) 10s sleep
    # - update client to print "2.04 changed" to improve §A test
    # - investigate if sending DELETE /0, /1 is correct
    # - use and check "0-SetOfValue"
    # - check received WRITE operations instead of sent WRITE operations
    # - investigate if PUT /0/1 is correct or if it should be PUT /0 (same for PUT /1/1)
    # - since CLI output needs to be checked in sequence §B and §C checks happen §B1,§C1,§B2,§C2 (same CLI).
    # - check payload for discover response
    # - make testcase robust to handle if blocktransfer is used (better to disable/use new default 1024 value)
    # - check for inconsistencies in §E

    client = Helper(lwm2mclient_boot)
    bootstrapserver = Helper(lwm2mbootstrapserver)

    # check that client attempts to bootstrap
    assert client.waitfortext("STATE_BOOTSTRAPPING")

    # TODO: this is a waste of time, can be improved?
    sleep(10)

    # §A
    # bootstrap request is triggered by command line option
    assert bootstrapserver.waitfortext('Bootstrap request from "apa"\r\r\n')
    # should check for "2.04" changed but informarmation not available at CLI. Just check that we got packet (of correct size)
    assert client.waitfortext("8 bytes received from")
    
    # check that DELETE /0 is sent and ack:ed (not in TC spec, see TODO)
    assert bootstrapserver.waitfortext('Sending DELETE /0 to "apa" OK.')
    assert bootstrapserver.waitfortext('Received status 2.02 (COAP_202_DELETED) for URI /0 from endpoint apa.')

    # check that DELETE /1 is sent and ack:ed (not in TC spec, see TODO)
    assert bootstrapserver.waitfortext('Sending DELETE /1 to "apa" OK.')
    assert bootstrapserver.waitfortext('Received status 2.02 (COAP_202_DELETED) for URI /1 from endpoint apa.')

    # §B check that bootstrap write operations are sent (not checking data)
    assert bootstrapserver.waitfortext('Sending WRITE /0/1 to "apa" OK.')
    # §C check that bootstrap server received success ACK
    assert bootstrapserver.waitfortext('Received status 2.04 (COAP_204_CHANGED) for URI /0/1 from endpoint apa.')

    # §B check that bootstrap write operations are sent (not checking data)
    assert bootstrapserver.waitfortext('Sending WRITE /1/1 to "apa" OK.')
    # §C check that bootstrap server received success ACK
    assert bootstrapserver.waitfortext('Received status 2.04 (COAP_204_CHANGED) for URI /1/1 from endpoint apa.')

    # §D check bootstrap discover ACK
    assert bootstrapserver.waitfortext('Received status 2.05 (COAP_205_CONTENT) for URI / from endpoint apa.')

    # §E check that bootstrap server receives a successful ACK for bootstrap finish
    assert bootstrapserver.waitfortext('Sending BOOTSTRAP FINISH  to "apa" OK.')
    assert bootstrapserver.waitfortext('Received status 2.04 (COAP_204_CHANGED) for URI / from endpoint apa.')
