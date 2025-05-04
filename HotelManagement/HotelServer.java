import java.rmi.Naming;

public class HotelServer {
    public static void main(String[] args) {
        try {
            // LocateRegistry.createRegistry(1099); // Start RMI registry
            HotelInterface hotel = new HotelImplementation();
            Naming.rebind("HotelService", hotel);
            System.out.println("Hotel Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
