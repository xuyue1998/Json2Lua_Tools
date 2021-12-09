#@deltaxu

import jsontolua
import os
import os.path

Inputpath = os.path.pardir
Outputpath = os.path.pardir
matchlist = []
Floderlist = os.listdir(Inputpath)

for var in Floderlist:
   splitedname = var.split('.')
   if "json" in splitedname:
      matchlist.append(splitedname[0])

for name in matchlist:
   jsontolua.file_to_lua_file(Outputpath + '/' + name + '.json',Outputpath + '/' + name + '.lua')
   print("Out:" + name + '.lua')

print ("Done")
