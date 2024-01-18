#/usr/bin/expect -f

if {[llength $argv] == 1} {
  set hostname [lindex $argv 0]
} else {
  set hostname "builds.roflmao.space"
}

source builds/tests/failures.tcl

spawn virt-install --autoconsole text --os-variant gentoo --location builds/amd64/minimal/latest-livecd-stage3-amd64-minimal.iso,kernel=boot/gentoo,initrd=boot/gentoo.igz --extra-args "console=ttyS0 cdroot quiet verify" --metadata title=builds/amd64/router --disk size=10

while true {
	expect {
		"roflmaOS login:" { exec virsh pool-refresh default; send "root\r" }
		"router login:" { send "root\r" }
		"Password:" { send "router\r" }
		"root@roflmaOS ~ #" {
			if {$LIVE == 0} { send "sed -i '/Encrypt/d;/CopyFiles/d' /etc/repart.d/bios/20-root.conf\r" }
			if {$LIVE == 1} { send "systemd-repart --no-pager /dev/vda --empty=require --dry-run=no --definitions /etc/repart.d/bios\r" }
			if {$LIVE == 2} { send "systemd-mount /dev/vda2\r" }
			if {$LIVE == 3} { send "systemd-mount /dev/vda1 /run/media/system/root-x86-64/boot\r" }
			if {$LIVE == 4} { send "getpath=\$(curl -s https://$hostname/amd64/router/latest-stage1-amd64-router.txt)\r" }
			if {$LIVE == 5} { send "curl -s https://$hostname/amd64/router/\$getpath | tar xJ -C /run/media/system/root-x86-64\r" }
			if {$LIVE == 6} { send "rsync --recursive /lib/modules/ /run/media/system/root-x86-64/lib/modules\r" }
			if {$LIVE == 7} { send "systemd-firstboot --root /run/media/system/root-x86-64 --setup-machine-id --hostname router\r" }
			if {$LIVE == 8} { send "arch-chroot /run/media/system/root-x86-64\r" }

			if {$LIVE == 20} { send "systemctl reboot\r" }
			if {$LIVE >= 22} { exit }
			set LIVE [expr $LIVE + 1]
		}
		"root@roflmaOS / #" {
			if {$LIVE == 9} { send "grub-install /dev/vda\r" }
			if {$LIVE == 10} { send "echo 'GRUB_CMDLINE_LINUX=\"quiet console=ttyS0,115200n8 mitigations=auto,nosmt\"' >> /etc/default/grub\r" }
			if {$LIVE == 11} { send "echo 'GRUB_TERMINAL=serial' >> /etc/default/grub\r" }
			if {$LIVE == 12} { send "echo 'GRUB_SERIAL_COMMAND=\"serial --speed=115200\"' >> /etc/default/grub\r" }
			if {$LIVE == 13} { send "mv /boot/gentoo /boot/vmlinuz-\$(uname -r)\r" }
			if {$LIVE == 14} { send "mv /boot/gentoo.igz /boot/initramfs-\$(uname -r).img\r" }
			if {$LIVE == 15} { send "grub-mkconfig -o /boot/grub/grub.cfg\r" }
			if {$LIVE == 16} { send "echo root:router | chpasswd\r" }
			if {$LIVE == 17} { send "echo /dev/vda2 / btrfs relatime,compress 1 1 > /etc/fstab\r" }
			if {$LIVE == 18} { send "echo /dev/vda1 /boot ext2 noatime 1 2 >> /etc/fstab\r" }
			if {$LIVE == 19} { send "exit\r" }
			set LIVE [expr $LIVE + 1]
		}
		"root@router ~ #" { exit }
		"device-mapper: remove ioctl" ioctl
		-re $failures handle_failures
	}
}
