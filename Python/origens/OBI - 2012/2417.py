import sys

cv, ce, cs, fv, fe, fs = map(int, sys.stdin.readline().split())

cp = cv * 3 + ce
fp = fv * 3 + fe

if (cp == fp and cs > fs) or cp > fp:
    sys.stdout.write("C\n")
elif (cp == fp and fs > cs) or cp < fp:
    sys.stdout.write("F\n")
else:
    sys.stdout.write("=\n")