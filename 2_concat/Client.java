import java.rmi.Naming;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try {
           
            Concat stub = (Concat) Naming.lookup("rmi://localhost:1098/ConcatService");

            Scanner sc = new Scanner(System.in);
            System.out.print("Enter first string: ");
            String s1 = sc.nextLine();
            System.out.print("Enter second string: ");
            String s2 = sc.nextLine();

            String result = stub.concatenate(s1, s2);
            System.out.println("Concatenated Result: " + result);
        } catch (Exception e) {
            System.out.println("Client Exception: " + e);
        }
    }
}
