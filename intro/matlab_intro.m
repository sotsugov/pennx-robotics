% Create x from -2 to 2 in steps of 0.5
x = -2:0.5:2;

% Use x to create y according to the formula in the description
y = 3*x.^2 + 2*x - 6;

r1 = 2;
area1 = areaCircle(r1)
r2 = [2 5; 0.5 1];
area2 = areaCircle(r2)
r3 = [1 1.5 3 -4];
area3 = areaCircle(r3)

function area = areaCircle(r)
% Function named areaCircle to calculate the are of a circle. 
% The function should take one input that is the radius of the circle.
% The function should work if the input is a scalar, vector, or matrix.
% The function should return, one ouput, the same size as the input, that contains the area of a circle for each correspoding element.
% If a negative radius passed as input, the function should return the value -1 to indicate the error.
negIndices = r < 0;
area = pi * r.^2;
area(negIndices) = -1;
end