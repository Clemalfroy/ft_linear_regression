% x refers to the mileage in km
% y refers to the price in $

%% Initialization
clear ; close all; clc

fprintf('Plotting Data ...\n')

data = csvread('data.csv');
data = data(2:size(data,1), 1:2);
X = data(:, 1); y = data(:, 2);

m = length(y); % number of training examples

% Plot Data
plotData(X, y);
[X mu sigma] = featureNormalize(X);
X = [ones(m, 1), X]; % Add a column of ones to x
theta = zeros(2, 1); % initialize fitting parameters

% Some gradient descent settings
iterations = 1500;
alpha = 0.1;

% run gradient descent
theta = gradientDescent(X, y, theta, alpha, iterations);

% print theta to screen
fprintf('Theta found by gradient descent:\n%f\n', theta);
 
% Plot the linear fit
hold on; % keep previous plot visible
plot(0, estimatep([0], mu, sigma, theta), 'bx', 'MarkerSize', 10, 'LineWidth', 2);
plot(50000, estimatep([50000], mu, sigma, theta), 'bx', 'MarkerSize', 10, 'LineWidth', 2);
plot(100000, estimatep([100000], mu, sigma, theta), 'bx', 'MarkerSize', 10, 'LineWidth', 2);
plot(150000, estimatep([150000], mu, sigma, theta), 'bx', 'MarkerSize', 10, 'LineWidth', 2);
plot(200000, estimatep([200000], mu, sigma, theta), 'bx', 'MarkerSize', 10, 'LineWidth', 2);
plot(250000, estimatep([250000], mu, sigma, theta), 'bx', 'MarkerSize', 10, 'LineWidth', 2);
legend('Training data', 'Linear regression')
hold off % don't overlay any more plots on this figure

% Grid over which we will calculate J
theta0_vals = linspace(-10000, 10000, 100);
theta1_vals = linspace(-10000, 10000, 100);

% initialize J_vals to a matrix of 0's
J_vals = zeros(length(theta0_vals), length(theta1_vals));

% Fill out J_vals
for i = 1:length(theta0_vals);
    for j = 1:length(theta1_vals)
	  t = [theta0_vals(i); theta1_vals(j)];
	  J_vals(i,j) = computeCost(X, y, t);
    end
end

% Because of the way meshgrids work in the surf command, we need to
% transpose J_vals before calling surf, or else the axes will be flipped
J_vals = J_vals';
% Surface plot
figure;
surf(theta0_vals, theta1_vals, J_vals);
xlabel('\theta_0'); ylabel('\theta_1');

% Contour plot
figure;
% Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
contour(theta0_vals, theta1_vals, J_vals, logspace(-20, 30, 200));
xlabel('\theta_0'); ylabel('\theta_1');
hold on;
plot(theta(1), theta(2), 'rx', 'MarkerSize', 10, 'LineWidth', 2);
save theta.mat theta
save mu.mat mu
save sigma.mat sigma