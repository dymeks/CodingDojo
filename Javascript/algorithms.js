//prints all numbers between 1 and 255
function print1_255(){
	for(var i =1; i <= 255; i++){
		console.log(i);
	}
}

//pritn odd numbers between 1 and 255
function print_odds(){
	for(var i =1; i <=255; i++){
		if(i%2 != 0){
			console.log(i);
		}
	}
}

//print the number being added and the running sum from 0-255
function print_running_sum(){
	var sum = 0;
	for(var i = 0; i<=255; i++){
		sum += i;
		console.log(i);
		console.log(sum);
	}
}

//print the entire contents of an array
function print_array(array){
	for(var i =0; i< array.length; i++){
		console.log(array[i]);
	}
}

//print the maximum value in an array
function print_max(array){
	var max = array[0];
	for(var i =1; i<array.length;i++){
		if(array[i] > max){
			max = array[i];
		}
	}
	console.log(max);
}

//print the average of an array
function print_average(array){
	var sum = array[0];
	var average;
	for(var i =1; i<array.length; i++){
		sum += array[i];
	}
	average = sum/array.length;
	console.log(average)
}

//make an array of all the odd numbers between 1 and 255
function array_of_odds(){
	var result =[];
	for(var i = 0; i <=255; i++){
		if(i%2 != 0){
			result.push(i);
		}
	}
	return result;
}

//square all the elements in an array
function square_array(array){
	for(var i = 0; i < array.length; i++){
		array[i] = array[i]*array[i];
	}
	return array;
}

//print the number of elements in an array greater then Y.
function greater_thanY(array,y){
	var count = 0;
	for(var i =0; i <array.length; i++){
		if(array[i] > y){
			count++;
		}
	}
	console.log(count);
}

//replace all negative numbers in the array with 0.
function zero_out_negatives(array){
	for(var i =0; i <array.length; i++){
		if(array[i] < 0){
			array[i] = 0;
		}
	}
	return array;
}

//print the max, min and average values in an array.
function print_max_min(array){
	var max = array[0];
	var min = array[0];
	var sum = array[0];
	var average;
	for(var i =1; i < array.length; i++){
		if(array[i] > max) {
			max = array[i];
		}
		if(array[i] < min){
			min = array[i];
		}
		sum += array[i]

	}
	average = sum/array.length;
	console.log(min);
	console.log(max);
	console.log(average);
}

//shift everything in the array to the left. Replace the last element in the array with a 0.
function shift_left(array){
	for(var i = 0; i < array.length-1; i++){
		array[i] = array[i+1];
	}
	array[array.length-1] = 0;
	return array;
}

//replace negative numbers in the array with "Dojo".
function swap_negatives_dojo(array){
	for(var i =0; i<array.length; i++){
		if(array[i] < 0){
			array[i] = 'Dojo';
		}
	}
	return array;
}
//InsertAt takes an index to insert at and a value to insert at the 
//specified index
function insertAt(index,value){

}

//Removes the item at a  specific index
function removeAt(index){

}

function pushFront(value){

}

function popFront(){

}

function reverse(arr){

}

function removeDuplicates(){

}

function isSupervolcaic(str){
	var lowercase = str.lower()
	var vowels = {a:0,e:0,i:0,o:0,u:0}

	for(var i =0; i<lowercase.length; i++){
		if(lowercase[i] == 'a' || lowercase[i] == 'e' || lowercase[i] == 'i' || lowercase[i] == 'o' || lowercase[i] == 'u'){
			if(vowels[lowercase[i]] == 1){
				return false;
			}
			vowels[lowercase[i]]++;
		}
	}

	for(letter in vowels){
		if(vowels[letter] == 0){
			return false;
		}
	}

	return true;
}

function isPalendrome(str){
	start_index = 0;
	end_index = len(str) -1;

	while(start_index > end_index){
		if(str[start_index] !== str[end_index]){
			return false;
		}
		start_index ++;
		end_index --;
	}
	return true;
}

// console.log(isPalendrome("racecar"));

function removeSpaces(str) {
	var removed_spaces = ''

	for(var i = 0; i < str.length; i++){
		if(str[i] != ' '){
			removed_spaces += str[i];
		}
	}

	return removed_spaces;
}

function accronym(str){

}

function changeMatrixValue(matrix,value){
	for(var row = 0; row < matrix.length; row++){
		for(var col = 0; col < matrix[row].length; col++) {
			if(matrix[row][col] != value){
				matrix[row][col] =value;
			}
		}
	}
	return matrix;
}

//Print Roman Numerals given a number
function printRomanNumerals(number){
	if(type(number) == number){
		var romanNumeral = "";
		var romanNumeralValues ={
			'M':1000,
			'CM':900,
			'D':500,
			'CD':400,
			'C':100,
			'XC':90,
			'L':50,
			'XL':40,
			'X':10,
			'IX':9,
			'V':5,
			'IV':4,
			'I':1
		}

		var romanNumeralOrdered = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"];

		for(var i =0; i < romanNumeralOrdered.length;i++){
			while(number > romanNumeralValues[romanNumeralOrdered[i]]){
				romanNumeral += romanNumeralOrdered[i];
				number -=romanNumeralValues[romanNumeralOrdered[i]];
			}
		}
	}
}

function splice(arr, indx, value){
	arr.push(value);
	for(let i = arr.length-1; i > indx; i--){
		arr[i] = arr[i-1];
	}

	arr[indx] = value;

	return arr;
}

arr = [1,2,3,4];

function removeNegatives(arr) {
	for(let i = 0; i <= arr.length; i++){
		
		if(arr[i] < 0){
			for(let j = i; j < arr.length-1 ; j++){
				
				arr[j] = arr[j+1];
			}
			
			arr.pop();
			i--;
		}
	}
	
}

// removeNegatives([-1,-3,-2,-5,-8,-9]);

function quickSortInitial(arr){
	console.log("I'm TOP Quicksort");
	quickSort(arr, 0, arr.length -1);
	
}

function quickSort(arr, leftIndex, rightIndex){
	console.log("I'm LOWER Quicksort");
	console.log(leftIndex + " " + rightIndex);
	if(leftIndex >= rightIndex){
		return;
	}

	let pivotIndex = Math.floor((leftIndex + rightIndex) /2);

	let sortedIndex = partition(arr, leftIndex, rightIndex, pivotIndex);

	quickSort(arr, leftIndex, sortedIndex - 1);
	quickSort(arr, sortedIndex, rightIndex);
}

function partition(arr, leftIndex, rightIndex, pivotIndex){
	console.log("I'm in PARTITION!");
	console.log( leftIndex +" "+ rightIndex)
	while(leftIndex <= rightIndex){
		while(arr[leftIndex] < arr[pivotIndex]){
			leftIndex++;
		}

		while(arr[rightIndex] > arr[pivotIndex]){
			rightIndex--;
		}
		console.log("left and right before swap: " + leftIndex + " " + rightIndex);
		if(arr[leftIndex] < arr[rightIndex]){
			var temp = arr[leftIndex];
			arr[leftIndex] = arr[rightIndex];
			arr[rightIndex] = temp;

			leftIndex++;
			rightIndex--;
		}
	}

	return leftIndex;
}

quickSortInitial([1,5,10,3,9,2]);