#include <stdlib.h>
#include <stdio.h>
#include <time.h> 

int testForPrime(long p)  //slow prime test 
{ long i=0;
  for(i=2; i<p; i++) {
      if ((p%i)==0) return 0;
   }
  return 1;
}

int main(int argc, char **argv)
{ long i=0;
  int gPrimesFound=0;
  double inicio = 0, fin = 0;
  int start = atoi(argv[1]), end = atoi(argv[2]);
  clock_t start_clocks, end_clocks;

start_clocks = (double) clock();
#pragma omp parallel for 
  for (i = start; i <= end; i++)
     { if (testForPrime(i))
          gPrimesFound++;
     }
end_clocks = (double) clock();

   printf("number of primes between %d and %d: %d\n",start,end,gPrimesFound);
   printf("number of seconds passed %lf seconds\n",(end_clocks/CLOCKS_PER_SEC));
}