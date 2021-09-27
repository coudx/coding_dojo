public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app.
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";

        // Menu variables (add yours below)
        double mochaPrice = 3.5;
        double coffeePrice = 3.0;
        double lattePrice = 3.5;
        double cappuccinoPrice = 3.8;

        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "Sam";
        String customer3 = "Jimmy";
        String customer4 = "Noah";

        // Order completions (add yours below)
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2 = false;
        boolean isReadyOrder3 = false;
        boolean isReadyOrder4 = false;

        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        System.out.println(generalGreeting + customer1); // Displays "Welcome to Cafe Java, Cindhuri"
    	// ** Your customer interaction print statements will go here ** //
        // Cindhuri ordered a coffee. Print to the console the correct status message, based on her order status.
        System.out.println(customer1+pendingMessage);
        System.out.println(customer1+readyMessage);
        // Noah ordered a cappuccino. Use an if statement to check the status of his order and print the correct status message. If it is ready, also print the message to display the total. Note: Outcomes may be different depending on what you assigned as the status.
        System.out.println(generalGreeting + customer4);
        System.out.println(customer4+pendingMessage);
        if(isReadyOrder4){
            System.out.println(customer4+readyMessage);
            System.out.println(displayTotalMessage+cappuccinoPrice);
        }
        // Sam just ordered 2 lattes, print the message to display their total first. Next print the appropriate order status message. Change the isReady flag value from true to false or vice versa in order to test your control logic (if-statements).
        System.out.println(generalGreeting+ customer2);
        System.out.println(displayTotalMessage+lattePrice*2);
        System.out.println(customer2+pendingMessage);
        if (isReadyOrder2){
            System.out.println(customer2+readyMessage);
        }
        isReadyOrder2=true;
        if (isReadyOrder2){
            System.out.println(customer2+readyMessage);
        }
        // Jimmy just realized he was charged for a coffee but had ordered a latte. Tell him his new total (what he owes) to make up the difference.
        System.out.println(generalGreeting+customer3);
        System.out.println(displayTotalMessage+(lattePrice-coffeePrice));
        // Try changing the price values for each drink and isReady flags (booleans), to test if all of your logic works, even when prices and statuses are changed.

    }
}
