def com(cstr: str):
    return """
fun main() {
    println("VAL");
}""".replace("VAL", cstr).replace("\n", "", 1)