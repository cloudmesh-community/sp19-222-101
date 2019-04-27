#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
   static const char filename[] = "dockerContainers.txt";
   FILE *file = fopen(filename, "r");
   if(file != NULL)
   {
      char line[128] = {0};
      int index = 1;
      
      while(fgets(line, sizeof line, file) != NULL)
      {
	 char* word;
	 char* prevWord;
	 if(index%2 != 0)
	 {
	    index++;
	    continue;
	 }
	 
	 word = strtok(line, " ");
	 
	 while(word != NULL)
	 {
	    printf("%s\n", word);

	    prevWord = malloc(strlen(word));
	    prevWord = strcpy(prevWord, word);

	    word = strtok(NULL, " ");
	    if(word == NULL)
	       break;
	    free(prevWord);
	 }
	 if(prevWord)
	 {
	   printf("Last word is: %s\n", prevWord);
	   free(prevWord);
	 }
	 if(word)
	    free(word);
	 
	 index++;	 
      } /* While */
   }
	
   fclose(file);

   return 0;
}


