public class Lasagna {
    int varExpectedMinutesInOven;

    public Lasagna(){
        this.varExpectedMinutesInOven = 40;
    }

    public Lasagna(int varExpectedMinutesInOven){
        this.varExpectedMinutesInOven = varExpectedMinutesInOven;
    }

    // define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven() {
        return this.varExpectedMinutesInOven;
    }

    // define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int actualMinutesInOven) {
        return this.expectedMinutesInOven() - actualMinutesInOven;
    }

    // define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int layer) {
        return layer * 2;
    }

    // define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int layer, int actualMinutesInOven) {
         return actualMinutesInOven + this.preparationTimeInMinutes(layer);
    }
}
