import java.util.Scanner; 

public class BubbleSort {
    public static void main(String[] args) {

        boolean swap = false;
        for (int i = 0; i < args.length; i++) {
            for (int j = i + 1; j < args.length; j++) {
                if ( Integer. parseInt(args[i]) >  Integer. parseInt(args[j])) {
                    String tmp = args[i];
                    args[i] = args[j];
                    args[j] = tmp;
                    swap = true;
                }
            }
            if (swap != true) {
                break;
            }
        }

        for (String i: args) {
            System.out.println(i);
        }
    }
}
