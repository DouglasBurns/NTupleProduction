import FWCore.ParameterSet.Config as cms
rootTupleEvent = cms.EDProducer(
        "BristolNTuple_Event",
        DCSInputTag=cms.InputTag('scalersRawToDigi'),
        HCALLaserFilterInput=cms.InputTag('HcalLaserEventFilter'),
        ECALDeadCellFilterInput=cms.InputTag('EcalDeadCellBoundaryEnergyFilter'),
        TrackingFailureFilterInput=cms.InputTag('trackingFailureFilter'),
        Prefix=cms.string('Event.'),
        Suffix=cms.string('')
)
