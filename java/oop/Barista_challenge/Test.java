public class Test {
    public static void main(String[] args) {
        // Create 2 orders for unspecified guests (without specifying a name);
        Order order1 = new Order();
        Order order2 = new Order();
        // Create 3 orders using the overloaded constructor to give each a name for the
        // order.
        Order order3 = new Order("order3");
        Order order4 = new Order("order4");
        Order order5 = new Order("order5");
        // Add at least 2 items to each of the orders using the addItem method you
        // wrote, for example, to add item1 to order3 you would need to call the addItem
        // method from the order3 instance like so: order3.addItem(item1);
        Item item1 = new Item("mocha", 3.5);
        Item item2 = new Item("latte", 3.2);
        Item item3 = new Item("drip coffee", 2.8);
        Item item4 = new Item("capuccino", 3.8);
        order3.addItem(item1);
        order3.addItem(item2);
        order4.addItem(item2);
        order4.addItem(item3);
        order5.addItem(item3);
        order5.addItem(item4);
        // Test your getStatusMessage functionality by setting some orders to ready and
        // printing the messages for each order. For example: order2.setReady(true);
        // System.out.println(order2.getStatusMessage());
        order2.setReady(true);
        System.out.println(order2.getStatusMessage());
        // Test the total by printing the return value like so:
        System.out.println(order1.getOrderTotal());
        System.out.println(order3.getOrderTotal());
        // Finally, call the display method on all of your orders, like so:
        // order3.display();
        order3.display();
    }
}
