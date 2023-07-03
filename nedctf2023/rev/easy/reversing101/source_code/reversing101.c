#include <stdio.h>
#include <string.h>

void banner() {

    printf(R"EOF(    ____                           _                _______ ___
   / __ \___ _   _____  __________(_)___  ____ _   <  / __ <  /
  / /_/ / _ \ | / / _ \/ ___/ ___/ / __ \/ __ `/   / / / / / / 
 / _, _/  __/ |/ /  __/ /  (__  ) / / / / /_/ /   / / /_/ / /  
/_/ |_|\___/|___/\___/_/  /____/_/_/ /_/\__, /   /_/\____/_/   
                                       /____/                  
)EOF");

}

int main() {
    char str[] = "5tr0ng3stpa$$w0rd"; // the string to match against
    char input[100]; // the user input
    int arr[] = {
    0x4e,0x43,0x43,0x7b,0x34,0x6c,0x6c,0x5f,0x77,0x34,0x72,0x6d,0x33,0x64,0x5f,0x75,0x70,0x7d
  };
  int arr_len = sizeof(arr) / sizeof(arr[0]); // get the length of the array

    banner();
    printf("Enter the password: ");
    scanf("%s", input);

    if (strcmp(input, str) == 0) { // if the strings match
        printf("Correct!\nFlag: ");
        for (int i = 0; i < arr_len; i++) {
      int result = arr[i] ;
      printf("%c", (char) result); // cast the result to char and print it
    }
    } else { // if the strings do not match
        printf("Wrong!\n");
    }

    return 0;
}
