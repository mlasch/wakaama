import pytest
import pexpect

class Helper:

    def __init__(self, obj):
        self.pexpectobj = obj

    def __dumptext(self):
        print("Debug help: actual output---------------------")
        print(self.pexpectobj.before)
        print("----------------------------------------------")

    def commandresponse(self, cmd,resp):
        self.pexpectobj.sendline(cmd)
        try:
            self.pexpectobj.expect_exact(resp)
        except:
            self.__dumptext()
            return False
        return True

    def waitforpacket(self):
        try:
            self.pexpectobj.expect_exact("bytes received from")
        except:
            self.__dumptext()
            assert False
        #save match line
        try:
            self.pexpectobj.expect_exact("\r\r\n>")
        except:
            __dumptext()
            assert False
        return self.pexpectobj.before

    def waitfortext(self,txt):
        try:
            self.pexpectobj.expect_exact(txt)
        except:
            self.__dumptext()
            return False
        return True


@pytest.fixture
def lwm2mserver():
    """Provide lwm2mserver instance."""
    server = pexpect.spawn("build-wakaama/examples/server/lwm2mserver",
                           encoding="utf8",
                           timeout=3)
    # uncomment to enable logging, helpful when debugging
    # server.logfile = open("lwm2mserver_log.txt", "w")
    server.expect_exact("> ")
    yield server
    server.sendline("q")
    server.expect(pexpect.EOF)


@pytest.fixture
def lwm2mclient():
    """Provide lwm2mclient instance."""
    client = pexpect.spawn("build-wakaama/examples/client/lwm2mclient",
                           encoding="utf8",
                           timeout=3)
    # uncomment to enable logging, helpful when debugging
    client.logfile = open("lwm2mclient_log.txt", "w")
    client.expect("STATE_READY")
    yield client
    client.sendline("quit")
    client.expect(pexpect.EOF)


@pytest.fixture
def lwm2mclient_boot():
    """Provide lwm2mclient instance."""
    client = pexpect.spawn("build-wakaama/examples/client/lwm2mclient -b -n apa",
                           encoding="utf8",
                           timeout=3)
    # uncomment to enable logging, helpful when debugging
    client.logfile = open("lwm2mclient_boot_log.txt", "w")
    #client.expect("STATE_READY")
    yield client
    client.sendline("quit")
    client.expect(pexpect.EOF)


@pytest.fixture
def lwm2mbootstrapserver():
    """Provide lwm2mclient instance."""
    bootstrapserver = pexpect.spawn("build-wakaama/examples/bootstrap_server/bootstrap_server -f examples/bootstrap_server/bootstrap_server.ini",
                           encoding="utf8",
                           timeout=3)
    # uncomment to enable logging, helpful when debugging
    bootstrapserver.logfile = open("lwm2mbootstrapserver_log.txt", "w")
    bootstrapserver.expect(">")
    #LWM2M Bootstrap Server now listening on port
    yield bootstrapserver
    bootstrapserver.sendline("q")
    bootstrapserver.expect(pexpect.EOF)
    