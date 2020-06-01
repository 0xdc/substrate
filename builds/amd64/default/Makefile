ARCH=amd64

.PHONY: latest
latest:
	test -f stage3-$(ARCH)-latest.tar.* || make stage3-$(ARCH)-latest.tar.xz || make stage3-$(ARCH)-latest.tar.bz2

stage3-$(ARCH)-latest.tar.%:
	getpath=$$(wget -q -O- http://distfiles.gentoo.org/releases/$(ARCH)/autobuilds/latest-stage3-$(ARCH).txt | awk 'NR==3{print$$1}') && \
	grep -q $* <<<$$getpath && \
	rsync --no-motd --progress mirror.bytemark.co.uk::gentoo/releases/$(ARCH)/autobuilds/$${getpath}* . && \
	sed -n '/SHA512/{N;p}' $$(basename $${getpath}.DIGESTS) | sha512sum -c && \
	ln -s $$(basename $$getpath) $@
