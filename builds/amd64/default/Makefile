stage3-amd64-latest.tar.bz2:
	export getpath=$$(wget -q -O- http://distfiles.gentoo.org/releases/amd64/autobuilds/latest-stage3-amd64.txt | awk 'NR==3{print$$1}') && \
	rsync --no-motd --progress mirror.bytemark.co.uk::gentoo/releases/amd64/autobuilds/$${getpath}* . && \
	sed -n '/SHA512/{N;p}' $$(basename $${getpath}.DIGESTS) | sha512sum -c && \
	chattr +i $$(basename $${getpath}) && \
	ln -s $$(basename $$getpath) $@

