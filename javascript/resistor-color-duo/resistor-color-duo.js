//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const decodedValue = (arr) => {
	const color=["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
	let [ten,single]=arr.map(function(find_color){return color.findIndex(function(item){return item==find_color})})
	return 10*ten+single
};
