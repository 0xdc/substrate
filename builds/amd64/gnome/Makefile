ARCH=amd64
BUILD=gnome
UPSTREAM=systemd-mergedusr

.PHONY: latest
latest:
	test -f stage3-$(ARCH)-$(BUILD)-latest.tar.* || make stage3-$(ARCH)-$(BUILD)-latest.tar.xz || make stage3-$(ARCH)-$(BUILD)-latest.tar.bz2

stage3-$(ARCH)-$(BUILD)-latest.tar.%:
	getpath=$$(wget -q -O- http://www.mirrorservice.org/sites/distfiles.gentoo.org/releases/$(ARCH)/autobuilds/latest-stage3-$(ARCH)-$(UPSTREAM).txt | gpg -d | awk 'NR==3{print$$1}') && \
	grep -q $* <<<$$getpath && \
	rsync --no-motd --progress rsync.mirrorservice.org::distfiles.gentoo.org/releases/$(ARCH)/autobuilds/$${getpath}* . && \
	sed -n '/SHA512/{N;p}' $$(basename $${getpath}.DIGESTS) | sha512sum -c && \
	ln -s $$(basename $$getpath) $@
