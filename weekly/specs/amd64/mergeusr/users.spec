profile: default/linux/amd64/17.1/no-multilib/systemd
source_subpath: amd64/mergeusr/stage3-amd64-mergeusr-latest
target: stage4

stage4/packages:
	acct-group/nginx
	acct-user/murmur
	acct-user/nginx
