# substrate

These are scripts to simplify catalyst build stages in a rolling fashion.
A substrate is a substance added to a catalysed reaction to create new products.

## Getting started

Substrate requires catalyst's dependencies and this repository has additional submodules that need to be pulled:

    # git submodule update --init
    # emerge -ao '>catalyst-3'

## Portage snapshot sources

Instead of creating our own portage snapshots with `catalyst -s`, we can download pre-packed and distributed portage snapshots from:

*  the Gentoo [distfiles squashfs archive /snapshots/squashfs](http://distfiles.gentoo.org/snapshots/squashfs)
   * contain the last 30 days of the gentoo portage tree, plus
   * one squashfs archive of each month since April 2016.
   * available in lzo and xz compression (squashfs-tools by default only works with xz)
   * portage snapshots for the previous day are taken around 01:45 UTC on the following day

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

Most of the specfile instructions are added programmatically during runtime, this keeps the specfiles
small and simple. These are expanded into temporary files and echo'd during runtime.
We use text substitution to replace some hard-coded paths in spec files, in a similar vein to autoconf,
by sed replacing some tokens surrounded by at-signs (@).
