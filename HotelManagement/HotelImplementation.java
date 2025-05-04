import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashSet;
import java.util.Set;

public class HotelImplementation extends UnicastRemoteObject implements HotelInterface {
    private Set<String> bookedGuests;

    protected HotelImplementation() throws RemoteException {
        bookedGuests = new HashSet<>();
    }

    public synchronized String bookRoom(String guestName) throws RemoteException {
        if (bookedGuests.contains(guestName)) {
            return "Room already booked for " + guestName;
        }
        bookedGuests.add(guestName);
        return "Room booked successfully for " + guestName;
    }

    public synchronized String cancelBooking(String guestName) throws RemoteException {
        if (bookedGuests.remove(guestName)) {
            return "Booking cancelled for " + guestName;
        }
        return "No booking found for " + guestName;
    }
}
