import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;

public class HotelImpl extends UnicastRemoteObject implements Hotel {
    private List<String> bookings;

    protected HotelImpl() throws RemoteException {
        bookings = new ArrayList<>();
    }

    public synchronized String bookRoom(String guestName) {
        bookings.add(guestName);
        return "Room booked for " + guestName;
    }

    public synchronized String cancelBooking(String guestName) {
        if (bookings.remove(guestName)) {
            return "Booking cancelled for " + guestName;
        } else {
            return "No booking found for " + guestName;
        }
    }

    public synchronized String getBookings() {
        return "Current bookings: " + bookings.toString();
    }
}