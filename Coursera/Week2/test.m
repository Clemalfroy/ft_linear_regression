A = eye(5)
hist(A)
pinv(A)
A = magic(3)
sum(sum(A .* eye(9)))
A = [1 2; 3 4; 5 6]
A(3, 2)
t = [0:0.01:0.98]
y2 = cos(2 * pi * 4 * t)
y1 = sin(2 * pi * 4 * t)
plot (t, y2)
hold on
plot (t, y1, 'r')
xlabel('time')
ylabel('value')
legend('sin', 'cos')
title('titre')
close
figure(1); plot(t, y1, 'r')
figure(1); plot(t, y2)
subplot(4,4,1)
plot (t, y1, 'r')
subplot(4,4,2)
plot (t, y1, 'b')
clf


