#!/usr/bin/env bash
set -x
set -e

source env.sh

if [ -z "${MG_DIR}" ]; then echo "ERROR: environment variable MG_DIR is not set"; exit 1; fi

## todo, use feynrules site and not the copy. Add a possible loop
pushd ${MG_DIR}/models
wget --no-check-certificate https://feynrules.irmp.ucl.ac.be/raw-attachment/wiki/SMEFT/SMEFTsim_A_U35_MwScheme_UFO_v2.1.tar.gz
tar -zxf SMEFTsim_A_U35_MwScheme_UFO_v2.1.tar.gz
rm SMEFTsim_A_U35_MwScheme_UFO_v2.1.tar.gz
popd
