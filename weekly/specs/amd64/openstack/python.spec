profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/systemd/stage3-amd64-systemd-latest
target: embedded
portage_confdir: @REPO_DIR@/confdirs/openstack

# tcc: to build python C extensions from pip
# liberasurecode: required for swift
# git: download horizon source, or bleeding edge pips
# linux-headers: headers for tcc builds
# uwsgi: (dev) web server for keystone
#        pulls in python
embedded/packages:
	dev-lang/tcc
	dev-libs/liberasurecode
	dev-vcs/git
	sys-kernel/linux-headers
	www-servers/uwsgi
