#!/usr/bin/env bash
set -x
set -e

source env.sh

if [ -z "${MG_DIR}" ]; then echo "ERROR: environment variable MG_DIR is not set"; exit 1; fi

## todo, use feynrules site and not the copy. Add a possible loop
pushd ${MG_DIR}/models
wget --no-check-certificate https://amarini.web.cern.ch/amarini/SMEFTsim_A_general_MwScheme_UFO_v2.tar.gz
tar -zxf SMEFTsim_A_general_MwScheme_UFO_v2.tar.gz
rm SMEFTsim_A_general_MwScheme_UFO_v2.tar.gz
popd
