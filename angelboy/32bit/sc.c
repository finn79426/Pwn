/*
 * sc.c
 * Copyright (C) 2018 howpwn <finn79426@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char name[50];


int main(){
	setvbuf(stdout,0,2,0);
	printf("Name:");
	gets(name);
	char buf[30];
	printf("Try your best:");
	gets(buf);
	return ;	
}

