

import errno, sys
import random


k = random.randint(0, 1)

if k:
  pass    
else:
  sys.exit(errno.EACCES)
