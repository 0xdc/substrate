#/usr/bin/expect -f

set LIVE 0

set EXTRA [lassign $argv CD]
# builds/amd64/duet/latest-livecd-stage3-amd64-duet.iso --memory 1024 --disk size=10

spawn virt-install --autoconsole text --os-variant gentoo --boot uefi --location $CD,kernel=boot/gentoo,initrd=boot/gentoo.igz --extra-args "console=ttyS0 root=live:LABEL=ISOIMAGE quiet rd.live.dir=/ rd.live.squashimg=image.squashfs" --metadata title=$CD {*}$EXTRA

while true {
	expect {
		"duet login:" { send "root\r" }
		"root@duet ~ #" {
			if {$LIVE == 0} { send "systemd-repart --no-pager /dev/vda --empty=require --dry-run=no\r" }
			if {$LIVE == 1} { send "/lib/systemd/systemd-cryptsetup attach cryptoroot /dev/vda3\r" }
			if {$LIVE == 2} { send "systemd-mount /dev/mapper/cryptoroot\r" }
			if {$LIVE == 3} { send "systemd-mount /dev/vda1 /run/media/system/root-x86-64/efi\r" }
			if {$LIVE == 4} { send "systemd-machine-id-setup --root /run/media/system/root-x86-64\r" }
			if {$LIVE == 5} { send "systemd-nspawn --bind /sys/firmware/efi -D/run/media/system/root-x86-64\r" }
			if {$LIVE == 10} { send "systemctl reboot\r" }
			set LIVE [expr $LIVE + 1]
		}
		"root@root-x86-64 ~ #" {
			if {$LIVE == 6} { send "bootctl install\r" }
			if {$LIVE == 7} { send "echo quiet console=ttyS0 > /etc/kernel/cmdline\r" }
			if {$LIVE == 8} { send "kernel-install add \$(uname -r) /boot/gentoo\r" }
			if {$LIVE == 9} { send "exit\r" }
			set LIVE [expr $LIVE + 1]
		}
		"Please enter passphrase for disk" { send "\r" }
                "Last login:" { if {$LIVE >= 10} { exit } }
	}
}
