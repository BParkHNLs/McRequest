# Instructions to test B->HNL generation


Release with *all* modifications is not yet available, therefore use this setup for the moment
```
cmsrel CMSSW_10_2_15
cd CMSSW_10_2_15/src
cmsenv
git cms-init

git cms-merge-topic mgratti:BHNL

git clone https://github.com/mgratti/McRequest.git 

mkdir Configuration/GenProduction/python/.
cp McRequest/fragments/BToNMuX_NToEMuPi_SoftQCD_b_mN3.0_ctau100.0mm_TuneCP5_13TeV_pythia8-evtgen_cfi.py Configuration/GenProduction/python/.

scram b -j 8

cmsDriver.py Configuration/GenProduction/python/BToNMuX_NToEMuPi_SoftQCD_b_mN3.0_ctau100.0mm_TuneCP5_13TeV_pythia8-evtgen_cfi.py \
--fileout file:BToNMuX_NToEMuPi_test.root \
--mc \
--eventcontent RAWSIM \
--datatier GEN \
--conditions 102X_upgrade2018_realistic_v11 \
--beamspot Realistic25ns13TeVEarly2018Collision \
--step GEN \
--geometry DB:Extended \
--era Run2_2018 \
--python_filename BToNMuX_NToEMuPi_mN3.0_ctau100.0mm_cfg.py \
--no_exec \
--customise Configuration/DataProcessing/Utils.addMonitoring \
-n 100
```

### Running tests
for Bc
/eos/home-m/mratti/BHNL_Bc_LHEtoRoot_step0_nj90.root
