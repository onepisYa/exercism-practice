public class LogLevels {
    public static String message(String logLine) {
        // throw new UnsupportedOperationException("Please implement the (static) LogLevels.message() method");
        // return logLine.split(":")[1].trim();
        return logLine.substring(logLine.indexOf(":") + 1).trim();
    }

    public static String logLevel(String logLine) {
        // String logLevelString = logLine.split(":")[0].trim();
        // return logLevelString.substring(logLevelString.indexOf("[") + 1, logLevelString.indexOf("]")).strip().toLowerCase();
        return logLine.substring(1, logLine.indexOf("]"))
                        // [ERROR] 只留下 ERROR
                        // 提取了 才 1 到 长度减 1 的子字符串
                .trim().toLowerCase();
    }

    public static String reformat(String logLine) {
        // 虽然 String.format 这是一种美妙而强大的方法，
        // 但对于只需要与 + 运算符进行简单 String 串联的问题来说，它非常慢。
        // 有关 的性能的更多信息 String.format ，请查看 Java 字符串串联：哪种方式最好？。
        // https://redfin.engineering/java-string-concatenation-which-way-is-best-8f590a7d22a8
        // return String.format("%s (%s)",message(logLine), logLevel(logLine));
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
