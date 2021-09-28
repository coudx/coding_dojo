public class TestOrders {
    public static void main(String[] args) {

        // Menu items
        Item item1 = new Item();
        Item item2 = new Item();
        Item item3 = new Item();
        Item item4 = new Item();
        item1.name = "mocha";
        item1.price = 3.5;
        item2.name = "latte";
        item2.price = 3.2;
        item3.name = "drip coffee";
        item3.price = 2.8;
        item4.name = "capuccino";
        item4.price = 3.8;
        // Order variables -- order1, order2 etc.
        Order order1 = new Order();
        Order order2 = new Order();
        Order order3 = new Order();
        Order order4 = new Order();
        order1.name = "Cindhuri";
        order2.name = "Jimmy";
        order3.name = "Noah";
        order4.name = "Sam";
        // Application Simulations
        // Use this example code to test various orders' updates
        System.out.printf("Name: %s\n", order1.name);
        System.out.printf("Total: %s\n", order1.total); // predict print 0
        System.out.printf("Ready: %s\n", order1.ready);
        // Add item1 to order2's item list and increment the order's total.
        order2.addItem(item1);
        // order3 ordered a cappucino. Add the cappuccino to their order list and to
        // their tab.
        order3.addItem(item4);
        // order4 added a latte. Update accordingly.
        order4.addItem(item2);
        // Cindhuri’s order is now ready. Update her status.
        order1.ready = true;
        // Sam ordered more drinks - 2 lattes. Update their order as well.
        order4.addItem(item2);
        order4.addItem(item2);
        // Jimmy’s order is now ready. Update his status.
        order2.ready = true;
    }
}