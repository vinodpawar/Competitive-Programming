//1.2wW6.2b34 
#include <stdio.h>
int
main ()
{
  int score[10];
  //char players[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b'};
  int p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11 = 0;
  int i = 0, extras = 0, strike = 1, nonstrike = 2, pcount = 2, ballCount = 0;

    printf("Enter score: ");
    scanf("%s", score);

  while (score[i] != '\0')
    {

      if (score[i] == '1' || '2' || '3' || '4' || '5' || '6')
	{

	  if (strike == 1)
	    {

	      p1 = p1 + score[i];
	    }

	  else if (strike == 2)
	    {

	      p2 = p2 + score[i];
	    }

	  else if (strike == 3)
	    {

	      p3 = p3 + score[i];
	    }

	  else if (strike == 4)
	    {

	      p4 = p4 + score[i];
	    }

	  else if (strike == 5)
	    {

	      p5 = p5 + score[i];
	    }

	 else if (strike == 6)
	    {

	      p6 = p6 + score[i];
	    }

	  else if (strike == 7)
	    {

	      p7 = p7 + score[i];
	    }

	  else if (strike == 8)
	    {

	      p8 = p8 + score[i];
	    }

	  else if (strike == 9)
	    {

	      p9 = p9 + score[i];
	    }

	  else if (strike == 10)
	    {

	      p10 = p10 + score[i];
	    }

	  else if (strike == 11)
	    {

	      p11 = p11 + score[i];
	    }
	}

      else if (score[i] == 'W')
	{

	  pcount = pcount + 1;
	  strike = pcount;
	}

      else if (score[i] == 'w' || 'b')
	{

	  extras = extras + 1;
	}

      else
	{


	}

      ballCount = ballCount + 1;

      if (ballCount == 6)
	{

	  int temp = strike;
	  strike = nonstrike;
	  nonstrike = temp;

	  ballCount = 0;
	}
	
	i++;

    }
  
  printf("p1: %d \np2: %d \np3: %d \np4: %d \np5: %d \np6: %d \np7: %d \np8: %d \np9: %d \np10: %d \np11: %d \nextra: %d", &p1, &p2, &p3, &p4, &p5, &p6, &p7, &p8, &p9, &p10, &p11, &extras);

  
}





    //printf("Enter the score: ");

    //scanf("%s",score);