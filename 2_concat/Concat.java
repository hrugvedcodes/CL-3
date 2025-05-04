import java.rmi.*;

public interface Concat extends Remote {
    String concatenate(String str1, String str2) throws RemoteException;
}
