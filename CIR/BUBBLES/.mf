###
																###
###		A COPY OF THIS FILE EXISTS AS .mfb SHOULD ANYTHING HAPPEN TO THIS (ACCIDENTAL FILE DESTRUCTION)
																###
###
																###



# ENV VARIABLES


export DOT=$(shell pwd)

export DOTDOT=$(shell cat .dotdot)

MAKEFLAGS += --no-print-directory

.SILENT: obj




# BUILDER

all: $(DOT)/.timestamp

$(DOT)/.timestamp: bld_specs
	./.lib/bld.sh



# OBJECT


obj: oup
	DIR=$$(tail -n 1 .objd) ;\
	echo "building $${DIR} ..." ;\
	mkdir "$(DOT)/$${DIR}"
	./.lib/obj.sh




# METHODs


order:
	./.lib/ord.sh

remove: /tmp/BU
	./.lib/rmv.sh $(RM)

clean: /tmp/BU
	./.lib/cln.sh

update-mfs:
	./.lib/mnp.sh

update-all:
	./.lib/upd.sh

bld_specs:
	./.lib/bds.sh


# METADATA


.oname:
	echo bub > .oname

oup: .nobjn
	./.lib/oup.sh

.nobjn:
	echo 0 > .nobjn

/tmp/BU:
	mkdir /tmp/BU


