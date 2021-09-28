import java.util.ArrayList;

// Here we're creating a new data type called Order
public class Order {

    // MEMBER VARIABLES
    private String name;
    private ArrayList<Item> items; // defaults to null

    // CONSTRUCTOR
    // No arguments, sets name to "Guest", initializes items as an empty list.
    public Order() {
        name = "Guest";
        items = new ArrayList<Item>();
    }

    public Order(String name) {
        setName(name);
        items = new ArrayList<Item>();
    }
    // ORDER METHODS

    // Implement the addItem method within the Order class
    public void addItem(Item item) {
        items.add(item);
    }

    // Implement the getOrderTotal method within the Order class
    public double getOrderTotal() {
        double total = 0;
        for (var i = 0; i < items.size(); i++) {
            total += items.get(i).getPrice();
        }
        return total;
    }

    public void display() {
        System.out.println(String.format("Cusomter Name: %s", getName()));
        for (var i = 0; i < items.size(); i++) {
            System.out.println(String.format("%s - $%.2f", items.get(i).getName(), items.get(i).getPrice()));
        }
        System.out.println(String.format("Total: $%.2f", getOrderTotal()));
    }

    // Most of your code will go here,
    // so implement the getters and setters first!

    // GETTERS & SETTERS
    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}