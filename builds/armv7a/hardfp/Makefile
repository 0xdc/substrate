stage3-armv7a_hardfp-latest.tar.bz2:
	export getpath=$$(wget -q -O- https://builds.0xdc.io/armv7a/hardfp/latest-stage3-armv7a_hardfp.txt | awk 'NR==1{print$$1}') && \
	wget https://builds.0xdc.io/armv7a/hardfp/$${getpath} && \
	wget https://builds.0xdc.io/armv7a/hardfp/$${getpath}.CONTENTS && \
	wget https://builds.0xdc.io/armv7a/hardfp/$${getpath}.DIGESTS && \
	sed -n '/SHA512/{N;p}' $$(basename $${getpath}.DIGESTS) | sha512sum -c && \
	ln -s $$(basename $$getpath) $@
