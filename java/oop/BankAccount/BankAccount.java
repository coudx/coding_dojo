import java.util.Random;

// Create a BankAccount class.
public class BankAccount {
    // The class should have the following attributes: (double) checking balance,
    // (double) savings balance.
    private double checkingBalance;
    private double savingBalance;
    private int accountNumber;

    // Create a class member (static) that has the number of accounts created thus
    // far.
    private static int member = 0;
    // Create a class member (static) that tracks the total amount of money stored
    // in every account created.
    private static double totalBalance = 0;

    // In the constructor, be sure to increment the account count.
    public BankAccount() {
        member++;
        accountNumber = genAccountNumber();
    }

    // getter & setter
    // Create a getter method for the user's checking account balance.
    public double getCheckBalance() {
        return checkingBalance;
    }

    // Create a getter method for the user's saving account balance.
    public double getSaveBalance() {
        return savingBalance;
    }

    public void setCheckBalance(double checkBalance) {
        this.checkBalance = checkBalance;
    }

    public void setSaveBalance(double saveBalance) {
        this.saveBalance = saveBalance;
    }

    // methods
    // Create a method that will allow a user to deposit money into either the
    // checking or saving, be sure to add to total amount stored.
    public void deposit(String account, double amount) {
        if (account.equals("saving")) {
            setSaveBalance(getSaveBalance() + amount);
        } else if (account.equals("checking")) {
            setCheckBalance(getCheckBalance() + amount);
        } else {
            System.out.println("Account does not exist, use checking or saving");
        }
        totalBalance += amount;
    }

    public void withdraw(String account, double amount) {
        if (account.equals("saving")) {
            if (getSaveBalance() < amount) {
                System.out.println("Insufficient funds");
            } else {
                setSaveBalance(getSaveBalance() - amount);
            }
        } else if (account.equals("checking")) {
            if (getCheckBalance() < amount) {
                System.out.println("Insufficient funds");
            } else {
                setCheckBalance(getCheckBalance() - amount);
            }
        } else {
            System.out.println("Account does not exist, use checking or saving");
        }
        totalBalance -= amount;
    }

    // Create a method to see the total money from the checking and saving.
    public double getTotalBalance() {
        return getCheckBalance() + getSaveBalance();
    }

    public int genAccountNumber() {
        String num = "";
        for (var i = 0; i < 10; i++) {
            num += new Random.nextInt(10);
        }
        return num;
    }
}
