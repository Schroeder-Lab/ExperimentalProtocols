% define your colour channels (LUTs) here:
% (row vectors of length 256 with values between 0 and 1)
red = linspace(0, 0, 256);
blue = linspace(0, 1, 256);
green = linspace(0, 1, 256);

% concatenate colour channels to a matrix [1 x 256 x 3]
im = cat(3, red, blue, green);

% transform values to integers between 0 and 255
im = uint8(round(im .* 255));

% plot image
figure
image(im)
axis image
set(gca, 'Visible', 'off')

% save image
% (NOTE: saves image into current folder)
imwrite(im, 'ourLUT.png')