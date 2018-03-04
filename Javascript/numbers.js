var arr = [1,2,'hello',5,'hi'];

function numbers_only(arr){

	for(var i =0; i<arr.length; i++) {
		if(typeof arr[i] != 'number'){
			arr.splice(i,1);
		}
	}

	return arr;
}

var result = numbers_only(arr);
console.log(result)