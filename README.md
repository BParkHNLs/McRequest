# Instructions to test B->HNL generation


Release with *all* modifications is now available (validation test was performed)
```
cmsrel CMSSW_10_2_27
cd CMSSW_10_2_27/src
cmsenv
git cms-init

git clone https://github.com/mgratti/McRequest.git 
```

Test a single Bu/Bd/Bs sample
```
mkdir -p Configuration/GenProduction/python/.
cp McRequest/fragments/BToNMuX_NToEMuPi_SoftQCD_b_mN3.0_ctau100.0mm_TuneCP5_13TeV_pythia8-evtgen_cfi.py Configuration/GenProduction/python/fragment_BuBdBs.py

scram b -j 8

cmsDriver.py Configuration/GenProduction/python/fragment_BuBdBs.py --fileout file:BToNMuX_NToEMuPi_test.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --geometry DB:Extended --era Run2_2018 --python_filename test_BuBdBs.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100
```

Test a single Bc sample
```
mkdir -p Configuration/GenProduction/python/.
cp McRequest/fragments/BcToNMuX_NToEMuPi_SoftQCD_b_mN3.0_ctau100.0mm_TuneCP5_13TeV_pythia8-evtgen_cfi.py Configuration/GenProduction/python/fragment_Bc.py

scram b -j 8

cmsDriver.py Configuration/GenProduction/python/fragment_Bc.py --fileout file:BcToNMuX_NToEMuPi_test.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --geometry DB:Extended --era Run2_2018 --python_filename test_Bc.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100 --filein  root://eosuser.cern.ch//eos/user/m/mratti/BHNL_Bc_LHEtoRoot_step0_nj90.root
```

The filter efficiencies can be found in ```./efficiencies```. The format of the file can be read as: 
```
mass,  ctau(mm), filter eff, time/evt [after filter] (s) 
(1.0,  10000.00, 1.69e-04, 427),
```

LHE files for Bc sample stored on eos
```
/eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for201*/*
```

