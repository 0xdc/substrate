stage3-amd64-latest.tar.bz2:
	export getpath=$$(wget -q -O- http://distfiles.gentoo.org/releases/amd64/autobuilds/latest-stage3-amd64.txt | awk 'NR==3{print$$1}'); \
	wget -c http://distfiles.gentoo.org/releases/amd64/autobuilds/$$getpath; \
	ln -s $$(basename $$getpath) $@

