proc handle_failures {} {
	puts $::expect_out(0,string)
	exec virsh pool-refresh default
	exit 2
}
set fail_messages "
	Shell>
	Reboot Into Firmware Interface
	crypt_init
	No space left on device
	No such file or directory
	efusing
	Kernel panic
"
set reasons [join [lmap reason [split $fail_messages \n] {
	set reason [string trim $reason]
	if {$reason == {}} continue
	set reason
}] |]
set failures "($reasons)"
