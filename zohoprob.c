#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{
     char c[100]="ZzobZ999957589558";
     int i,j,k,l;
     char g;
     int count[100]={0};

    for(i=0;i<strlen(c);i++)
     {
        for(j=0;j<i;j++)
        {   
           if(i==j)
            {
              continue;
            }
           if( (c[i]== c[j]) || (c[i]==(c[j]+ 32)) || (c[i]==( c[j]- 32)))
            {
                count[i] = count[i]+ 1 ;
            }
        }
      }
    for(i=0;i<strlen(c);i++)
     {
         if(count[i] > 0)
            {
              if(c[i] == '9')
                {
                    g= '/';
                }
              else if(c[i] == 'Z' || c[i]== 'z')
                {
                    g = '`';
                }
             else
                {
                    g=c[i];
                }
               for(k=1;k<=count[i];k++)
                {
                    c[i] =  g + k;
                }
            }
        }
        for(i=0;i<strlen(c);i++)
        {
           printf("%c",c[i]);
        }
        getch();
        return 0;
}
