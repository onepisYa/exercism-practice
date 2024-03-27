public class LogLine {

    private final String logLine;
    public LogLine(String logLine) {
        this.logLine = logLine;
    }

    public LogLevel getLogLevel() {
        String logLevelString = this.logLine.substring(0, logLine.indexOf("]")+1);
//        boolean isLogLevel;
//        LogLevel result = null;
//        for (LogLevel logLevel : LogLevel.values()){
//            isLogLevel = logLevel.getLogLevel().equals(logLevelString);
//            if(isLogLevel){
//                result = logLevel;
//                break;
//            }
//        }
//        if (result == null) {
//            return LogLevel.UNKNOWN;
//        }
//        return result;

        // 也可以使用 switch 语句、我封装在了 LogLevel 类中
        return LogLevel.getLogLevel(logLevelString);
    }

    public String getOutputForShortLog() {
        // throw new UnsupportedOperationException("Please implement the getOutputForShortLog() method");
        LogLevel logLevel = this.getLogLevel();
        int shortLogLevel = logLevel.getShortLog();
        String message = this.getMessage();
        return shortLogLevel+ ":" + message;
    }
    public String getMessage() {
        return this.logLine.substring(this.logLine.indexOf(":")+1).trim();
    }
}