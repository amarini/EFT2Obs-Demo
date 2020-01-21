import os,sys


params = {
    "ceWPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "ceBPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cuGPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cuWPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cuBPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cdGPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cdWPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cdBPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHudPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "ceHPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cuHPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cdHPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cledqPh" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cquqd1Ph" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cquqd8Ph" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "clequ1Ph" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "clequ3Ph" : { "SM_value" : 0.000000e+00, "variation_range" : [-0.1, 0.1] },
    "LambdaSMEFT" : { "SM_value" : 1.000000e+03, "variation_range" : [-0.1, 0.1] },
    "cG" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cGtil" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cW" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cWtil" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cH" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHbox" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHDD" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHG" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHGtil" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHW" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHWtil" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHB" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHBtil" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHWB" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHWBtil" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "ceHAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cuHAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cdHAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "ceWAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "ceBAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cuGAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cuWAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cuBAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cdGAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cdWAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cdBAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHl1" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHl3" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHe" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHq1" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHq3" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHu" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHd" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cHudAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cll" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cll1" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cqq1" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cqq11" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cqq3" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cqq31" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "clq1" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "clq3" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cee" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cuu" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cuu1" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cdd" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cdd1" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "ceu" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "ced" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cud1" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cud8" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cle" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "clu" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cld" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cqe" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cqu1" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cqu8" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cqd1" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cqd8" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cledqAbs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cquqd1Abs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "cquqd8Abs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "clequ1Abs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] },
    "clequ3Abs" : { "SM_value" : 1.000000e+00, "variation_range" : [-0.1, 0.1] }
}

################## END CONFIGURATION #######
vname = ('SM','down','up')

fout =open("reweight_card.dat","w")

print >> fout, "change rwgt_dir rwgt"
print >> fout, "change mode LO"

## default
print >> fout, "launch --rwgt_name=SM"
for pname in params.keys():
    print >> fout, "   set", pname, params[pname]["SM_value"]

## up down for param
for par in params.keys():
    for v,variation in enumerate(params[par]["variation_range"]):
        print >> fout
        print >> fout, "launch --rwgt_name=",'_'.join([par,vname[v+1]])
        print >> fout, "   set", par, str(params[par]["SM_value"]+variation)
        for other in params.keys():
            if other != par:
                print >> fout, "   set", other, params[other]["SM_value"]


## 2D
# for name in params:
#     for name2 in params:
#         if name ==name2: continue
#         for v1,v2 in [ (a,b) for a in [1,2] for b in [1,2]]:
#             print >> fout, "launch --rwgt_name=",'_'.join([name,vname[v1],name2,vname[v2]])
#             print >>fout, "   set",name,params[name][v1]
#             print >>fout, "   set",name,params[name2][v2]
#             for nameSM in params:
#                 if name != nameSM and name2 != nameSM:print >>fout, "   set",nameSM,params[nameSM][0]
