#include <stdio.h>

// Hello world boilerplate helper for adding vectors in cpp
extern "C" void speedTestHelper(double * vecOne, double * vecTwo, int iterations, int sz) {
    for (int i = 0; i < iterations; i++) { 
        for (int j = 0;  j < sz; j++) {
            double computedVal = vecOne[j] + vecTwo[j];
        }
    }
}

// Hello world boilerplate helper for adding vectors in cpp
extern "C" void addVectors(double * vecOne, double * vecTwo, int sz) {
    for (int i = 0;  i < sz; i++) {
        double computedVal = vecOne[i] + vecTwo[i];
        printf("computed: %.1f\n", computedVal);
    }
}

int main()
{
    return 0;
}




