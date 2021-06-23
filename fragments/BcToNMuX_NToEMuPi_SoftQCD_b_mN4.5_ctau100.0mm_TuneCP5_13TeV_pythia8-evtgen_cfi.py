
import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

# Production Info
configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Bc -> mu N X, with long-lived N, m=4.5GeV, ctau=100.0mm'),
    name = cms.untracked.string('Bc -> mu N X, with long-lived N, m=4.5GeV, ctau=100.0mm'),
    version = cms.untracked.string('$1.0$')
)

BFilter = cms.EDFilter("MCMultiParticleFilter",
   NumRequired = cms.int32(1),
   AcceptMore = cms.bool(True),
   ParticleID = cms.vint32(541),
   PtMin = cms.vdouble(0.),
   EtaMax = cms.vdouble(10.),
   Status = cms.vint32(0), 
)

BToNMuXFilter = cms.EDFilter("PythiaFilterMotherSister", 
    MaxEta = cms.untracked.double(1.55),
    MinEta = cms.untracked.double(-1.55),
    MinPt = cms.untracked.double(6.8), 
    ParticleID = cms.untracked.int32(13),
    MotherIDs = cms.untracked.vint32(541), 
    SisterID = cms.untracked.int32(9900015), 
    MaxSisterDisplacement = cms.untracked.double(1300.), # max Lxy displacement to generate in mm, -1 for no max
    NephewIDs = cms.untracked.vint32(11,13,211), # ids of the nephews you want to check the pt of
    MinNephewPts = cms.untracked.vdouble(0.4,0.4,0.5), 
)

generator = cms.EDFilter("Pythia8HadronizerFilter",
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            convertPythiaCodes = cms.untracked.bool(False),
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            
            list_forced_decays = cms.vstring(       
                'myBc+', 
                'myBc-',
            ),
            
            operates_on_particles = cms.vint32(541, -541), 
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_BHNL_mass4.5_ctau100.0_maj.pdl'),
            user_decay_file = cms.vstring('GeneratorInterface/EvtGenInterface/data/HNLdecay_mass4.5_maj_emu_Bc.DEC'),
        ),
        parameterSets = cms.vstring('EvtGen130'),
    ),

    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring('541:m0 = 6.275',
                                        '541:tau0 = 0.153',
                                        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    ),
    ),

    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(-1),      # this will not be used by Pythia, only saved in GenInfo 
    maxEventsToPrint = cms.untracked.int32(0),        
    pythiaHepMCVerbosity = cms.untracked.bool(False), 
    pythiaPylistVerbosity = cms.untracked.int32(0),
)


ProductionFilterSequence = cms.Sequence(generator+BFilter+BToNMuXFilter)

