# Flags

## National Flags

### Germany

3:5 <img alt="German Flag" src="germany.svg" width="150"/>

**HUMAN**: *What are the correct proportions of the national flag of Germany?*

**CHAT**: *The national flag of Germany has proportions of 3:5. This means that the length of the flag is 1.67 times its height. The flag consists of three equal 
horizontal bands with the colors black, red, and gold from top to bottom.*

**HUMAN**: *Generate an SVG file containing a rectangle with a height of 360 and a width of 600, divided into three equal horizontal 
bands of black, red, and gold from top to bottom.*

**CHAT**:

    `<svg width="600" height="360">
        <rect width="600" height="120" y="0" fill="black" />
        <rect width="600" height="120" y="120" fill="red" />
        <rect width="600" height="120" y="240" fill="gold" />
    </svg>`



### Great Britain

 3:5 <img alt="Great Britain Flag" src="great-britain.svg" width="150"/> 1:2 for Navy<img alt="Great Britain Navy Flag" src="great-britain-navy.svg" width="150"/>

**HUMAN**: *What are the correct proportions of the national flag of Great Britain?*

**CHAT**: *The national flag of Great Britain, also known as the Union Jack or Union Flag, has proportions of 1:2. This means that the length of the flag is 
twice its height. The Union Jack is a combination of the flags of England, Scotland, and Northern Ireland, and features the following elements: 
the Cross of St. George for England (red on a white background), the Cross of St. Patrick for Northern Ireland (red on a white background, diagonally), 
and the Cross of St. Andrew for Scotland (white on a blue background, diagonally).*

The Union Jack is more complex and requires the human operator to develop a proper learning program for the CHAT.
Each step must be checked because the CHAT makes errors in evaluating the text and also in the calculations.
Thus, the human operator has to step in and make the appropriate corrections.

#### Draw the rectangle

**HUMAN**: Generate an SVG code that draws a blue rectangle with a width of 600 and a height of 360, with the color being RGB 003371.

**CHAT**:

    `<svg xmlns="http://www.w3.org/2000/svg" width="640" height="320">
        <rect width="640" height="320" fill="#003371" />
    </svg>`

#### Draw the St. Andrews Cross

**HUMAN**: Using the previously generated code:
Add a white line that goes from the top left vertex to the bottom right vertex. 
The line has a width of 1/5 the height of the rectangle. 
Also, add a white line that goes from the bottom left vertex to the top right vertex. 
The line has a width of 1/5 the height of the rectangle.

**CHAT**:

    `<svg xmlns="http://www.w3.org/2000/svg" width="640" height="320">
        <rect width="640" height="320" fill="#003371" />
        <line x1="0" y1="0" x2="640" y2="320" stroke="white" stroke-width="64" />
        <line x1="0" y1="320" x2="640" y2="0" stroke="white" stroke-width="64" />
    </svg>`

#### Draw the St. Patrick's Cross

**HUMAN**: 
Using the previous generated code:
- Add a new line at the end, staring at the upper left corner and ending in the middle, 
  the line color is CE1126, the width of the line is 1/15 of the height of the rectangle. 
- Move the stating point of the last line -1/20 of the rectangle width to the left. 
- Move the starting point of the last line -1/20 of the rectangle height to the top.
- Transform the last line translating it 1/15 of the rectangle height horizontally to the left.

**CHAT**:

    `<svg width="640" height="320">
        <rect width="640" height="320" fill="#003371" />
        <line x1="0" y1="0" x2="640" y2="320" stroke="white" stroke-width="64" />
        <line x1="0" y1="320" x2="640" y2="0" stroke="white" stroke-width="64" />
        <line x1="-32" y1="-16" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(-21.33, 0)" />
    </svg>`

**HUMAN**:
Using the previous generated code:
- Add a new line at the end, staring at the lower left corner and ending in the middle,
  the line color is CE1126, the width of the line is 1/15 of the width of the rectangle.
- Move the stating point of the last line -1/20 of the rectangle width to the left.
- Move the starting point of the last line 1/20 of the rectangle height to the bottom.
- Transform the last line translating it 1/15 of the rectangle height horizontally to the right.

