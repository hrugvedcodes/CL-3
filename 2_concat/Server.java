import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server {
    public static void main(String[] args) {
        try {
            // Change the port number from 1099 to 1098
            int port = 1098;
            // Create and start the RMI registry on the new port
            Registry registry = LocateRegistry.createRegistry(port); // Start RMI Registry on port 1098
            
            // Create the remote object
            ConcatImpl obj = new ConcatImpl();
            
            // Bind the object to the new RMI registry on the changed port
            registry.rebind("ConcatService", obj); // Register the remote object
            
            System.out.println("Server is ready...");
        } catch (Exception e) {
            System.out.println("Server Exception: " + e);
        }
    }
}

// Implementation of the Concat interface
class ConcatImpl extends UnicastRemoteObject implements Concat {
    protected ConcatImpl() throws RemoteException {
        super();
    }

    // Implementation of the remote method
    public String concatenate(String str1, String str2) throws RemoteException {
        return str1 + str2;
    }
}
