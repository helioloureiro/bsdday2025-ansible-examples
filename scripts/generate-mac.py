#!/usr/bin/env python3
## src: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/5/html/virtualization/sect-virtualization-tips_and_tricks-generating_a_new_unique_mac_address#sect-Virtualization-Tips_and_tricks-Generating_a_new_unique_MAC_address
# macgen.py script to generate a MAC address for guests on Xen
#
import random
#
def randomMAC():
	mac = [ 0x00, 0x16, 0x3e,
		random.randint(0x00, 0x7f),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff) ]
	return ':'.join(map(lambda x: "%02x" % x, mac))
#
print(randomMAC())
