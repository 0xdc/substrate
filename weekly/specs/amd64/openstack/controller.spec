portage_confdir: @REPO_DIR@/confdirs/controller
profile: default/linux/amd64/23.0/no-multilib/systemd
source_subpath: amd64/systemd/stage3-amd64-systemd-latest
target: embedded

embedded/root_overlay: @REPO_DIR@/root_overlays/openstack

# liberasurecode: required for swift
# git: download horizon source, or bleeding edge pips
# coreutils: useful utils (e.g. mkdir, ls)
# sed: used by rabbitctl
# binutils: allows gcc to link binaries
# gcc: to build python C extensions from pip
# linux-headers: headers for gcc builds
# rabbit: message queue
# uwsgi: (dev) web server for api services
#        pulls in python
embedded/packages:
	dev-libs/liberasurecode
	dev-vcs/git
	sys-apps/coreutils
	sys-apps/iproute2
	sys-apps/sed
	sys-devel/binutils
	sys-devel/gcc
	sys-kernel/linux-headers
	>=net-misc/rabbitmq-server-3.7.24
	www-servers/uwsgi

# Install mask takes wildcards
install_mask:
        /etc/c*
        /etc/f*
        /etc/g*
        /etc/h*
        /etc/i*
        /etc/l*
        /etc/m*
        /etc/n*
        /etc/passwd*
        /etc/r*
        /etc/sh*
        /etc/ssl/*.cnf
        /etc/sys*
        /etc/x*

# rm must be exact
embedded/rm:
        /etc/X11
        /etc/binfmt.d
        /etc/dbus-1
        /etc/env.d
        /etc/kernel
        /etc/sandbox.d
        /etc/services
        /etc/skel
        /etc/ssl/misc
        /etc/ssl/private
        /etc/tmpfiles.d
        /etc/udev
        /usr/lib/tmpfiles.d/portables.conf
        /usr/share/bash-completion
        /usr/share/doc
        /usr/share/info
        /usr/share/man
        /usr/share/terminfo
        /usr/share/zsh
        /var
