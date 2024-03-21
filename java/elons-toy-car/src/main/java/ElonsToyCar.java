public class ElonsToyCar {
    private int distance = 0;
    private int battery = 100;
    public static ElonsToyCar buy() {
        // throw new UnsupportedOperationException("Please implement the (static) ElonsToyCar.buy()  method");
        return new ElonsToyCar();
    }

    public String distanceDisplay() {
        // throw new UnsupportedOperationException("Please implement the ElonsToyCar.distanceDisplay()  method");
        return String.format("Driven %d meters", distance);
    }

    public String batteryDisplay() {
        // throw new UnsupportedOperationException("Please implement the ElonsToyCar.batteryDisplay()  method");
        if (battery == 0) return "Battery empty";
        return String.format("Battery at %d%%", battery);
    }

    public void drive() {

        // throw new UnsupportedOperationException("Please implement the ElonsToyCar.drive()  method");
        if (battery == 0)return;
        distance+=20;
        battery-=1;
    }
}
