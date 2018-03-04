var number_of_days = 30;
var initial_amount = 0.01;

function few_billion(days,initial_amount) {
	var amount_sofar = initial_amount;
	for(var i =2; i <= days; i++) {
		if(amount_sofar > 10000 && amount_sofar < 10500) {
			console.log("It takes " + i +" days to make $10,000");

		} else if(amount_sofar > 1000000000 && amount_sofar < 100000000) {
			console.log("It takes " + i +" days to make $1,000,000,000");
		}

		amount_sofar = amount_sofar*2;
		console.log("Amount after " + i + "days: " + amount_sofar);
	}
}

few_billion(number_of_days,initial_amount);