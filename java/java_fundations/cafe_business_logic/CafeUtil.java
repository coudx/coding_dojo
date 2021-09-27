import java.util.ArrayList;

public class CafeUtil {
    public int getStreakGoal() {
        return (1 + 10) * 5;
    }

    public void printPriceChart(String name, double price, int number) {
        System.out.println(name);
        for (int i = 1; i <= number; i++) {
            double newprice = price * i;
            System.out.println(String.format("%d - $%.2f", i, newprice));
        }
    }

    public double getOrderTotal(double[] price) {
        double sum = 0;
        for (int i = 0; i < price.length; i++) {
            sum += price[i];
        }
        return sum;
    }

    public void displayMenu(ArrayList<String> name, ArrayList<Double> price) {
        for (int i = 0; i < name.size(); i++) {
            System.out.println(String.format("%d %s -- $%.2f", i, name.get(i), price.get(i)));
        }
    }

    public void addCustomer(ArrayList<String> name) {
        String userName = System.console().readLine();
        if (!userName.equals("q")) {
            name.add(userName);
            addCustomer(name);
        }
    }
}
