public enum LogLevel {
    TRACE("[TRC]",1),
    DEBUG("[DBG]", 2),
    INFO("[INF]", 4),
    WARNING("[WRN]", 5),
    ERROR("[ERR]", 6),
    FATAL("[FTL]", 42),
    UNKNOWN("[UNK]", 0);

    private final String logLevel;
    private final int shortLog;
    LogLevel(String logLevel, int shortLog){
        this.logLevel = logLevel;
        this.shortLog = shortLog;
    }
    public String getLogLevel() {
        return this.logLevel;
    }
    public int getShortLog() {
        return this.shortLog;
    }
    static LogLevel getLogLevel(String shortLogLevelString) {
        switch(shortLogLevelString){
            case "[TRC]":
                return LogLevel.TRACE;
            case "[DBG]":
                return LogLevel.DEBUG;
            case "[INF]":
                return LogLevel.INFO;
            case "[WRN]":
                return LogLevel.WARNING;
            case "[ERR]":
                return LogLevel.ERROR;
            case "[FTL]":
                return LogLevel.FATAL;
            default:
                return LogLevel.UNKNOWN;
        }
    }
}
