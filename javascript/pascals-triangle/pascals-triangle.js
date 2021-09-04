//
// This is only a SKELETON file for the 'Pascals Triangle' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const rows = (num) => {
	"use strict";
	let base_arr=[[1],[1,1]];

	function gen_new_arr(num){
		let end_arr=base_arr[base_arr.length-1]
		let new_arr=new Array(num);
		new_arr.fill(1);
		for (let i=1;i<end_arr.length;i++){
			new_arr[i]=end_arr[i-1] +end_arr[i]
		}
		base_arr.push(new_arr)
	}

	if (num==1){
		return [[1]]
	}
	else if (num==2){
		return [[1],[1,1]]
	}
	else if(num>2){
		for (let i=3;i<=num;i++){
			gen_new_arr(i);
		}
		return base_arr;
	}
	else {
		return []
	}

	

};

