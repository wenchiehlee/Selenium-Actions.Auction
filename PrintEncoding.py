#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import locale

print('locale.getpreferredencoding():\t{}'.format(
  locale.getpreferredencoding())
)
print('sys.getfilesystemencoding():\t{}'.format(
  sys.getfilesystemencoding())
)
print('sys.getdefaultencoding():\t{}'.format(
  sys.getdefaultencoding())
)
print('sys.stduot.encoding:\t\t{}'.format(
  sys.stdout.encoding)
)