
import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

# Production Info
configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Bc -> mu N X, with long-lived N, m=5.5GeV, ctau=0.0mm'),
    name = cms.untracked.string('Bc -> mu N X, with long-lived N, m=5.5GeV, ctau=0.0mm'),
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

DoubleMuFilter = cms.EDFilter("MCParticlePairFilter",
    MaxEta = cms.untracked.vdouble(1.55, 2.45), 
    MinEta = cms.untracked.vdouble(-1.55, -2.45),
    MinPt = cms.untracked.vdouble(6.8, 1.0),
    ParticleID1 = cms.untracked.vint32(-13, 13),
    ParticleID2 = cms.untracked.vint32(-13, 13),
    MaxInvMass = cms.untracked.double(10.),
    Status = cms.untracked.vint32(1, 1),
)

HNLDisplacementFilter = cms.EDFilter("PythiaFilterMotherSister", 
    ParticleID = cms.untracked.int32(13),
    MotherIDs = cms.untracked.vint32(541),
    SisterID = cms.untracked.int32(9900015),
    MaxSisterDisplacement = cms.untracked.double(1300.),
    NephewIDs = cms.untracked.vint32(13,211),
    MinNephewPts = cms.untracked.vdouble(0.4, 0.5),
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
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_BHNL_mass5.5_ctau0.01_maj.pdl'),
            user_decay_embedded = cms.vstring(
              
               'Alias myB+ B+',
               'Alias myBc+ B_c+',
               'Alias myBc- B_c-',
               'ChargeConj myBc+ myBc-',
               'Decay myBc+',
               '13.1417801672               mu+    hnl    PHSP;',
               'Enddecay',
               'CDecay myBc-',
               'Decay hnl',
               '0.5     mu-    pi+    PHSP;',
               '0.5     mu+    pi-    PHSP;',
               'Enddecay',
               'End',      

            )
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
    maxEventsToPrint = cms.untracked.int32(0),        
    pythiaHepMCVerbosity = cms.untracked.bool(False), 
    pythiaPylistVerbosity = cms.untracked.int32(0),
)

ProductionFilterSequence = cms.Sequence(generator+BFilter+DoubleMuFilter+HNLDisplacementFilter)

