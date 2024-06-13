#include <stdio.h>
#include <string.h>

void xor_encrypt(char *flag, char *key, char *result) {
    int flag_len = strlen(flag);
    int key_len = strlen(key);
    for (int i = 0; i < flag_len; i++) {
        result[i] = flag[i] ^ key[i % key_len];
    }
    result[flag_len] = '\0';
}

int main() {
    char flag[100];
    char key[] = "e|/O8B=r)8V.8G3";
    char result[100];

    printf("Enter the value to encrypt: ");
    fgets(flag, sizeof(flag), stdin);
    flag[strcspn(flag, "\n")] = '\0';  // Remove the newline character

    xor_encrypt(flag, key, result);

    printf("Encrypted Result: ");
    for (int i = 0; result[i] != '\0'; i++) {
        printf("%02x ", (unsigned char)result[i]);
    }
    printf("\n");

    return 0;
}


// To build, I used 
// gcc challenge.c -o pulse
// Then,
// upx pulse -o pulse-upx