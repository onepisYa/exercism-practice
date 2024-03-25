import java.util.Arrays;
import java.util.Map;
public class CarsAssemble {
    private final Map<Range,Double> rateRangeMap = Map.of(
            new Range(1,4),1.0,
            new Range(5,8),0.9,
            new Range(9,9),0.8,
            new Range(10,10),0.77
    );

    public double productionRatePerHour(int speed) {
        int producedEachHour = 221;
        return producedEachHour *speed*getRate(getRange(speed));
    }

    public int workingItemsPerMinute(int speed) {
        return (int)(productionRatePerHour(speed)/60);
    }

    private Range getRange(int speed){
        return Arrays.stream(rateRangeMap.keySet().toArray(new Range[0]))
                .filter(range -> range.contains(speed))
                .findFirst()
                .orElse(null);
    }
    private double getRate(Range range){
        try{
            return rateRangeMap.get(range);
        } catch(NullPointerException e){
            return 0.0;
        }
    }
}

class Range{
    int min;
    int max;
    Range(int min,int max){
        this.min = min;
        this.max = max;
    }
    public boolean contains(int speed) {
        return speed >= min && speed <= max;
    }
}
