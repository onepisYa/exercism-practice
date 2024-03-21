class CalculatorConundrum {
    public String calculate(int operand1, int operand2, String operation) {
//        throw new UnsupportedOperationException("Please implement the CalculatorConundrum.calculate() method");
if (operation == null){
    throw new IllegalArgumentException("Operation cannot be null");
}
        String result;
        switch (operation) {
            case "+":
                result = Integer.toString(operand1 + operand2);
                break;
            case "*":
                result = Integer.toString(operand1 * operand2);
                break;
            case "/":
                try{
                    result = Integer.toString(operand1 / operand2);
                    break;
                }catch (ArithmeticException e){
                    // 注意错误类型 以及传递 cause 原因.
                    throw new IllegalOperationException("Division by zero is not allowed", e);
                }
            case "":
                // 注意错误类型
                throw new IllegalArgumentException("Operation cannot be empty");
            case "-":
                // result = Integer.toString(operand1 - operand2);
                // break;
            default:
                throw new IllegalOperationException("Operation '" + operation + "' does not exist");
        }

        return operand1 + " " + operation + " " + operand2 + " = " + result;
    }
}
