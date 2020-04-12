#include <stdio.h>
#include <math.h>
int main(void) {
  int buraco, i;
  float xc, yc, xr, yr, xb, yb;
  float bc, br, t1, t2;
  scanf("%d %f %f %f %f", &buraco, &xc, &yc, &xr, &yr);
  for(i=0;i<buraco;i++){
    scanf("%f %f", &xb, &yb);
    bc=sqrt((xc-xb)*(xc-xb)+(yc-yb)*(yc-yb));
    br=sqrt((xr-xb)*(xr-xb)+(yr-yb)*(yr-yb));
    t1=bc/1;
    t2=br/2;
    //printf("%f\n%f\n",t1,t2);
    if(t2>t1){
      printf("O coelho pode escapar pelo buraco (%.3f,%.3f).", xb,yb);
      goto final;
    }
  }
  printf("O coelho nao pode escapar.");
  final:
  return 0;
}