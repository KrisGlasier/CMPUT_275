
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTID AND OR NOT TRUE FALSE LPAREN RPARENexpression : expression_false\n                | expression_trueexpression_true : TRUE\n                | expression_true AND expression_true\n                | expression_true OR expression_true\n                | expression_true OR expression_false\n                | expression_false OR expression_true\n                | NOT expression_false\n                | LPAREN expression_true RPARENexpression_false : FALSE\n                | NOT expression_true\n                | expression_false AND expression_true\n                | expression_true AND expression_false\n                | expression_false AND expression_false\n                | expression_false OR expression_false\n                | LPAREN expression_false RPARENexpression : ID'
    
_lr_action_items = {'NOT':([0,2,6,9,12,13,14,15,16,21,22,],[2,9,2,2,9,9,2,2,9,9,9,]),'OR':([3,4,5,8,10,11,17,18,19,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[14,16,-10,-3,-8,-11,14,16,-8,-11,21,16,-14,-12,-15,-7,-13,-4,-6,-5,-16,-9,-15,-7,-13,-4,]),'AND':([3,4,5,8,10,11,17,18,19,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[13,15,-10,-3,-8,-11,13,15,-8,-11,13,22,-14,-12,13,15,-13,-4,13,22,-16,-9,13,22,-13,-4,]),'$end':([1,3,4,5,7,8,10,11,19,20,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[0,-1,-2,-10,-17,-3,-8,-11,-8,-11,-14,-12,-15,-7,-13,-4,-6,-5,-16,-9,-15,-7,-13,-4,]),'FALSE':([0,2,6,9,12,13,14,15,16,21,22,],[5,5,5,5,5,5,5,5,5,5,5,]),'LPAREN':([0,2,6,9,12,13,14,15,16,21,22,],[6,12,6,6,12,12,6,6,12,12,12,]),'ID':([0,],[7,]),'TRUE':([0,2,6,9,12,13,14,15,16,21,22,],[8,8,8,8,8,8,8,8,8,8,8,]),'RPAREN':([5,8,10,11,17,18,19,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,],[-10,-3,-8,-11,33,34,-8,-11,33,34,-14,-12,-15,-7,-13,-4,-6,-5,-16,-9,-15,-7,-13,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'expression_false':([0,2,6,9,12,13,14,15,16,21,22,],[3,10,17,19,23,25,27,29,31,35,37,]),'expression_true':([0,2,6,9,12,13,14,15,16,21,22,],[4,11,18,20,24,26,28,30,32,36,38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression_false','expression',1,'p_expression','boolean.py',68),
  ('expression -> expression_true','expression',1,'p_expression','boolean.py',69),
  ('expression_true -> TRUE','expression_true',1,'p_expression_true','boolean.py',73),
  ('expression_true -> expression_true AND expression_true','expression_true',3,'p_expression_true','boolean.py',74),
  ('expression_true -> expression_true OR expression_true','expression_true',3,'p_expression_true','boolean.py',75),
  ('expression_true -> expression_true OR expression_false','expression_true',3,'p_expression_true','boolean.py',76),
  ('expression_true -> expression_false OR expression_true','expression_true',3,'p_expression_true','boolean.py',77),
  ('expression_true -> NOT expression_false','expression_true',2,'p_expression_true','boolean.py',78),
  ('expression_true -> LPAREN expression_true RPAREN','expression_true',3,'p_expression_true','boolean.py',79),
  ('expression_false -> FALSE','expression_false',1,'p_expression_false','boolean.py',84),
  ('expression_false -> NOT expression_true','expression_false',2,'p_expression_false','boolean.py',85),
  ('expression_false -> expression_false AND expression_true','expression_false',3,'p_expression_false','boolean.py',86),
  ('expression_false -> expression_true AND expression_false','expression_false',3,'p_expression_false','boolean.py',87),
  ('expression_false -> expression_false AND expression_false','expression_false',3,'p_expression_false','boolean.py',88),
  ('expression_false -> expression_false OR expression_false','expression_false',3,'p_expression_false','boolean.py',89),
  ('expression_false -> LPAREN expression_false RPAREN','expression_false',3,'p_expression_false','boolean.py',90),
  ('expression -> ID','expression',1,'p_expression_id','boolean.py',95),
]
