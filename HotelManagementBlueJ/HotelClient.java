import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class HotelClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            Hotel stub = (Hotel) registry.lookup("HotelService");

            System.out.println(stub.bookRoom("Alice"));
            System.out.println(stub.bookRoom("Bob"));
            System.out.println(stub.getBookings());
            System.out.println(stub.cancelBooking("Alice"));
            System.out.println(stub.getBookings());

        } catch (Exception e) {
            System.out.println("Client error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}