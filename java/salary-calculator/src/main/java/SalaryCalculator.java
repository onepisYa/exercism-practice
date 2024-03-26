public class SalaryCalculator {
    public double salaryMultiplier(int daysSkipped) {
        return daysSkipped >= 5 ? 0.85 : 1.0;
    }

    public int bonusMultiplier(int productsSold) {
        // throw new UnsupportedOperationException("Please implement the SalaryCalculator.bonusMultiplier() method");
        return productsSold >= 20 ? 13 : 10;
    }

    public double bonusForProductsSold(int productsSold) {
        // throw new UnsupportedOperationException("Please implement the SalaryCalculator.bonusForProductsSold() method");
        return productsSold * bonusMultiplier(productsSold);
    }

    public double finalSalary(int daysSkipped, int productsSold) {
        // throw new UnsupportedOperationException("Please implement the SalaryCalculator.finalSalary() method");
        int baseSalary = 1000;
        double _finalSalary = baseSalary*salaryMultiplier(daysSkipped) + bonusForProductsSold(productsSold);
        return _finalSalary > 2000 ? 2000 : _finalSalary;
    }
}
