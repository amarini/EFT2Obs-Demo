import os,sys


params={}

#default, down, up
#params['cH'] =(0.,-1.E-4,1.E-4)
params['cG'] =(0.,-1.E-2,1.E-2)
params['cGtil'] =(0.,-1.E-2,1.E-2)
#params['cHG'] =(0.,-1.E-4,1.E-4)
#params['cHW'] =(0.,-1.E-4,1.E-4)

################## END CONFIGURATION #######
vname = ('SM','down','up')

fout =open("reweight_card.dat","w")

print >> fout, "change rwgt_dir rwgt"
print >> fout, "change mode LO"

## default
print >> fout, "launch --rwgt_name=SM"
for nameSM in params:
    print >>fout, "   set",nameSM,params[nameSM][0]

## up down for param
for name in params:
    for v in [1,2]:
        print >> fout, "launch --rwgt_name=",'_'.join([name,vname[v]])
        print >>fout, "   set",name,params[name][v]
        for nameSM in params:
            if name != nameSM:print >>fout, "   set",nameSM,params[nameSM][0]


## 2D
for name in params:
    for name2 in params:
        if name ==name2: continue
        for v1,v2 in [ (a,b) for a in [1,2] for b in [1,2]]:
            print >> fout, "launch --rwgt_name=",'_'.join([name,vname[v1],name2,vname[v2]])
            print >>fout, "   set",name,params[name][v1]
            print >>fout, "   set",name,params[name2][v2]
            for nameSM in params:
                if name != nameSM and name2 != nameSM:print >>fout, "   set",nameSM,params[nameSM][0]
