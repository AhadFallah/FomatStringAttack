#include <stdio.h>
int main(void) {
  char string[127];
  printf("Enter your string >> ");
  scanf("%127s", &string);
  printf(string);
}
