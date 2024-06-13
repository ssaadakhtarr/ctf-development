#include <stdio.h>
#include <string.h>

void level_three(char* flag, int length) {
    int start = 0;
    int end = length - 1;
    while (start < end) {
        char temp = flag[start];
        flag[start] = flag[end];
        flag[end] = temp;
        start++;
        end--;
    }
}

void level_two(char* flag, int length) {
    for (int i = 0; i < length; i++) {
        flag[i] ^= 0xAA;
        for (int j = 0; j < 8; j++) {
            if (flag[i] & (1 << j)) {
                flag[i] ^= (1 << (j + 1));
            }
        }
    }
}

void level_one(char* flag, int length) {
    for (int i = 0; i < length; i++) {
        flag[i] ^= (i + 1);
        flag[i] = ~flag[i] & 0xFF;
    }
}

void encrypt_flag() {
    printf("Welcome to the Super Cool C Encryptor!\n");
    printf("Enter the text to encrypt: ");
    char plain_text[100];
    fgets(plain_text, sizeof(plain_text), stdin);

    int length = strlen(plain_text);
    if (plain_text[length - 1] == '\n') {
        plain_text[length - 1] = '\0'; // Remove the newline character
        length--; // Adjust the length accordingly
    }

    char flag[100];
    strcpy(flag, plain_text);

    level_one(flag, length);
    level_two(flag, length);
    level_three(flag, length);

    printf("Encrypted Flag: %s\n", flag);

    printf("Hex Format: ");
    for (int i = 0; i < length; i++) {
        printf("%#04x ", (unsigned char)flag[i]);
    }
    printf("\n");
}

int main() {
    encrypt_flag();
    return 0;
}
