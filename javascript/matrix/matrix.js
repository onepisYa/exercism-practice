//
// This is only a SKELETON file for the 'Matrix' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Matrix {
	constructor(str) {
		this.arr=str.split('\n').map(s=>s.split(/\s/).map(Number));
	}

	get rows() {
		return this.arr
	}

	get columns() {
		return this.arr[0].map((_,index)=>this.arr.map(row=>row[index]))
	}
}


