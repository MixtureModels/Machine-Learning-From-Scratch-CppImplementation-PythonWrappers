#include <stdio.h>

int main()
{
    return 0;
}

// Linear algebra cpp-library functions being exported 
extern "C" int healthCheck() {
    printf (" << C++ functions successfully exported! \n");
    return 1;
}

// Hello world boilerplate helper for adding vectors in cpp
extern "C" void addVectors(double * vecOne, double * vecTwo) {
    int sz = 3;

    for (int i = 0;  i < sz; i++) {
        double computedVal = vecOne[i] + vecTwo[i];
        printf("computed: %.1f\n", computedVal);
    }
}





