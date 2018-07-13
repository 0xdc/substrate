stage3-armv7a_hardfp-latest.tar.bz2: stage3-armv7a_hardfp-20161129-1.tar.bz2
	ln -sf $< $@

stage3-armv7a_hardfp-20161129-1.tar.bz2: stage3-armv7a_hardfp-20161129-1.tar
	bzip2 $<

stage3-armv7a_hardfp-20161129-1.tar: stage3-armv7a_hardfp-20161129.tar.bz2
	test -d tmp || mkdir tmp
	pushd $$(mktemp -d -ptmp) && \
	tar xf $$OLDPWD/$< && \
	rm -fvr tmp/* && \
	tar cf $$OLDPWD/$@ .

stage3-armv7a_hardfp-20161129.tar.bz2:
	rsync --no-motd --progress mirror.bytemark.co.uk::gentoo/releases/arm/autobuilds/current-stage3-armv7a_hardfp/$@ .
