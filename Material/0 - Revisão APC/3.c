#include <stdio.h>

int main(void) {
  int dia1,dia2,h1,h2,m1,m2,s1,s2;
  int total;
  scanf("%d %d:%d:%d", &dia1,&h1,&m1,&s1);
  scanf("%d %d:%d:%d", &dia2,&h2,&m2,&s2);
  total=(dia2-dia1)*86400+(h2-h1)*3600+(m2-m1)*60+(s2-s1);
  if(total<0){
    printf("Data invalida!\n");
  }else{
    printf("%d dia(s)\n", total/86400);
    total=total%86400;
    printf("%d hora(s)\n", total/3600);
    total=total%3600;
    printf("%d minuto(s)\n", total/60);
    total=total%60;
    printf("%d segundo(s)\n", total);
  }
  
  return 0;
}