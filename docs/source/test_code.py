"""
test_code - Python library for testing code.
"""

__version__ = "0.1.0"


class Module():
  '''
  Strip Module Class - all the fixin's
  '''

  def __init__(self, module_sn):
    '''
    Module Initialization

    :param module_sn: Module Serial Number
    :type module_sn: str
    '''

    Module.sn          = module_sn
    Module.type        = None
    Module.FMC_channel = None

  def SetModuleType(self, module_sn):
    '''
    Set Module Type

    :param module_sn: Module Serial Number
    :type module_sn: str
    :return: The module type
    :rtype: str
    '''

    return 'R1'

if __name__ == "__main__":
  
  module = Module('20USEM10000042')
  print(module.sn)
  module.type = module.SetModuleType(module.sn)
  print(module.type)
