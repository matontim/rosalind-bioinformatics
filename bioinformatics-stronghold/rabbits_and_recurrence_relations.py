Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def rabbit_pairs(months):
...     if months <= 0: 
...         return 0
...     if months == 1 or months == 2: 
...         return 1
...         
...     prev_2 = 1
...     prev_1 = 1
...     current = 0
...     
...     for i in range(3, months + 1):
...         current = prev_1 + (2 * prev_2)
...         prev_2 = prev_1
...         prev_1 = current
...         
...     return current
... 
>>> print(rabbit_pairs(31))
715827883
