class NeedForSpeed {
    private final int speed;
    private final int batteryDrain;
    private int battery = 100;
    private int _distanceDriven = 0;

    NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
    }

    public boolean batteryDrained() {
        return battery == 0;
    }

    public int distanceDriven() {
        return _distanceDriven;
    }

    public void drive() {
        if(battery >= batteryDrain){
            battery = battery - batteryDrain;
            _distanceDriven += speed;
        }
    }

    /**
     * Best-selling car is the Nitro.
     * which has a stunning top speed of 50 meters
     * with a battery drain of 4%
     *
     * @return a car instance in NeedForSpeed has a top speed of 50 meters and drains 4% of its battery per use.
     */
    public static NeedForSpeed nitro() {
        // throw new UnsupportedOperationException("Please implement the (static) NeedForSpeed.nitro() method");
        return new NeedForSpeed(50, 4);
    }
    public double perUnitBatteryDrained() {
        // throw new UnsupportedOperationException("Please implement the NeedForSpeed.percentBatteryDrained() method");
        return (double)  batteryDrain / speed;
    }
}

class RaceTrack {
    int distance;
    RaceTrack(int distance) {
        this.distance = distance;
    }

    public boolean tryFinishTrack(NeedForSpeed car) {
        return car.perUnitBatteryDrained()*distance <= 100;
    }
}
