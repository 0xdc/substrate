stage3-arm64-latest.tar.bz2: stage3-arm64-20190115.tar.bz2
	ln -s $< $@

stage3-arm64-20190115.tar.bz2:
	rsync --no-motd --progress rsync.mirrorservice.org::distfiles.gentoo.org/experimental/arm64/$@* .
	sed -n '/SHA512/{N;s/2008.0/20190115/;p}' $@.DIGESTS | sha512sum -c -
	-chattr +i $@
