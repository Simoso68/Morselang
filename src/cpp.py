def com(cstr: str):
    return """
#include <iostream.h>

int main() {
    std::cout << "VAL";
    return 0;
}""".replace("VAL", cstr).replace("\n", "", 1)