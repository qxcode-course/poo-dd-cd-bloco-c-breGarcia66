from Customer import Customer;
from Market import Market;

c1 = Customer('Armando');
c2 = Customer('Maria');
c3 = Customer('João');
c4 = Customer('Carol');
c5 = Customer('Lucas');

m = Market(3);

print(c1, c2, c3, c4, c5);
print(m, '\n');

m.arrive(c1);
m.arrive(c2);
m.arrive(c3);
m.arrive(c4);
m.arrive(c5);

m.callCustomer(0);  
print(m, '\n');

m.callCustomer(1);
print(m, '\n');

m.callCustomer(2);
print(m, '\n');

# m.callCustomer(0);
# print(m, '\n');

m.finish(0);
print(m, '\n');

m.finish(0);
print(m, '\n');
