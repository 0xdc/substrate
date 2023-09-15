profile: default/linux/amd64/17.1/desktop/plasma/systemd/merged-usr
source_subpath: amd64/plasma/stage4-amd64-plasma-latest
portage_confdir: @REPO_DIR@/confdirs/amd64/plasma/duet

livecd/use:
	ibus
	vaapi

livecd/packages:
	app-admin/pass-otp
	app-admin/sysstat
	app-crypt/efitools
	app-crypt/sbsigntools
	app-crypt/tpm2-openssl
	app-crypt/yubikey-manager
	app-office/sc-im
	dev-libs/intel-compute-runtime
	dev-python/dbus-python
	dev-python/pefile
	dev-python/pyroute2
	dev-texlive/texlive-latexextra
	dev-util/intel-graphics-compiler
	gui-libs/libhandy
	kde-apps/ffmpegthumbs
	mail-client/thunderbird
	media-gfx/zbar
	media-libs/libva-intel-media-driver
	media-tv/v4l-utils
	media-video/mpv
	net-analyzer/nmap
	net-analyzer/traceroute
	net-analyzer/vnstat
	net-dialup/xl2tpd
	net-im/gajim
	net-im/signal-desktop-bin
	net-irc/quassel
	net-misc/aria2
	net-misc/mosh
	net-misc/wol
	net-misc/yt-dlp
	net-voip/mumble
	sys-apps/ipmitool
	sys-apps/kexec-tools
	sys-apps/usbutils
	sys-auth/pam_u2f
	sys-boot/efibootmgr
	sys-firmware/intel-microcode
	sys-fs/btrfs-progs
	sys-fs/dosfstools
	sys-fs/fuse-exfat
	sys-kernel/linux-firmware
	sys-power/powertop
	sys-power/thermald
	x11-drivers/xf86-video-intel
	x11-misc/zim

livecd/depclean: yes
