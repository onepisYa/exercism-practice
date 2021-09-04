//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
export const hey=(message)=>{
	let bob=message.trim();
	let result;
	switch(true){
		case bob=="":
			result= "Fine. Be that way!";
			break;
		case bob.endsWith("?") && bob.toUpperCase()==bob && (bob.match(/[A-Z].*/)!=null):
			result= "Calm down, I know what I'm doing!";
			break;
		case bob.toUpperCase()==bob && (bob.match(/.*[A-Z].*/)!=null):
			result= "Whoa, chill out!";
			break;
		case bob.endsWith("?"):
			result= "Sure.";
			break;
		default:
			result= "Whatever.";
			break;
	}
	return result;
}
