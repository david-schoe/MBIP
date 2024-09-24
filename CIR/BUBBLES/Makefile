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
		echo $${dir} >> .bfp; \
	done; \
	echo $${n} > .nobjn

$(OBJS0):
	mkdir "$(DOT0)/$(OBJS0)"


new_study: studys .nstdn
	n=$$(cat .nstdn); \
	fil=$$(printf "studys/study_%02d.py" $${n}); \
	cp .study_template $${fil}; \
	echo $$((n+1)) > .nstdn; \
	nano $${fil}


run_study: studys
	s=$$(printf "study_%02d" $(S)); \
	PYTHONPATH="$(shell pwd)/.lib/plib:$(shell pwd)/studys" py -m $${s} &


studys:
	mkdir studys



# METHODs


order:
	./.lib/ord.sh

clean: /tmp/BU
	rm -r $(OBJS0); \
	rm .bfp; \
	rm -r studys; \
	rm .nobjn; \
	rm .nstdn

update-all:
	./.lib/upd.sh



# METADATA
.nstdn:
	echo 0 > .nstdn

.nobjn:
	echo 0 > .nobjn

/tmp/BU:
	mkdir /tmp/BU


