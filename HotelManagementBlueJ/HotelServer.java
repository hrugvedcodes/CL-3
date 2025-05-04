import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class HotelServer {
    public static void main(String[] args) {
        try {
            HotelImpl obj = new HotelImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("HotelService", obj);
            System.out.println("Hotel server is running...");
        } catch (Exception e) {
            System.out.println("Server error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}