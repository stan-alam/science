
<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%201.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%202.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%203.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%204.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%205.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%206.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%208.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%209.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2010.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2011.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2012.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2013.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2014.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2015.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2016.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2017.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2018.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2019.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2020.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2021.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2022.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2023.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2024.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2025.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2026.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2027.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2028.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2029.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2030.png" width="80%" height="80%">
</a>

<a>
  <img src="https://github.com/stan-alam/science/blob/develop/CS/Pthreads/images/01/pThreads%20-%20page%2031.png" width="80%" height="80%">
</a>

```c
#include <stdio.h>
#include <pthread.h>

void do_one_thing(int *);
void do_another_thing(int *);
void do_wrapup(int, int);

int r1 = 0;
int r2 = 0;

extern int

main(void)
{
  pthread_t thread01;
  pthread_t thread02;

  pthread_create(r&thread1, NULL, (void *) do_another_thing,
  (void *) &r1);
  pthread_create(& thread02, NULL, (void *)do_another_thing, (void *) &r2);

  pthread_join(thread01, NULL);
  pthread_join(thread02, NULL);
    do_wrapup(r1, r2,);

  return 0
} 
```