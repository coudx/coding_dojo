import java.util.ArrayList;

public class TestPuzzleJava {

    public static void main(String[] args) {
        ArrayList<Integer> randomRolls = Puzzle.getTenRolls();
        System.out.println(randomRolls);

        ArrayList<String> randomPassword = Puzzle.getNewPasswordSet(5);
        System.out.println(randomPassword);
    }
}
