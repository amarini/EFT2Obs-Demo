#!/usr/bin/env bash
set -x
set -e

### SET ENVIRONMENT VARIABLES HERE
MG_DIR="MG5_aMC_v2_6_5"
PROCESS="ggF_SMEFT"
#PROCESS="ggF"
RUNLABEL="pilotrun"
###

export PYTHIA8DATA=$PWD/${MG_DIR}/HEPTools/pythia8/share/Pythia8/xmldoc

cp cards/${PROCESS}/{param,reweight,run,pythia8}_card.dat ${MG_DIR}/${PROCESS}/Cards/

# Need to harcode the path to the FIFO, madgraph won't expand environment variables
sed -i "s@XTMPDIRX@${TMPDIR}@g" ${MG_DIR}/${PROCESS}/Cards/pythia8_card.dat


pushd ${MG_DIR}/${PROCESS}
# Create MG config
{
  echo "shower=Pythia8"
  echo "reweight=ON"
  echo "done"
} > mgrunscript

if [ -d "${MG_DIR}/${PROCESS}/Events/${RUNLABEL}" ]; then rm -r ${MG_DIR}/${PROCESS}/Events/${RUNLABEL}; fi
./bin/generate_events pilotrun < mgrunscript 
popd

rivet --analysis=HiggsTemplateCrossSections "${TMPDIR}/fifo.hepmc" -o Rivet.yoda
yoda2root Rivet.yoda