**CHAT**:

    `<svg width="640" height="320">
        <rect width="640" height="320" fill="#003371" />
        <line x1="0" y1="0" x2="640" y2="320" stroke="white" stroke-width="64" />
        <line x1="0" y1="320" x2="640" y2="0" stroke="white" stroke-width="64" />
        <line x1="-32" y1="-16" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(-21.33, 0)" />
        <line x1="-32" y1="336" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(21.33, 0)" />
    </svg>`

**HUMAN**:
Using the previous generated code:
- Add a new line at the end, staring at the upper right corner and ending in the middle,
  the line color is CE1126, the width of the line is 1/15 of the width of the rectangle.
- Move the stating point of the last line 1/20 of the rectangle width to the right.
- Move the starting point of the last line 1/20 of the rectangle height to the top.
- Transform the last line translating it 1/15 of the rectangle height horizontally to the left.

**CHAT**:

    `<svg width="640" height="320">
        <rect width="640" height="320" fill="#003371" />
        <line x1="0" y1="0" x2="640" y2="320" stroke="white" stroke-width="64" />
        <line x1="0" y1="320" x2="640" y2="0" stroke="white" stroke-width="64" />
        <line x1="-32" y1="-16" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(-21.33, 0)" />
        <line x1="-32" y1="336" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(21.33, 0)" />
        <line x1="672" y1="-16" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(-21.33, 0)" />
    </svg>`

**HUMAN**:
Using the previous generated code:
- Add a new line at the end, staring at the lower right corner and ending in the middle,
  the line color is CE1126, the width of the line is 1/15 of the width of the rectangle.
- Move the stating point of the last line 1/20 of the rectangle width to the right.
- Move the starting point of the last line 1/20 of the rectangle height to the bottom.
- Transform the last line translating it 1/15 of the rectangle height horizontally to the right.

**CHAT**:

    `<svg width="640" height="320">
        <rect width="640" height="320" fill="#003371" />
        <line x1="0" y1="0" x2="640" y2="320" stroke="white" stroke-width="64" />
        <line x1="0" y1="320" x2="640" y2="0" stroke="white" stroke-width="64" />
        <line x1="-32" y1="-16" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(-21.33, 0)" />
        <line x1="-32" y1="336" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(21.33, 0)" />
        <line x1="672" y1="-16" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(-21.33, 0)" />
        <line x1="672" y1="336" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(21.33, 0)" />
    </svg>`

#### Draw the St. George's Cross

**HUMAN**:
Using the previous generated code:
- Add a new line at the end that divide the rectangle horizontally in two equal parts,
  the line is white and the width of the line is 1/3 of the height.
- Add a new line at the end that divide the rectangle vertically in two equal parts,
  the line is white and the width of the line is 1/3 of the height.
- Add a new line at the end that divide the rectangle horizontally in two equal parts,
  the line color is #CE1126 and the width of the line is 1/5 of the height.
- Add a new line at the end that divide the rectangle vertically in two equal parts,
  the line color is #CE1126 and the width of the line is 1/5 of the height.

**CHAT**:

    `<svg xmlns="http://www.w3.org/2000/svg" width="640" height="320">
      <rect x="0" y="0" width="640" height="320" fill="#002147" />
      <line x1="0" y1="320" x2="640" y2="0" stroke="#fff" stroke-width="64" />
      <line x1="0" y1="0" x2="640" y2="320" stroke="#fff" stroke-width="64" />
      <line x1="-32" y1="-16" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(-21.33,0)"/>
      <line x1="-32" y1="336" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(21.33,0)"/>
      <line x1="672" y1="-16" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(-21.33,0)"/>
      <line x1="672" y1="336" x2="320" y2="160" stroke="#CE1126" stroke-width="21.33" transform="translate(21.33,0)"/>
      <line x1="0" y1="160" x2="640" y2="160" stroke="white" stroke-width="106.67" />
      <line x1="320" y1="0" x2="320" y2="320" stroke="white" stroke-width="106.67" />
      <line x1="0" y1="160" x2="640" y2="160" stroke="#CE1126" stroke-width="64" />
      <line x1="320" y1="0" x2="320" y2="320" stroke="#CE1126" stroke-width="64" />
    </svg>`