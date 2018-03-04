var skip = 2;
var start_point = -4;
var end_point = 20;

function print_range(start_point,skip,end_point){
	if(skip == undefined) {
		skip = 1;
	}
	var index = start_point;

	if(end_point == undefined) {
		end_point = start_point;
		start_point = 0;
		if(end_point < start_point){
			index = end_point;
		}
		
		
	}

	while(index <= end_point) {
		console.log(index);
		index += skip;
	}
}

print_range(start_point,skip);