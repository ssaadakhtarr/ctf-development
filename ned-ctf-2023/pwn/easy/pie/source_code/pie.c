#include <stdio.h>

void banner() {

    printf(R"EOF(╺┳╸╻ ╻┏━╸   ╻  ┏━┓┏━┓╺┳╸   ┏━┓┏┓╻┏━╸
 ┃ ┣━┫┣╸    ┃  ┣━┫┗━┓ ┃    ┃ ┃┃┗┫┣╸ 
 ╹ ╹ ╹┗━╸   ┗━╸╹ ╹┗━┛ ╹    ┗━┛╹ ╹┗━╸)EOF");
 printf("\n\n");

}

void win() {
    FILE *fp;
    char ch;
    fp = fopen("flag.txt", "r");
    if (fp == NULL) {
        printf("Error: could not open file.\n");
        return;
    }
    printf("Contents of flag.txt:\n");
    while ((ch = fgetc(fp)) != EOF) {
        printf("%c", ch);
    }
    fclose(fp);
}



int main() {

    banner();
    vuln();

    return 0;
}

void vuln() {
    char buffer[20];

    printf("Leaked address: %p\n", main);
    printf("For the last time could you tell me your name please? ");
    gets(buffer);
    printf("\nThank you %s", buffer);
    // printf(buffer);
}




