public class ExperimentalRemoteControlCar implements RemoteControlCar{
    private int distanceTravelled = 0;
    public void drive() {
        // throw new UnsupportedOperationException("Please implement the ExperimentalRemoteControlCar.drive() method");
        int speed = 20;
        distanceTravelled+= speed;
    }

    public int getDistanceTravelled() {
        // throw new UnsupportedOperationException("Please implement the ExperimentalRemoteControlCar.getDistanceTravelled() method");
        return distanceTravelled;
    }
}
