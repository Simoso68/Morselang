def com(cstr: str):
    return """
#include <stdio.h>

int main() {
    printf("VAL");
    return 0;
}""".replace("VAL", cstr).replace("\n", "", 1)