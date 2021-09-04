def response(hey_bob):
    if hey_bob.strip().endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.strip().endswith("?"):
        return "Sure."
    elif hey_bob.strip()=="":
        return "Fine. Be that way!"
    else:
        return "Whatever."

bob_dic={(True,True,False):"Calm down, I know what I'm doing!",(True,False,False):"Sure.",(False,True,False):"Whoa, chill out!",(False,False,False):"Whatever.",(False,False,True):"Fine. Be that way!"}
def response1(hey_bob):
    bob=hey_bob.strip()
    bob_key=(bob.endswith("?"),bob.isupper(),bob=="")
    return bob_dic.get(bob_key)

