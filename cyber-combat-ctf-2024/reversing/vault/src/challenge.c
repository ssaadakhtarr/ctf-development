#include <stdio.h>
#include <string.h>

// Secret function to obfuscate the flag
void obfuscate_flag(char* flag) {
    int i;
    for (i = 0; i < strlen(flag); i++) {
        flag[i] ^= 0x5A; // XOR operation with 0x5A
    }
}

int main() {
    char passcode[100];
    char flag[] = {0x3c,0x36,0x3b,0x3d,0x21,0x23,0x6a,0x2f,0x5,0x3d,0x6a,0x2e,0x5,0x37,0x69,0x5,0x3b,0x3d,0x6e,0x6b,0x34,0x34,0x34,0x7b,0x27}; // Obfuscated flag

    // Get passcode from the user
    printf("Enter the passcode to unlock the vault: ");
    fgets(passcode, sizeof(passcode), stdin);

    // Check if the passcode is correct
    if (strcmp(passcode, "SuperSecretPa$$w0rd_158271\n") == 0) {
        // Passcode is correct, print the flag
        obfuscate_flag(flag);
        printf("Congratulations! You've unlocked the vault.\n");
        printf("The flag is: %s\n", flag);
    } else {
        // Passcode is incorrect
        printf("Incorrect passcode. Access denied.\n");
    }

    return 0;
}
