
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('B -> mu N X, with long-lived N, m=1.0GeV, ctau=1000.0mm'),
    name = cms.untracked.string('B -> mu N X, with long-lived N, m=1.0GeV, ctau=1000.0mm'),
    version = cms.untracked.string('$1.0$')
)

process.BFilter = cms.EDFilter("MCMultiParticleFilter",
   NumRequired = cms.int32(1),
   AcceptMore = cms.bool(True),
   ParticleID = cms.vint32(521,511,531),
   PtMin = cms.vdouble(0.,0.,0.),
   EtaMax = cms.vdouble(10.,10.,10.),
   Status = cms.vint32(0,0,0), 
)

process.BToNMuXFilter = cms.EDFilter("PythiaFilterMotherSister", 
    MaxEta = cms.untracked.double(1.55),
    MinEta = cms.untracked.double(-1.55),
    MinPt = cms.untracked.double(6.8), 
    ParticleID = cms.untracked.int32(13),
    MotherIDs = cms.untracked.vint32(521, 511, 531), 
    SisterID = cms.untracked.int32(9900015), 
    MaxSisterDisplacement = cms.untracked.double(1300.), # max Lxy displacement to generate in mm, -1 for no max
    NephewIDs = cms.untracked.vint32(11,13,211), # ids of the nephews you want to check the pt of
    MinNephewPts = cms.untracked.vdouble(0.4,0.4,0.5), 
)

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            convertPythiaCodes = cms.untracked.bool(False),
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            
            list_forced_decays = cms.vstring(       
                'myB+', 
                'myB-',
                'myB0',
                'myB0bar',
                'myB0s',
                'myB0sbar',
            ),
            
            operates_on_particles = cms.vint32(521, -521, 511, -511, 531, -531), 
            particle_property_file = cms.FileInPath('McRequest/evtGenData/evt_2014_mass1.0_ctau1000.0_maj.pdl'),
            user_decay_file = cms.vstring('McRequest/evtGenData/HNLdecay_mass1.0_maj_emu.DEC'),
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),

    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring('SoftQCD:nonDiffractive = on',
                                        'PTFilter:filter = on',      
                                        'PTFilter:quarkToFilter = 5', 
                                        'PTFilter:scaleToFilter = 5.0',
                                        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
    ) 

    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(-1),      # this will not be used by Pythia, only saved in GenInfo 
    crossSection = cms.double(1.0)
    maxEventsToPrint = cms.untracked.int32(0),        
    pythiaHepMCVerbosity = cms.untracked.bool(False), 
    pythiaPylistVerbosity = cms.untracked.int32(0)    
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.BFilter+process.BToNMuXFilter)

