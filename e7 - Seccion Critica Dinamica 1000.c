#include <stdlib.h>
#include <stdio.h>
#include <omp.h>
#include <math.h>
 
int *ThreadCalculus;

int testForPrime(long p)  //slow prime test 
{ long i=0;
  int n = sqrt(p)+1;
  for(i=2; i<=n; i++) {
      if ((p%i)==0) return 0;
   }
  return 1;
}

int main(int argc, char **argv)
{ long i=0;
  int gPrimesFound=0;
  double inicio = 0, fin = 0;
  long start = 0, end = 0;
  int n;

start = atoi(argv[1]); 
end = atoi(argv[2]);
omp_set_num_threads(atoi(argv[3]));
n = omp_get_max_threads();
ThreadCalculus = (int*)malloc (sizeof (int) * n);
for (int i = 0; i < omp_get_max_threads(); i++)
{
  ThreadCalculus[i] = 0;
}

inicio = omp_get_wtime();
#pragma omp parallel for schedule (dynamic, 1000)
  for (i = start; i <= end; i++)
     { if (testForPrime(i))
        #pragma omp critical
        {
          gPrimesFound++;
          ThreadCalculus[(int) omp_get_thread_num()]++;
        }
     }
fin = omp_get_wtime();

  printf("number of primes between %d and %d: %d\n",start,end,gPrimesFound);
  printf("number of seconds passed %lf seconds\n",fin - inicio);
  for (int i = 0; i < omp_get_max_threads(); i++)
  {
    printf("%d\n", ThreadCalculus[i]);
  }

}