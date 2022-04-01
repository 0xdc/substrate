profile: default/linux/amd64/17.1/no-multilib/systemd
source_subpath: amd64/systemd/stage3-amd64-systemd-latest

# gnupg[-ssl] avoids pulling in gnutls
# git[-perl] avoids having perl and gcc
# git[-pcre-jit] avoids libpcre2
#   nmap pulls in libpcre so we use that instead
# iproute2[-iptables] since we use nftables now

embedded/packages:
	app-crypt/gnupg[-ssl,usb]
	dev-vcs/git[-perl,-pcre-jit]
	net-analyzer/nmap
	net-analyzer/tcpdump
	net-analyzer/traceroute
	net-dialup/ppp
	net-dialup/rp-pppoe
	net-dns/dnsmasq[dnssec]
	net-firewall/nftables
	sys-apps/iproute2[-iptables]
	sys-apps/util-linux
	www-servers/nginx
