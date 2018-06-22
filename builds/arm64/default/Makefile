stage3-arm64-latest.tar.bz2: stage3-arm64-20180305.tar.bz2
	ln -s $< $@

stage3-arm64-20180305.tar.bz2:
	rsync --no-motd --progress mirror.bytemark.co.uk::gentoo/experimental/arm64/$@* .
	sed -n '/SHA512/{N;s/2008.0/20180305/;p}' $@.DIGESTS | sha512sum -c -
	-chattr +i $@
