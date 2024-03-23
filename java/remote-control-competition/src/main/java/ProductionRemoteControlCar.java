 public class ProductionRemoteControlCar implements RemoteControlCar, Comparable<ProductionRemoteControlCar>{

    private int distanceTravelled = 0;
    private int numberOfVictories = 0;
    public void drive() {
        // throw new UnsupportedOperationException("Please implement the ProductionRemoteControlCar.drive() method");
        int speed = 10;
        distanceTravelled += speed;
    }

    public int getDistanceTravelled() {
        // throw new UnsupportedOperationException("Please implement the ProductionRemoteControlCar.getDistanceTravelled() method");
        return distanceTravelled;
    }

    public int getNumberOfVictories() {
        // throw new UnsupportedOperationException("Please implement the ProductionRemoteControlCar.getNumberOfVictories() method");
        return numberOfVictories;
    }

    public void setNumberOfVictories(int numberOfVictories) {
        // throw new UnsupportedOperationException("Please implement the ProductionRemoteControlCar.setNumberOfVictories() method");
        this.numberOfVictories = numberOfVictories;
    }

    public int compareTo(ProductionRemoteControlCar otherCar) {
        // You can write it either way
        // ✅ but recommended way is to use Integer.compare() more readable
        // return (this.numberOfVictories < numberOfVictories) ? -1 : ((this.numberOfVictories == numberOfVictories) ? 0 : 1);
        return Integer.compare(otherCar.numberOfVictories, numberOfVictories);
    }
}
