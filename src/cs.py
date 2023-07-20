def com(cstr: str):
    return """
namespace Program {
    class Main {
        static void Main(string[] args) {
            System.Console.WriteLine("VAL")
        }
    }
}""".replace("VAL", cstr).replace("\n", "", 1)