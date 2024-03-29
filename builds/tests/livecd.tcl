#/usr/bin/expect -f

set EXTRA [lassign $argv CD]
# builds/amd64/minimal/latest-livecd-stage3-amd64-minimal.iso --extra-args real_init=/usr/lib/systemd/systemd
# builds/amd64/systemd/latest-livecd-stage3-amd64.iso
# builds/amd64/plasma/latest-livecd-stage3-amd64-plasma.iso --memory 1024 --disk size=10

source builds/tests/failures.tcl

spawn virt-install --autoconsole text --os-variant gentoo --boot uefi --location $CD,kernel=boot/gentoo,initrd=boot/gentoo.igz --extra-args "console=ttyS0 cdroot quiet verify" --metadata title=$CD {*}$EXTRA

while true {
	expect {
		"Connected to domain" { exec virsh pool-refresh default }
		"roflmaOS login:" { send "root\r" }
		"root@roflmaOS ~ #" {
			if {$LIVE == 0} { send "systemd-repart --no-pager /dev/vda --empty=require --dry-run=no\r" }
			if {$LIVE == 1} { send "/lib/systemd/systemd-cryptsetup attach cryptoroot /dev/vda2\r" }
			if {$LIVE == 2} { send "systemd-mount /dev/mapper/cryptoroot\r" }
			if {$LIVE == 3} { send "systemd-mount -o uid=0,gid=0,fmask=0077,dmask=0077 /dev/vda1 /run/media/system/root-x86-64/efi\r" }
			if {$LIVE == 4} { send "systemd-machine-id-setup --root /run/media/system/root-x86-64\r" }
			if {$LIVE == 5} { send "systemd-nspawn --bind /sys/firmware/efi -D/run/media/system/root-x86-64\r" }
			if {$LIVE == 9} { send "systemctl reboot\r" }
			set LIVE [expr $LIVE + 1]
		}
		"root@root-x86-64 ~ #" {
			if {$LIVE == 6} { send "bootctl install\r" }
			if {$LIVE == 7} { send "if grep -q ID= /etc/os-release && which objcopy; then dracut --kernel-cmdline='quiet console=ttyS0' --uefi --kernel-image=/boot/gentoo; else echo quiet console=ttyS0 > /etc/kernel/cmdline; kernel-install add \$(uname -r) /boot/gentoo; fi\r" }
			if {$LIVE == 8} { send "exit\r" }
			set LIVE [expr $LIVE + 1]
		}
		"device-mapper: remove ioctl" ioctl
		"Please enter passphrase for disk" { send "\r" }
		"Last login:" { if {$LIVE >= 10} { exit } }
		$fat_clusters_msg fat_clusters
		-re $failures handle_failures
	}
}
