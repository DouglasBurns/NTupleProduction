from BristolAnalysis.NTupleTools.commonConfig import config

config.General.requestName = 'QCD_EMEnriched_50to80'
config.Data.inputDataset = '/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.publishDataName = 'QCD_EMEnriched_50to80'
