# Disable loading the wrapt C library
# Since python is compiled with gcc and pip modules are built with tcc
export WRAPT_DISABLE_EXTENSIONS=1
# https://github.com/GrahamDumpleton/wrapt/blob/264c06fd3850bd0cda6917ca3e87417b573e023f/docs/changes.rst#version-11011
# https://github.com/GrahamDumpleton/wrapt/blob/264c06fd3850bd0cda6917ca3e87417b573e023f/src/wrapt/wrappers.py#L723
