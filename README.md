
# Uptimes

A small python3 package for uptimes.

## How to Install :

```shell
pip install uptimes==0.1.0
```

## Usage :
```py
import uptimes.uptimes
import time

time.sleep(10)
print(uptimes.uptimes.uptimes())
print(uptimes.uptimes.raw_uptimes())
```
## Output:
```
**0** days **0** hours **0** minutes **10** seconds
{"days":0,"hours":0,"minutes":0,"seconds":10}
```
