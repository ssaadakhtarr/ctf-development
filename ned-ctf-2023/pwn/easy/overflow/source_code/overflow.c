#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void banner() {

    printf(R"EOF(╻ ╻┏━╸╻  ┏━╸┏━┓┏┳┓┏━╸   ╺┳╸┏━┓   ╺┳╸╻ ╻┏━╸   ┏━┓╻ ╻┏┓╻   ╻ ╻┏━┓┏━┓╻  ╺┳┓
┃╻┃┣╸ ┃  ┃  ┃ ┃┃┃┃┣╸     ┃ ┃ ┃    ┃ ┣━┫┣╸    ┣━┛┃╻┃┃┗┫   ┃╻┃┃ ┃┣┳┛┃   ┃┃
┗┻┛┗━╸┗━╸┗━╸┗━┛╹ ╹┗━╸    ╹ ┗━┛    ╹ ╹ ╹┗━╸   ╹  ┗┻┛╹ ╹   ┗┻┛┗━┛╹┗╸┗━╸╺┻┛
)EOF");

}

void win() {

    FILE *fp;
    char ch;
    fp = fopen("flag.txt", "r");
    if (fp == NULL) {
        printf("Error: could not open file.\n");
        return;
    }
    printf("\nHere's your flag: ");
    while ((ch = fgetc(fp)) != EOF) {
        printf("%c", ch);
    }
    fclose(fp);
    
}

void segv_handler(int signal) {
    printf("Segmentation fault detected\n");
    win();
    exit(1);
}

void overflow_handler() {
    printf("Buffer overflow detected!\n");
    win();
    exit(0);
}

int main() {

setvbuf(stdout, NULL, _IONBF, 0);  // Disable output buffering
    setvbuf(stdin, NULL, _IONBF, 0);   // Disable input buffering
      fflush(stdout);
    char buffer[20];
    struct sigaction segv_act, overflow_act;

    segv_act.sa_handler = segv_handler;
    segv_act.sa_flags = SA_RESETHAND;
    sigaction(SIGSEGV, &segv_act, NULL);

    overflow_act.sa_handler = overflow_handler;
    overflow_act.sa_flags = SA_RESTART;
    sigaction(SIGABRT, &overflow_act, NULL);
    
    banner();
    printf("\n\nEnter your name: ");
    gets(buffer);
    printf("Hello, %s\n", buffer);

    return 0;
}
