var symbol = "-->";
var reversed = true;

function fancy_print(arr,symbol,reversed){
	var start = 0;
	var end = arr.length;
	if(reversed) {
		for(var i =arr.length-1; i >=0;i--){
			console.log(i + symbol + arr[i]);
		}
	} else {
		for(var i =0; i <arr.length;i++){
			console.log(i + symbol + arr[i]);
		}
	}

	
	
}

fancy_print([1,2,3,4,6],symbol,reversed);