###
																###
###		A COPY OF THIS FILE EXISTS AS .Makefile SHOULD ANYTHING HAPPEN TO THIS (ACCIDENTAL FILE DESTRUCTION)
																###
### 		PLEASE NOTE THAT A CALL TO MAKE WILL NOT FUNCTION UNLESS $(VID) IS DEFINED.
																###



# ENV VARIABLES


export DOT=$(shell pwd)

MAKEFLAGS += --no-print-directory

.SILENT: obj




# BUILDER


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




# METADATA


.oname:
	echo bub > .oname

oup: .nobjn
	./.lib/oup.sh

.nobjn:
	echo 0 > .nobjn

/tmp/BU:
	mkdir /tmp/BU


