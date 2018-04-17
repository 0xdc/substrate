stage3-armv7a_hardfp-latest.tar.bz2:
	export getpath=$$(wget -q -O- http://distfiles.gentoo.org/releases/arm/autobuilds/latest-stage3-armv7a_hardfp.txt | awk 'NR==3{print$$1}'); \
	rsync -P mirror.bytemark.co.uk::gentoo/releases/amd64/autobuilds/$${getpath}* .; \
	ln -s $$(basename $$getpath) $@

