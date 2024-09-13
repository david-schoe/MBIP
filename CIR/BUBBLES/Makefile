###
																###
###		A COPY OF THIS FILE EXISTS AS .mfb SHOULD ANYTHING HAPPEN TO THIS (ACCIDENTAL FILE DESTRUCTION)
																###
###
																###



# ENV VARIABLES


export DOT0=$(shell pwd)

MAKEFLAGS += --no-print-directory

#.SILENT:

SHELL = /bin/bash

OBJ0 = bub
OBJS0 = bubs

SPEC0 = vid
SPECS0 = vids

# BUILDER

build: $(DOT0)/.timestamp

$(DOT0)/.timestamp: $(SPECS0) $(OBJS0)
	n=$$(cat .nobjn); \
	for spec in $$(ls $(SPECS0)); do \
		ext=$${spec##*.}; \
		nameext=$${spec##*/}; \
		name=$${nameext%.*}; \
		obj=$$(printf "$(OBJ0)_%04d" $${n}); \
		echo "building $${obj} ..."; \
		dir=$(DOT0)/$(OBJS0)/$${obj}; \
		mkdir $${dir}; \
		echo $${ext} > $${dir}/$(SPEC0)ext; \
		echo $${name} > $${dir}/$(SPEC)name; \
		ln .mf0 $(OBJS0)/$${obj}/Makefile; \
		ln -s $(DOT0)/.lib $${dir}/.lib; \
		cp $(SPECS0)/$${spec} $${dir}/$(SPEC0).$${ext}; \
		make -C $(OBJS0)/$${obj}; \
		n=$$((n+1)); \
	done; \
	echo $${n} > .nobjn

$(OBJS0):
	mkdir "$(DOT0)/$(OBJS0)"


# METHODs


order:
	./.lib/ord.sh

clean: /tmp/BU
	rm -r $(OBJS0); \
	rm .nobjn

update-all:
	./.lib/upd.sh



# METADATA


.nobjn:
	echo 0 > .nobjn

/tmp/BU:
	mkdir /tmp/BU


