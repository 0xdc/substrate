# catalyst-scripts

These are scripts to simplify catalyst build stages in a rolling fashion.

## Portage snapshot sources

Instead of creating our own portage snapshots with `catalyst -s`, we can download pre-packed and distributed portage snapshots from:

*  the Gentoo [distfiles mirror /snapshots](http://distfiles.gentoo.org/snapshots)
   * these are recent snapshots (i.e. made in the past week)
   * older snapshots are rotated out
   * portage snapshots for the previous day are taken around 00:45 UTC on the following day
*  the [portage snapshot historical archives](https://dev.gentoo.org/~swift/snapshots/)
   * these are useful for upgrades of ancient stages that cannot directly upgrade to software in the recent snapshots
   * ebuilds often refer to source tarballs that are no longer available from original source mirror URLs (e.g. moved to archive folders)

Of course, these scripts do not prevent you from creating our own portage snapshots and building against them.

By default, the scripts will pull yesterday's (local time) portage snapshot.

## Architecture support

We target the following architectures:

* amd64 systemd
* armv7a hardfloat

The following targets are candidates for future support for various reasons:
* armv8 (aarch64)
* armv6j hardfp
* ppc32

## Dynamic versioning

We use text substitution to replace some hard-coded paths in spec files, in a similar vein to autoconf.
