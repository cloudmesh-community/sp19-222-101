#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
   static const char filename[] = "docker_containers.txt";
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
	    prevWord = malloc(strlen(word));
	    prevWord = strcpy(prevWord, word);

	    word = strtok(NULL, " ");
	    if(word == NULL)
	       break;
	    free(prevWord);
	 }
	 if(prevWord)
	 {
	    char command[128];
	    strcpy(command, "docker rm ");
	    strcat(command, prevWord);
		
	    system(command);

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


