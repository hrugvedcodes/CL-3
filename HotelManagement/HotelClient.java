import java.rmi.Naming;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try {
            HotelInterface hotel = (HotelInterface) Naming.lookup("rmi://localhost/HotelService");
            Scanner sc = new Scanner(System.in);
            while (true) {
                System.out.println("\n1. Book Room\n2. Cancel Booking\n3. Exit");
                System.out.print("Choose: ");
                int choice = sc.nextInt();
                sc.nextLine(); // consume newline
                switch (choice) {
                    case 1:
                        System.out.print("Enter guest name: ");
                        String name = sc.nextLine();
                        System.out.println(hotel.bookRoom(name));
                        break;
                    case 2:
                        System.out.print("Enter guest name: ");
                        name = sc.nextLine();
                        System.out.println(hotel.cancelBooking(name));
                        break;
                    case 3:
                        System.exit(0);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
