import Store
import Product

toaster = Product(20.0,"toaster","10bs","toasty toaster");
microwave = Product(100.0,"toaster","20lbs","waves");
oven = Product(200.0,"toaster","300bs","toasty toaster");
products = [toaster,microwave,oven];
Target = Store(products,"11901 NE 158th st. Kenmore, WA","Susie");
spoon = Product(5.0,"spoon",".5lbs","spoon");
Target.inventory()
Target.add_product(spoon)
Target.inventory()
# toaster.display_information();
# print str(toaster.add_tax(.10));	
# toaster.sell();
# toaster.display_information();
# toaster.return_item("opened");
# toaster.display_information();
