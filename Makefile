# Makefile for source rpm: gstreamer-plugins-base
# $Id$
NAME := gstreamer-plugins-base
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
