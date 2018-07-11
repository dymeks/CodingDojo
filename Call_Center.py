import random

class Call(object):
	"""docstring for Call"""
	def __init__(self,caller_name, caller_phone_number,time_of_call,call_reason):
		super(Call, self).__init__()
		self.name = caller_name;
		self.unique_id = random.randint(0,10);
		self.number = caller_phone_number;
		self.time_of_call = time_of_call;
		self.call_reason = call_reason; 
	def	display(self):
		print self.name;
		print self.unique_id;
		print self.number;
		print self.time_of_call;
		print self.call_reason;
		
class CallCenter(object):
	"""docstring for CallCenter"""
	def __init__(self, calls):
		# super(CallCenter, self).__init__()
		self.calls = calls;
		self.queue_size = len(calls);

	def add(self,call):
		self.calls.append(call);
		return self;

	def remove(self):
		self.calls.pop(0);
		return self;
	def info(self):
		print "Length of calls queue: " + str(len(self.calls));

		for call in self.calls:
			print call.name;
			print call.number;

	def remove_by_phone_number(self,phone_number):
		for call in self.calls:
			if (call.number == phone_number):
				self.calls.remove(phone_number);
		return self;				

call1 = Call("Susie","425-780-5496","3:00pm","Need Help");
call2 = Call("Bob","428-457-6598","4:00pm","No idea what is going on, help!");
call3 = Call("Bob","428-457-6598","4:00pm","No idea what is going on, help!");

callcenter1 = CallCenter([call1,call2,call3]);

callcenter1.info()
callcenter1.remove()
callcenter1.info()
callcenter1.add(call1)
callcenter1.info()
callcenter1.remove_by_phone_number("428-457-6598");
callcenter1.info()

		