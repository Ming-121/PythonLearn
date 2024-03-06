# import导入
import support

support.log('import导入')
support.log1('import导入')

# from...import导入
from support import log, log1

log('from...import导入')
log1('from...import导入')

# from...import* 导入
from support import*

log('from...import* 导入')
log1('from...import* 导入')

print(dir(support))
