x = csvread("output.csv")

step = x(:,1)
val1 = x(:,2)
val2 = x(:,3)

plot(step,val1)
hold on;
plot(step, val2)
