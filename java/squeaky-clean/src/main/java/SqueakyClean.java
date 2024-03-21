import java.util.HashMap;
import java.util.Map;

class SqueakyClean {
    private static final char SPACE = '_';
    private static final char DASH = '-';
    private static final Map<Character, Character> LEETMAP = Map.of(
            '4' , 'a',
            '3' , 'e',
            '0' , 'o',
            '1' , 'l',
            '7' , 't'
    );

    static String clean(String identifier) {
        // throw new UnsupportedOperationException("Please implement the (static) SqueakyClean.clean() method");
        // java.lang.Character
        // goal is practice Chars and StringBuilder
        // leet-speak https://en.wikipedia.org/wiki/Leet
        //  3. convert leet-speak to normal text
        // ✅ 4. filter out non-alphanumeric characters

        StringBuilder sb = new StringBuilder();
        boolean isCapital = false;
        char[] chars = identifier.toCharArray();
        for (char _char : chars) {
            // ✅ 1. replace space include leading and trailing spaces to underline _
            // ✅ 2. convert kebab-case to camelCase
            if (Character.isWhitespace(_char)) {
                sb.append(SPACE);
                isCapital = false;
            } else if (_char == DASH) {
                isCapital = true;
            }
            else if(LEETMAP.containsKey(_char)) {
                sb.append(LEETMAP.get(_char));
            }else if (Character.isLetter(_char)) {
                if (isCapital) {
                    sb.append(Character.toUpperCase(_char));
                    isCapital = false;
                } else {
                    sb.append(_char);
                }
            }
        }
        return sb.toString();
    }
}
