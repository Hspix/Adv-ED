dataPath = "./"
SenLen = 60
MaxPos = 2 * SenLen
LocalLen = 1
dimWE = 300
dimPE = 5
dimC = 200
dimE = 22
filter_size = 3
keepProb = 0.5
Epoch = 7
BatchSize = 170
vec_file = "wiki.multi.en.vec"
AugTimes = 1
NegCnt = 20
Threshold = 6
ItemTimes = 10
alpha = 4.0
sLr = 0.005
dLr = 0.02
EncodedDim = 2 * dimC + (2 * LocalLen + 1) * dimWE
