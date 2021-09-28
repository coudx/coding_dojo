import java.util.ArrayList;

public class CoffeeKiosk {
    private ArrayList<Item> menu;
    private ArrayList<Order> orders;

    public CoffeeKiosk() {
        menu = new ArrayList<Item>();
        orders = new ArrayList<Order>();
    }

    public void addMenuItemByInput(String name, double price) {
        menu.add(new Item(name, price));
    }

    public void addMenuItem() {
        menu.add(new Item("banana", 2));
        menu.add(new Item("coffee", 1.5));
        menu.add(new Item("lattee", 4.5));
        menu.add(new Item("capuccino", 3));
        menu.add(new Item("muffin", 4));
    }

    public void displayMenu() {
        for (int i = 0; i < menu.size(); i++) {
            System.out.println(String.format("%d %s - $%.2f", i, menu.get(i).getName(), menu.get(i).getPrice()));
        }
    }

    public void newOrder() {

        // Shows the user a message prompt and then sets their input to a variable, name
        System.out.println("Please enter customer name for new order:");
        String orderName = System.console().readLine();
        Order newOrder = new Order(orderName);
        // Your code:
        // Create a new order with the given input string
        // Show the user the menu, so they can choose items to add.
        displayMenu();
        // Prompts the user to enter an item number
        System.out.println("Please enter a menu item index or q to quit:");
        String itemNumber = System.console().readLine();

        // Write a while loop to collect all user's order items
        while (!itemNumber.equals("q")) {
            int number = Integer.parseInt(itemNumber);
            // Get the item object from the menu, and add the item to the order
            // Ask them to enter a new item index or q again, and take their input
            if (number < menu.size()) {
                newOrder.addItem(menu.get(number));
            } else {
                System.out.println("Item number does not exist");
            }
            displayMenu();
            System.out.println("Please enter a menu item index or q to quit:");
            itemNumber = System.console().readLine();

        }

        // After you have collected their order, print the order details
        // as the example below. You may use the order's display method.
        newOrder.display();
        orders.add(newOrder);
    }

}
