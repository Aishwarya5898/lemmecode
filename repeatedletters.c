#include<stdio.h>
#include<string.h>
#include<conio.h>
char *remdup(char str[]);
char *remdup(char str[] )
{
     int count[256];
     char blank[100];
      int i,c;
      c=0;
     for(i=0; str[i] != '\0' ;i++)
     {
                     count[str[i]] = 0;
                     }
                    for(i=0; str[i] != '\0' ;i++)
                     {
                                     count[str[i]] = count[str[i]] + 1;
                                     }
                                    for(i=0; str[i] != '\0' ;i++)
                     {
                              printf("%d ",count[str[i]]);
                                     }
                                      for(i=0; str[i] != '\0' ;i++)
                                     {
                                                     if(count[str[i]] == 1)
                                                     {
                                                         blank[c] = str[i];
                                                         c++;
                                                     }
                                                     if(count[str[i]]> 1)
                                                     {
                                                         count[str[i]] = 0;
                                                         blank[c] = str[i];
                                                         c++;
                                                         }

                                     }
                                                         blank[c] = '\0';
                                                         return blank;
                                                         }



int main()
{
     char str[] = "Aiihshhrwarya";
     printf("%s", remdup(str));
     getch();
     return 0;
     }

