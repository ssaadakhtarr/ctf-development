#include <stdio.h>
#include <string.h>

void banner() {

    printf(R"EOF(┏━┓   ┏┓ ╻╺┳╸   ┏┳┓┏━┓┏━┓┏━╸   ┏━╸╻ ╻┏━┓╻  ╻  ┏━╸┏┓╻┏━╸╻┏┓╻┏━╸   ╺┳╸╻ ╻╻┏━┓
┣━┫   ┣┻┓┃ ┃    ┃┃┃┃ ┃┣┳┛┣╸    ┃  ┣━┫┣━┫┃  ┃  ┣╸ ┃┗┫┃╺┓┃┃┗┫┃╺┓    ┃ ┣━┫┃┗━┓
╹ ╹   ┗━┛╹ ╹    ╹ ╹┗━┛╹┗╸┗━╸   ┗━╸╹ ╹╹ ╹┗━╸┗━╸┗━╸╹ ╹┗━┛╹╹ ╹┗━┛    ╹ ╹ ╹╹┗━┛
╺┳╸╻┏┳┓┏━╸┏━┓
 ┃ ┃┃┃┃┣╸  ╺┛
 ╹ ╹╹ ╹┗━╸ ╹)EOF");





}



void authenticator() {

    char user_input[50];
    char password[16];
    int secret = 4276215469;
    printf("\n\n\nEnter the username: ");
    gets(user_input);
    printf("\nHello %s!\n", &user_input);
    printf("\nPlease enter the secret password: ");
    fgets(password, sizeof(password), stdin); 

    if (secret == 0xcaf3bab3) {
        FILE* file = fopen("flag.txt", "r");
        if (file) {
            char buffer[256];
            printf("\nAccess Granted!\nHere's the flag: ");

            while (fgets(buffer, sizeof(buffer), file)) {
                printf("%s", buffer);
            }
            fclose(file);
        } else {
            printf("\nError: could not open file\n");
        }
    } else {
        printf("\nAccess Denied!");
    }

}

int main() {
    banner();   
    authenticator();

    return 0;
}
