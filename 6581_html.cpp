#include <iostream>
#include <string.h>
using namespace std;

int line=0;

void hr(){
    if( line!=0 ) printf("\n");
    for(int i=0; i<80; i++) printf("-");
    printf("\n");
    line = 0;
}


int main(void){

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

string in2;
    while( cin>>in2 ){
        if( in2=="<br>"){
            cout<<'\n';
            line = 0;
        }else if( in2=="<hr>"){
            hr();
        }else{
            if( line+in2.length()+1>80 ){
                cout<<'\n';
                line = 0;
            }
            if( line!=0 ){
                cout<<" ";
                line++;
            }
            cout<<in2;
            line += in2.length();
        }
    }
    return 0;
}

