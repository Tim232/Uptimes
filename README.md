
# Uptimes

A small python3 package for uptimes.

## How to Install :

Windows
```shell
python -m pip install -U uptimes
```

Linux
```shell
python3 -m pip3 install -U uptimes
```

## Usage :
```py
import uptimes
import time

time.sleep(10)
print(uptimes.uptimes())
print(uptimes.raw_uptimes())
```
## Output:
```
**0** days **0** hours **0** minutes **10** seconds
{"days":0,"hours":0,"minutes":0,"seconds":10}
```
