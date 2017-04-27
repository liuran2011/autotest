class VMInfo(object):
    def __init__(self,name,uuid,status,floating_ip):
        self._name=name
        self._uuid=uuid
        self._status=status
        self._floating_ip=floating_ip

    def name(self):
        return self._name

    def uuid(self):
        return self._uuid

    def status(self):
        return self._status

    def floating_ip(self):
        return self._floating_ip
