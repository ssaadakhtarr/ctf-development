#include <stdio.h>
#define BUFFER_SIZE 256

void print_flag() {
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

void banner() {

    printf(R"EOF(╻  ┏━╸╻ ╻┏━╸╻  ╻┏┓╻┏━╸   ╻ ╻┏━┓   ┏━┓   ╻  ╻╺┳╸╺┳╸╻  ┏━╸╻
┃  ┣╸ ┃┏┛┣╸ ┃  ┃┃┗┫┃╺┓   ┃ ┃┣━┛   ┣━┫   ┃  ┃ ┃  ┃ ┃  ┣╸ ╹
┗━╸┗━╸┗┛ ┗━╸┗━╸╹╹ ╹┗━┛   ┗━┛╹     ╹ ╹   ┗━╸╹ ╹  ╹ ┗━╸┗━╸╹)EOF");
printf("\n\n\n\n");

printf(R"EOF(┏━╸┏━┓┏┓╻   ╻ ╻┏━┓╻ ╻   ┏━┓┏━┓╻  ╻ ╻┏━╸   ╺┳╸╻ ╻╻┏━┓   ┏━┓┏┓╻┏━╸┏━┓
┃  ┣━┫┃┗┫   ┗┳┛┃ ┃┃ ┃   ┗━┓┃ ┃┃  ┃┏┛┣╸     ┃ ┣━┫┃┗━┓   ┃ ┃┃┗┫┣╸  ╺┛
┗━╸╹ ╹╹ ╹    ╹ ┗━┛┗━┛   ┗━┛┗━┛┗━╸┗┛ ┗━╸    ╹ ╹ ╹╹┗━┛   ┗━┛╹ ╹┗━╸ ╹)EOF");

}

int main() {
    
    char buffer[BUFFER_SIZE];

    banner();

    printf("\n\n\nMay I ask what your name is? ");

    gets(buffer);

    printf("Good luck %s!\n", buffer);

    return 0;
}
