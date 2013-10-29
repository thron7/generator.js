#!/usr/bin/env python

import re, os, sys, types, codecs
REL_QOOXDOO_PATH = os.path.abspath(os.path.dirname(__file__) + "/../../../../qooxdoo.git")
execfile(REL_QOOXDOO_PATH + "/tool/bin/qxenviron.py")
from ecmascript.transform import moztree_to_tree1
from generator.runtime.ShellCmd import ShellCmd
from misc import json

shell = ShellCmd()
cmd = "esparse --raw --loc " + sys.argv[1]
#print cmd
rcode, stdout, errout = (
    shell.execute_piped(cmd))
if rcode != 0:
    print errout
    sys.exit(1)
tree_json = json.loads(stdout)
node = moztree_to_tree1.esprima_to_tree1(tree_json)
print node.toXml()
#import pydb; pydb.debugger()
def opts():pass
opts.breaks = True
#print node.toJS(opts)
