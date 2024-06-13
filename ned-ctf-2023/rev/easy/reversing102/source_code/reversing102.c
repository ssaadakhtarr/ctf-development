#include <stdio.h>
#include <string.h>

void banner() {

    printf(R"EOF(    ____                           _                _______ ___ 
   / __ \___ _   _____  __________(_)___  ____ _   <  / __ \__ \
  / /_/ / _ \ | / / _ \/ ___/ ___/ / __ \/ __ `/   / / / / /_/ /
 / _, _/  __/ |/ /  __/ /  (__  ) / / / / /_/ /   / / /_/ / __/ 
/_/ |_|\___/|___/\___/_/  /____/_/_/ /_/\__, /   /_/\____/____/ 
                                       /____/                   
)EOF");

}

int main() {

  char input[100]; // the user input
  int arr[] = {
    0x1379,
    0x1374,
    0x1374,
    0x134c,
    0x1306,
    0x1343,
    0x1344,
    0x1368,
    0x1307,
    0x1359,
    0x135b,
    0x134e,
    0x1368,
    0x1343,
    0x135f,
    0x1304,
    0x1368,
    0x1355,
    0x1304,
    0x1350,
    0x135e,
    0x1359,
    0x1359,
    0x135e,
    0x1359,
    0x1350,
    0x134a
  };
  int arr_len = sizeof(arr) / sizeof(arr[0]); // get the length of the array

  int secret[] = {
    0xdede,
    0xded8,
    0xdedd,
    0xde9e,
    0xdedf,
    0xdede,
    0xde9e,
    0xdece,
    0xdedf,
    0xde9e,
    0xded9
  };
  int secret_len = sizeof(secret) / sizeof(secret[0]);
  for (int i = 0; i < secret_len; i++) {
    secret[i] ^= 0xdead; // apply XOR operation
  }

  banner();
  printf("Enter the secret key: ");
  scanf("%s", input);

  if (strlen(input) != 11) {
    printf("Access Denied! You're not allowed in here.");
  } else {

    for (int i = 0; i < 11; i++) {

      if (input[i] != secret[i]) {
        printf("Access Denied! You're not allowed in here.");
      }
    }

    printf("Access Granted! Here's your token.");
    printf("\nFlag: ");

    for (int i = 0; i < arr_len; i++) {
      int result = arr[i] ^ 0x1337; // apply XOR operation
      printf("%c", (char) result); // cast the result to char and print it
    }

  }

  return 0;
}