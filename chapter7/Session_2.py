from treepredict import *

tree = buildtree(my_data)
printtree(tree)

drawtree(tree,jpeg='treeview.jpg')

def classify(observation,tree):
  if tree.results!=None:
    return tree.results
  else:
    v=observation[tree.col]
    branch=None
    if isinstance(v,int) or isinstance(v,float):
      if v>=tree.value: branch=tree.tb
      else: branch=tree.fb
    else:
      if v==tree.value: branch=tree.tb
      else: branch=tree.fb
    return classify(observation,branch)

classify(['(direct)','USA','yes',5],tree)

def prune(tree,mingain, scoref=entropy):
  # If the branches aren't leaves, then prune them
  if tree.tb.results==None:
    prune(tree.tb,mingain)
  if tree.fb.results==None:
    prune(tree.fb,mingain)
    
  # If both the subbranches are now leaves, see if they
  # should merged
  if tree.tb.results!=None and tree.fb.results!=None:
    # Build a combined dataset
    tb,fb=[],[]
    for v,c in tree.tb.results.items():
      tb+=[[v]]*c
    for v,c in tree.fb.results.items():
      fb+=[[v]]*c
    
    # Test the reduction in entropy
    delta=scoref(tb+fb)-(scoref(tb)+scoref(fb)/2)

    if delta<mingain:
      # Merge the branches
      tree.tb,tree.fb=None,None
      tree.results=uniquecounts(tb+fb)


new_tree = buildtree(my_data)
prune(new_tree,0.1)
printtree(new_tree)

prune(new_tree, 1.0)
printtree(new_tree)

classify(['(direct)','USA','yes',5],tree)
classify(['(direct)','USA','yes',5],new_tree)


def mdclassify(observation,tree):
  if tree.results!=None:
    return tree.results
  else:
    v=observation[tree.col]
    if v==None:
      tr,fr=mdclassify(observation,tree.tb),mdclassify(observation,tree.fb)
      tcount=sum(tr.values())
      fcount=sum(fr.values())
      tw=float(tcount)/(tcount+fcount)
      fw=float(fcount)/(tcount+fcount)
      result={}
      for k,v in tr.items(): result[k]=v*tw
      for k,v in fr.items(): result[k]=v*fw      
      return result
    else:
      if isinstance(v,int) or isinstance(v,float):
        if v>=tree.value: branch=tree.tb
        else: branch=tree.fb
      else:
        if v==tree.value: branch=tree.tb
        else: branch=tree.fb
      return mdclassify(observation,branch)


mdclassify(['google',None,'yes',None],tree)
mdclassify(['google','France',None,None],tree)

#call http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz19u6ad6um17_6a5jo&2114&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA

import zillow
zillow.zwskey='X1-ZWz19u6ad6um17_6a5jo'
housedata=zillow.getpricelist()

cleansed_housedata=[]
for row in housedata: 
   ....:     if row != None: 
   ....:         cleansed_housedata.append(row)

reload(treepredict)

housetree=treepredict.buildtree(cleansed_housedata,scoref=treepredict.variance)
treepredict.drawtree(housetree,'housetree.jpg')

new_housetree = housetree
prune(new_housetree,0.1, scoref=treepredict.variance)
printtree(new_housetree)
prune(new_housetree,1.0, scoref=treepredict.variance)
printtree(new_housetree)
prune(new_housetree,2.0, scoref=treepredict.variance)
printtree(new_housetree)


treepredict.drawtree(new_housetree,'new_housetree.jpg')











