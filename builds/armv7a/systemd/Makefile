ARCH=armv7a
SUBA=hardfp

.PHONY: latest
latest:
	test -f stage3-$(ARCH)_$(SUBA)-systemd-latest.tar.* || make stage3-$(ARCH)_$(SUBA)-systemd-latest.tar.xz || make stage3-$(ARCH)_$(SUBA)-systemd-latest.tar.bz2

stage3-$(ARCH)_$(SUBA)-systemd-latest.tar.%:
	getpath=$$(wget -q -O- http://www.mirrorservice.org/sites/distfiles.gentoo.org/releases/arm/autobuilds/latest-stage3-$(ARCH)_$(SUBA)-systemd.txt | gpg -d | awk 'NR==3{print$$1}') && \
	grep -q $* <<<$$getpath && \
	rsync --no-motd --progress rsync.mirrorservice.org::distfiles.gentoo.org/releases/arm/autobuilds/$${getpath}* . && \
	sed -n '/SHA512/{N;p}' $$(basename $${getpath}.DIGESTS) | sha512sum -c && \
	ln -s $$(basename $$getpath) $@
