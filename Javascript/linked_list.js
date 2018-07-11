function SSL() {
	this.head = null;
}

function Node (value) {
	this.value = value;
	this.next = null;
}

SLL.prototype.addToFront = function(value) {
	var temp = new Node(value);
	temp.next = this.head;
	this.head = temp;
	
};

SLL.prototype.contains = function(value) {
	var current = this.head;
	var contains_value = false;

	while(current != null){
		if(current.value === value){
			contains_value = true;
		}
	}

	return contains_value;
};