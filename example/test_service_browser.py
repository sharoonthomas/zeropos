from zeroconf import raw_input, ServiceBrowser, Zeroconf


class MyListener(object):

    def removeService(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def addService(self, zeroconf, type, name):
        info = zeroconf.getServiceInfo(type, name)
        print("Service %s added, service info: %s" % (name, info))


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_trytonpos._tcp.local.", listener)
try:
    raw_input("Press enter to exit...\n\n")
finally:
    zeroconf.close()
