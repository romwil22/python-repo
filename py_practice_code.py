def upperStr(*args):
    upperArgs = [u.upper() for u in args]
    upperArgs.sort()
    return upperArgs

print(upperStr("snow", "glacier", "iceberg"))