#include<stdio.h>
#include<stdlib.h>


int main(){
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    unsigned seed;
    seed = (unsigned)time(NULL);
    srand(seed);

    int num = 0;

    puts( "Give me the magic :)" );
    read( 0 , &num , 4 );
    if( num != 127174655 ){
        puts( "Bye!" );
        exit(0);
    }

    int times = 1000;

    puts( "Hacker can complete 1000 math problems in 60s, prove yourself." );

    while( times-- ){
        int a = random()%40000 , b = random()%40000;
        int c = random()%3 , ans;

        switch( c ){
            case 0:
                printf( "%d + %d = ?", a , b );
                scanf( "%d" , &ans );
                if( ans != a + b ){
                    puts( "Bye!" );
                    exit(0);
                }
                break;
            case 1:
                printf( "%d - %d = ?", a , b );
                scanf( "%d" , &ans );
                if( ans != a - b ){
                    puts( "Bye!" );
                    exit(0);
                }
                break;
            case 2:
                printf( "%d * %d = ?", a , b );
                scanf( "%d" , &ans );
                if( ans != a * b ){
                    puts( "Bye!" );
                    exit(0);
                }
                break;
        }
    }

    puts( "Welcome hacker!" );
    system( "sh" );

    return 0;
}