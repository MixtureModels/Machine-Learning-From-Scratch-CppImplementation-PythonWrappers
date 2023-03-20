#!/bin/bash

rm Shared/linalg.so
gcc -fPIC -shared -o linalg.so linalg.cc
mv linalg.so Shared

echo "Linear Algebra library compiled"
