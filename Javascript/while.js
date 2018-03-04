var days_till_birthday = 60;

function birthday_wait(days_till_birthday){
	while(days_till_birthday != 0) {
		if(days_till_birthday > 30) {
			console.log("I'm so sad, I have " + days_till_birthday + "days till my birthday");
		} else if (days_till_birthday < 30 && days_till_birthday > 5) {
			console.log("I can't wait for my birthday! It's almost here!");
		} else if(days_till_birthday <= 5) {
			console.log(days_till_birthday + " DAYS TILL MY BIRTHDAY!");
		}

		days_till_birthday--;
	}

	console.log("~~~~~ PARTY!!!! :) :) :) ~~~~");
}

birthday_wait(days_till_birthday);