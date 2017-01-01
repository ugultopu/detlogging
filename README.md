# detlogging
Log details of an object.

## Usage
1. Download the module `detlogging.py`
2. Import `detlog` using `from .detlogging import detlog`
3. Log with `detlog(some_object)`

The attributes of `some_object` are logged to `stderr`.

## TODO
1. Uses the root logger. This probably should be changed.

## Notes
1. Since we use the root logger, and since we created a custom LogRecord attribute named `omsg`, errors about the `omsg` might occasionally be seen in the log messages which are created by the root logger, but without using our custom logger. This is expected. To fix this, root logger should not be used.
