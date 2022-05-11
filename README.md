# Instructions to test B->HNL generation

## Installation
Release with *all* modifications is now available (validation test was performed)
```
cmsrel CMSSW_10_2_28_patch1
cd CMSSW_10_2_28_patch1/src
cmsenv
git cms-init

git clone https://github.com/mgratti/McRequest.git 
cd McRequest
source setup.sh
```

### After first installation
```
cd CMSSW_10_2_28_patch1/src/McRequest
cmsenv
source setup.sh
```

## Directory structure

### The [./efficiencies](./efficiencies) directory
It is used to create the .csv file that is needed for the request: [makeCsv.py](./efficiencies/makeCsv.py).
Please, note that the inputs for this script need to be manually, starting from the information provided by [getFilterEff.py](./slurm/getFilterEff.py), and from the final estimates of the requested statistics (this was done in spreadsheets, see [presentation](https://indico.cern.ch/event/1054487/contributions/4431389/attachments/2278382/3873756/2021_07_07_Bpark_Signal_forEXO.pdf).

### The [./evtGenData](./evtGenData) directory
It is at this point useless, as all this data is already included in the distributions of CMSSW and CMS-data, so it is not used while running tests.
It contains the final versions of the .DEC and .pdl files.

### The [./fragments](./fragments) directory
It contains the final fragments that were used for the request

### The [./python](./python) directory
It contains a copy of the `objects.py`, `decays.py`, `common.py` libraries.
In truth only the class `Point` is used.

### The [./slurm](./slurm) directory
It is used to run the sample production


## Tests

### Single tests
Test a single Bu/Bd/Bs sample
```
mkdir -p Configuration/GenProduction/python/.
cp McRequest/fragments/BToNMuX_NToEMuPi_SoftQCD_b_mN3.0_ctau100.0mm_TuneCP5_13TeV_pythia8-evtgen_cfi.py Configuration/GenProduction/python/fragment_BuBdBs.py

scram b -j 8

cmsDriver.py Configuration/GenProduction/python/fragment_BuBdBs.py --fileout file:BToNMuX_NToEMuPi_test.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --geometry DB:Extended --era Run2_2018 --python_filename test_BuBdBs.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100 --mc
```

Test a single Bc sample
```
mkdir -p Configuration/GenProduction/python/.
cp McRequest/fragments/BcToNMuX_NToEMuPi_SoftQCD_b_mN3.0_ctau100.0mm_TuneCP5_13TeV_pythia8-evtgen_cfi.py Configuration/GenProduction/python/fragment_Bc.py

scram b -j 8

cmsDriver.py Configuration/GenProduction/python/fragment_Bc.py --fileout file:BcToNMuX_NToEMuPi_test.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --geometry DB:Extended --era Run2_2018 --python_filename test_Bc.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100 --filein  root://eosuser.cern.ch//eos/user/m/mratti/BHNL_Bc_LHEtoRoot_step0_nj90.root --mc
```

### Production tests
To test a production, use the [centralProdHelper.py](./slurm/centralProdHelper.py)








