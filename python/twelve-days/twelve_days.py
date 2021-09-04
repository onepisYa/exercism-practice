from itertools import chain


def recite(start_verse, end_verse):
    def verse(start_verse):
        text_verse = [gifts[i] for i in range(start_verse)][::-1]

        return "".join(
            chain([
                f"On the {index[start_verse-1]} day of Christmas my true love gave to me: "
            ], text_verse))

    index = [
        "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
        "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    gifts = [
        "a Partridge in a Pear Tree.", "two Turtle Doves, and ",
        "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ",
        "six Geese-a-Laying, ", "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ", "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ", "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ]
    Error_text = """
    <Input Error> .
    Please input number 1-12, and start_verse <= end_verse !!!"""

    assert isinstance(start_verse, int) and isinstance(end_verse,
                                                       int), Error_text

    if start_verse == end_verse <= 12:
        return [verse(start_verse)]
    elif start_verse < end_verse <= 12:
        return [verse(i) for i in range(start_verse, end_verse + 1)]
    else:
        raise Exception(Error_text)
