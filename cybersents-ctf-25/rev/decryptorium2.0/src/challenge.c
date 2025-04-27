#include <stdio.h>
#include <string.h>
#include <stdint.h>

void level_one(char* flag, int len) {
    for (int i = 0; i < len; i++) {
        flag[i] = ((flag[i] << 2) | (flag[i] >> 6)) ^ 0x3C; // left rotate 2 bits then XOR
    }
}

void level_two(char* flag, int len) {
    for (int i = 0; i < len; i++) {
        flag[i] = ~(flag[i] ^ i) + 1; // two's complement after XOR with index
    }
}

void level_three(char* flag, int len) {
    for (int i = 0; i < len; i += 2) {
        if (i + 1 < len) {
            char tmp = flag[i];
            flag[i] = flag[i + 1];
            flag[i + 1] = tmp;
        }
    }
}

uint8_t checksum(char* flag, int len) {
    uint8_t sum = 0;
    for (int i = 0; i < len; i++) {
        sum ^= (flag[i] + i);
    }
    return sum;
}

void encrypt_flag() {
    printf("Welcome to Super Cool C Encryptor 2.0 aka Decryptorium 2.0\n");
    printf("Enter the text to encrypt: ");
    char input[100];
    fgets(input, sizeof(input), stdin);

    int len = strlen(input);
    if (input[len - 1] == '\n') {
        input[len - 1] = '\0';
        len--;
    }

    char flag[100];
    strcpy(flag, input);

    level_one(flag, len);
    level_two(flag, len);
    level_three(flag, len);

    printf("Encrypted Flag: ");
    for (int i = 0; i < len; i++) {
        printf("%c", flag[i]);
    }
    printf("\n");

    printf("Hex Dump: ");
    for (int i = 0; i < len; i++) {
        printf("%#04x ", (unsigned char)flag[i]);
    }
    printf("\n");

    printf("Final Checksum: %#04x\n", checksum(flag, len));
}

int main() {
    encrypt_flag();
    return 0;
}
