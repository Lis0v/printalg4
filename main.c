#include <stdio.h>
#include <stdlib.h>

int main(){

	int offset[]={4, -5, 2, -3,};
	int list_len;

	printf("Number of pages: ");
	scanf("%d", &list_len);
	
	char list[list_len+1];
	
	for(int i=0;i<list_len+1;i++){
	list[i]=i;
	printf("%d, ",list[i]);
	}


}
