
import vstruct
import vstruct.defs.inet as vs_inet

from vstruct.primitives import *

class PCAP_FILE_HEADER(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.magic      = v_uint32()
        self.vers_maj   = v_uint16()
        self.vers_min   = v_uint16()
        self.thiszone   = v_uint32()
        self.sigfigs    = v_uint32()
        self.snaplen    = v_uint32()
        self.linktype   = v_uint32()

class PCAP_PACKET_HEADER(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.tvsec      = v_uint32()
        self.tvusec     = v_uint32()
        self.caplen     = v_uint32()
        self.len        = v_uint32()

def iterPcapFileName(filename, reuse=False):
    fd = file(filename, 'rb')
    for x in iterPcapFile(fd, reuse=reuse):
        yield x
    
def iterPcapFile(fd, reuse=False):

    h = PCAP_FILE_HEADER()
    b = fd.read(len(h))
    h.vsParse(b)

    pkt = PCAP_PACKET_HEADER()
    eII = vs_inet.ETHERII()

    ipv4 = vs_inet.IPv4()
    tcp_hdr = vs_inet.TCP()
    udp_hdr = vs_inet.UDP()

    go = True
    while go:

        hdr = fd.read(len(pkt))
        if hdr == '':
            break

        pkt.vsParse(hdr)

        b = fd.read(pkt.caplen)
        eII.vsParse(b, 0)

        # No support for non-ip protocol yet...
        if eII.etype != vs_inet.ETH_P_IP:
            continue

        offset = len(eII)

        #print eII.tree()
        if not reuse:
            ipv4 = vs_inet.IPv4()
        ipv4.vsParse(b, offset)

        # Make b *only* the IP datagram bytes...
        b = b[offset:offset+ipv4.totlen]
        offset = 0

        offset += len(ipv4)

        if ipv4.proto == vs_inet.IPPROTO_TCP:

            if not reuse:
                tcp_hdr = vs_inet.TCP()
            tcp_hdr.vsParse(b, offset)
            offset += len(tcp_hdr)
            pdata = b[offset:]

            yield pkt,ipv4,tcp_hdr,pdata

        elif ipv4.proto == vs_inet.IPPROTO_UDP:

            if not reuse:
                udp_hdr = vs_inet.UCP()
            udp_hdr.vsParse(b, offset)
            offset += len(udp_hdr)
            pdata = b[offset:]

            yield pkt,ipv4,udp_hdr,pdata

        else:
            print 'UNHANDLED IP PROTOCOL: %d' % ipv4.proto

