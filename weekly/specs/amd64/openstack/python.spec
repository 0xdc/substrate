profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/systemd/stage3-amd64-systemd-latest
target: embedded
portage_confdir: @REPO_DIR@/confdirs/openstack
portage_overlay: @REPO_DIR@/overlay

embedded/root_overlay: @REPO_DIR@/root_overlays/openstack
embedded/use:
	-uwsgi_plugins_*

# These packages are enough to install the basic OpenStack services
embedded/packages:
	dev-python/netifaces
	dev-python/psutil
	dev-python/rcssmin
	dev-python/scrypt
	dev-python/setproctitle
	dev-python/yappi
	www-servers/uwsgi[python]
