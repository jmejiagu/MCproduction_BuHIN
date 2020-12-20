import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
#from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
        pythiaPylistVerbosity = cms.untracked.int32(0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        crossSection = cms.untracked.double(0),
        comEnergy = cms.double(8160.0),
        maxEventsToPrint = cms.untracked.int32(0),
        ExternalDecays = cms.PSet(
            EvtGen130 = cms.untracked.PSet(
                decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
                particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
                user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Bu_JpsiK.dec'),
                list_forced_decays = cms.vstring('MyB+',
                                                 'MyB-'),
                operates_on_particles = cms.vint32()
            ),
            parameterSets = cms.vstring('EvtGen130')
        ),
        PythiaParameters = cms.PSet(
            pythia8CommonSettingsBlock,
            pythia8CUEP8M1SettingsBlock,
            processParameters = cms.vstring(
                'HardQCD:all = on',
                'PhaseSpace:pTHatMin = 5.',
            ),
            parameterSets = cms.vstring('pythia8CommonSettings',
                                        'pythia8CUEP8M1Settings',
                                        'processParameters',
            )
        )
)

#generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

###########
# Filters #
###########

bgenfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(321),
    MaxEta = cms.untracked.vdouble(9999.),
    MinEta = cms.untracked.vdouble(-9999.),
    MinPt = cms.untracked.vdouble(-1.0),
    NumberDaughters = cms.untracked.int32(1),
    ParticleID = cms.untracked.int32(521),
    verbose = cms.untracked.int32(0)
)

mumugenfilter = cms.EDFilter("PythiaDauVFilter",
    DaughterIDs = cms.untracked.vint32(-13, 13),
    MaxEta = cms.untracked.vdouble(9999.,9999.),
    MinEta = cms.untracked.vdouble(-9999., -9999.),
    MinPt = cms.untracked.vdouble(-1., -1.),
    MotherID = cms.untracked.int32(521),
    NumberDaughters = cms.untracked.int32(2),
    ParticleID = cms.untracked.int32(443),
    verbose = cms.untracked.int32(0)
)

ProductionFilterSequence = cms.Sequence(generator*bgenfilter*mumugenfilter)

"""
mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.0, 0.0),#0.5, 0.5
    MinP = cms.untracked.vdouble(0., 0.),
    MaxEta = cms.untracked.vdouble(10000.0, 10000.0),#2.5, 2.5
    MinEta = cms.untracked.vdouble(-10000.0, -10000.0),#-2.5, -2.5
    MinInvMass = cms.untracked.double(0.0),#2.0
    MaxInvMass = cms.untracked.double(100.0),#4.0
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

BJpsiDaufilter = cms.EDFilter("PythiaMomDauFilter",
    ParticleID = cms.untracked.int32(521),
    MomMinPt = cms.untracked.double(0.0),#5.0
    MomMinEta = cms.untracked.double(-2.8),
    MomMaxEta = cms.untracked.double(2.8),
    DaughterIDs = cms.untracked.vint32(443, 321),
    NumberDaughters = cms.untracked.int32(2),
    DaughterID = cms.untracked.int32(443),
    DescendantsIDs = cms.untracked.vint32(13, -13),
    NumberDescendants = cms.untracked.int32(2),
    MinEta = cms.untracked.double(-2.5),#-2.5
    MaxEta = cms.untracked.double(2.5),#2.5
)

#ProductionFilterSequence = cms.Sequence(generator*mumugenfilter*BJpsiDaufilter)
ProductionFilterSequence = cms.Sequence(generator*BJpsiDaufilter)
"""
