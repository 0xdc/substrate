stage3-arm64-systemd-latest.tar.bz2: stage3-arm64-systemd-20190428.tar.bz2
	ln -s $< $@

stage3-arm64-systemd-20190428.tar.bz2:
	rsync --no-motd --progress mirror.rackspace.com::gentoo/experimental/arm64/$@* .
	sed -n '/SHA512/{N;s/2008.0/20190428/;p}' $@.DIGESTS | sha512sum -c -
