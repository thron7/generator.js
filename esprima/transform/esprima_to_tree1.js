#! /usr/bin/env node

/**
 * Transform Esprima/Moziall Parser API AST into treegenerator_1 AST.
 */

var tree1 = require('tree1');

function esprima_to_tree1 (tree) {
  var tree_1 = new tree1.Node();
  return tree_1;
}

module.exports = esprima_to_tree1;
