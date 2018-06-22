stage3-armv7a_hardfp-latest.tar.bz2:
	export getpath=$$(wget -q -O- http://distfiles.gentoo.org/releases/arm/autobuilds/latest-stage3-armv7a_hardfp.txt | awk 'NR==3{print$$1}') && \
	rsync --no-motd --progress mirror.bytemark.co.uk::gentoo/releases/arm/autobuilds/$${getpath}* . && \
	sed -n '/SHA512/{N;p}' $$(basename $${getpath}.DIGESTS) | sha512sum -c && \
	chattr +i $$(basename $${getpath}) && \
	ln -s $$(basename $$getpath) $@

