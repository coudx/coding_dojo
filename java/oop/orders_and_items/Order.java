import java.util.ArrayList;

public class Order {
    public String name;
    public double total;
    public boolean ready;
    public ArrayList<Item> items = new ArrayList<Item>();

    public Order() {
        this.total = 0;
        this.ready = false;
    }

    public void addItem(Item item) {
        this.items.add(item);
        this.total += item.price;
    }
}
