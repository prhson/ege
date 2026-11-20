from itertools import *

for val in product('фокус', repeat=5):
    val = ''.join(val)

for pos, val in enumerate(product('фокус', repeat=5)):
    print(val)
    wal=''.join(val)
# Формирует все возможные комбинации с повторениями
