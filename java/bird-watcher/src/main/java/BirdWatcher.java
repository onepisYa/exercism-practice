
import java.util.Arrays;
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        // throw new UnsupportedOperationException("Please implement the BirdWatcher.getLastWeek() method");
        return new int[]{0, 2, 5, 3, 7, 8, 4};
    }
    public int getLastIndex(){
        return this.birdsPerDay.length-1;
    }
    public int getToday() {
        // throw new UnsupportedOperationException("Please implement the BirdWatcher.getToday() method");
        
        return this.birdsPerDay[this.getLastIndex()];
    }

    public void incrementTodaysCount() {
        // throw new UnsupportedOperationException("Please implement the BirdWatcher.incrementTodaysCount() method");
        this.birdsPerDay[this.getLastIndex()]+=1;
    }

    public boolean hasDayWithoutBirds() {
        // throw new UnsupportedOperationException("Please implement the BirdWatcher.hasDayWithoutBirds() method");
        boolean withoutBirds = false;
        for (int j : this.birdsPerDay) {
            if (j == 0) {
                withoutBirds = true;
                break;
            }
        }
        return withoutBirds;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int length = this.birdsPerDay.length;
        int iterate_length = Math.min(numberOfDays, length);
        return Arrays.stream(this.birdsPerDay).limit(iterate_length).sum();
    }

    public int getBusyDays() {
        // throw new UnsupportedOperationException("Please implement the BirdWatcher.getBusyDays() method");
        return (int) Arrays.stream(this.birdsPerDay).filter(el -> el >= 5 ).count();
    }
}
