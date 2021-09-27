import java.util.Random;
import java.util.ArrayList;

public class Puzzle {
    public static ArrayList<Integer> getTenRolls() {
        ArrayList<Integer> x = new ArrayList<Integer>();
        Random rand = new Random();
        for (int i = 0; i < 10; i++) {
            x.add(rand.nextInt(20) + 1);
        }
        return x;
    }

    public static char getRandomLetter() {
        Random rand = new Random();
        char[] lib = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z' };
        return lib[rand.nextInt(25)];
    }

    public static String generatePassword() {
        String pw = "";
        for (int i = 0; i < 8; i++) {
            pw += String.valueOf(getRandomLetter());
        }
        return pw;
    }

    public static ArrayList<String> getNewPasswordSet(int n) {
        ArrayList<String> x = new ArrayList<String>();
        for (int i = 0; i < n; i++) {
            x.add(generatePassword());
        }
        return x;
    }
}
