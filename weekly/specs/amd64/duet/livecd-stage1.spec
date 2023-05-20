profile: default/linux/amd64/17.1/desktop/plasma/systemd/merged-usr
source_subpath: amd64/plasma/stage4-amd64-plasma-latest
portage_confdir: @REPO_DIR@/confdirs/amd64/plasma/duet

livecd/use:
	ibus
	pulseaudio
	vaapi

livecd/packages:
	app-admin/pass-otp
	app-crypt/efitools
	app-crypt/sbsigntools
	app-crypt/tpm2-totp
	app-crypt/tpm2-tss-engine
	dev-libs/intel-compute-runtime
	kde-apps/ffmpegthumbs
	mail-client/thunderbird
	media-gfx/zbar
	media-libs/libva-intel-media-driver
	media-libs/vulkan-loader
	media-video/mpv
	net-dialup/xl2tpd
	net-im/dino
	net-im/signal-desktop-bin
	net-irc/quassel
	net-misc/yt-dlp
	net-voip/mumble
	sys-apps/kexec-tools
	sys-apps/usbutils
	sys-boot/efibootmgr
	sys-firmware/intel-microcode
	sys-fs/btrfs-progs
	sys-fs/dosfstools
	sys-kernel/linux-firmware
	x11-misc/zim

livecd/depclean: yes
