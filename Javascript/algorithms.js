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

}

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
		for(var col = 0; col < matrix[row].length) {
			if(matrix[row][col] != value){
				matrix[row][col] =value;
			}
		}
	}
	return matrix;
}