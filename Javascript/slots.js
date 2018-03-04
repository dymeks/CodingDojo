var quarters = 10;

function slots (quarters) {
	var max = 100;
	var min = 50;

	while(quarters != 0) {
		var slot_machine = Math.floor(Math.random()*10);
		console.log("The slot machine says: " + slot_machine);
		
		if(slot_machine >= 8) {
			var quarters_added = generate_random_number(min,max);
			quarters += quarters_added;
			console.log("JACKPOT!");
			console.log("I added " + quarters_added + "to my purse and now have " + quarters +" quarters");
			break;
		} 

		quarters--;

	}

	console.log("I ran out of money :( ")
}

function generate_random_number(min,max){
	return Math.ceil(Math.random() * (max-min) + min);
}

slots(quarters);