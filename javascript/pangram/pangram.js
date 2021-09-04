//
// This is only a SKELETON file for the 'Pangram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isPangram = (str_) => {
 let str_map=new Map([...str_.toLowerCase().matchAll(/[a-z]/g)])
	return str_map.size==26
};

