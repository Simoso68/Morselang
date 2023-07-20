def com(cstr: str):
    return """
public class Main {
    public static void main(String[] args) {
        System.out.println("VAL");
    }
}""".replace("VAL", cstr).replace("\n", "", 1)