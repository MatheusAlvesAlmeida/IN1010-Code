# ext/questao3.py

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *

log = core.getLogger()  # logging


class questao3(EventMixin):
    switches = {}

    def __init__(self):
        self.listenTo(core.openflow)

    def _handle_ConnectionUp(self, event):
        log.debug("Connection UP from %s", event.dpid)
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match()  # Match all packets
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)
        log.debug("Installed default flood flow rule on switch %s", event.dpid)

    def _handle_PacketIn(self, event):
        pass


def launch():
    core.openflow.miss_send_len = 1024
    core.registerNew(questao3)
