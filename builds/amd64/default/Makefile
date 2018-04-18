stage3-amd64-latest.tar.bz2:
	export getpath=$$(wget -q -O- http://distfiles.gentoo.org/releases/amd64/autobuilds/latest-stage3-amd64.txt | awk 'NR==3{print$$1}') && \
	rsync -P mirror.bytemark.co.uk::gentoo/releases/amd64/autobuilds/$${getpath}* . && \
	grep -A1 SHA512 $$(basename $${getpath}.DIGESTS) | sha512sum -c && \
	ln -s $$(basename $$getpath) $@

