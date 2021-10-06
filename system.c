#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(){

	int p = fork();
	if(p>0){
		fork();
		printf("Piyumal");
	}
	
	printf("piyumal");
	
	return 0;
}
