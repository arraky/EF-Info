// MODIFY BELOW VARIABLES TO CUSTOMIZE
/*

 WIDTH
  <->
 _____
/     \
▏     ▕       
▏     ▕  ^
▏     ▕  | Height
┕┒    ▕  ⌄ 
 ▕____▕ 

*/

WEMOS_WIDTH = 25;
WEMOS_HEIGHT = 35;
WEMOS_THICKNESS = 1;
WEMOS_WIFI_THICKNESS = 1;
WEMOS_USB_THICKNESS = 2.5;
WEMOS_USB_WIDTH = 8;
WEMOS_USB_CENTER_TO_RIGHT = 14;

USB_CABLE_HEIGHT = 8;
USB_CABLE_WIDTH = 11;

/*
 WIDTH
  <->
 _____
/     \       ^  WEMOS_OLED_OFFSET_TOP
_______       ⌄
▏_____ ▏ ^      
▏▏OLED▏▏ | Height
▏▏___▕▕  ⌄
┕┒_____▏  

*/

WEMOS_OLED_OFFSET_TOP = 7; /* offset to wifi antenna when mounted*/
OLED_WIDTH = 26;
OLED_HEIGHT = 28;
OLED_AND_PINS_THICKNESS = 15;
OLED_THICKNESS = 1.3;
DISPLAY_WIDTH = 16;
DISPLAY_HEIGHT = 11.5;
DISPLAY_OFFSET_LR = 6.5;
DISPLAY_OFFSET_TOP = 1; // offset display to end of it's platine


/*
 WIDTH
  <->
 _______  ^
 ▏○   ◠ ▏ | Height
▕_______▏ ⌄    
SCL -> D1
SDA -> D2

*/
CO2_WIDTH = 25;
CO2_HEIGHT = 20;
CO2_THICKNESS = 1.7;
CO2_OFFSET_LEFT_ENS160 = 7.15;
CO2_OFFSET_BOTTOM_ENS160 = 13.5;
CO2_ENS160_SIZE = 3.2;
CO2_COMP_HEIGHT = 1.2;
CO2_COMP_OFFSET_RIGHT = 3;

CO2_OFFSET_LEFT_AHT21= 16.5;
CO2_OFFSET_BOTTOM_AHT21 = 11.5;
CO2_AHT21_SIZE = 3.5;


/*
           X
          <->
        ________     ^
Y /    /       /|    | Z
 /    /_______/ |    ⌄ 
      |       | /
      |_______|/
*/
BOX_X = WEMOS_HEIGHT;
BOX_Y = 36;
BOX_Z = 32;
WALL_THICKNESS = 1.2;

BOX_X_OUTER = BOX_X + 2 * WALL_THICKNESS;
BOX_Y_OUTER = BOX_Y + 2 * WALL_THICKNESS;
BOX_Z_OUTER = BOX_Z + 2 * WALL_THICKNESS;

// Stützen um Wemos draufzulegen
BOX_BAR_HEIGHT = 3;
BOX_BAR_WIDTH = 3;

// SENS
SENSOR_SUPPORT_BAR_WIDTH = 2.4;

// INTERN PARAMS
WEMOS_UPPER_HEIGHT = OLED_AND_PINS_THICKNESS + WEMOS_THICKNESS;
WEMOS_DISPLAY_OFFSET_TOP = WEMOS_OLED_OFFSET_TOP + DISPLAY_OFFSET_TOP;
CAP_PADDING = BOX_BAR_WIDTH + 2;


/**
 _
| |
|/
Stütze um den WEMOS draufzulegen
*/
module wemos_bar_left() {
    // verbindet die äussere Hülle von Objekten
    translate([0,0,-BOX_BAR_HEIGHT])
        hull() {
            translate([0, 0, BOX_BAR_HEIGHT - 1])
                cube([BOX_BAR_WIDTH, BOX_Y, 1]);
            cube([0.001, BOX_Y, 0.001]); // trick: ein ganz dünner Balken als unteren Rand
        }
}

/**
 _
| |
 \|
Stütze um den WEMOS draufzulegen
*/
module wemos_bar_right() {
    // verbindet die äussere Hülle von Objekten
    translate([0,BOX_Y,0])
        rotate([0,0,180])
            wemos_bar_left();
}

module usb_hole() {
    r = USB_CABLE_HEIGHT / 2;
    translate([-0.01, 0, -(USB_CABLE_HEIGHT - WEMOS_USB_THICKNESS) / 2 - 0.01])
    rotate([0, 90, 0])
        translate([-r, -(USB_CABLE_WIDTH - USB_CABLE_HEIGHT) / 2, 0])
            hull() {
                cylinder(WALL_THICKNESS+0.02, r, r, $fn=50);
                translate([0, USB_CABLE_WIDTH - USB_CABLE_HEIGHT, 0])
                    cylinder(WALL_THICKNESS+0.02, r, r, $fn=50);
            }
}

module display_hole() {
    center_x = DISPLAY_HEIGHT / 2;
    center_y = DISPLAY_WIDTH / 2;
    translate([center_x,center_y, 0.5])
        scale([DISPLAY_HEIGHT, DISPLAY_WIDTH, 1])
            rotate([0,0,45])
                cylinder(h=WALL_THICKNESS,r1=1/sqrt(2), r2=1.5/sqrt(2),$fn=4);
}

module sensor_hole(size) {
    r = size / 2; 
    translate([r, 0, r])
        rotate([-90, 0, 0])
            rotate([0,0,45])
                cylinder(h=WALL_THICKNESS+0.02, r1=sqrt(2)*size, r2=size / sqrt(2), $fn=4);

}

module box() {
    union() {
        difference() {
            // OUTER BOX
            translate([-WALL_THICKNESS, -WALL_THICKNESS, -WALL_THICKNESS])
                cube([BOX_X_OUTER, BOX_Y_OUTER, BOX_Z_OUTER]);

            // INNER BOX
            translate([0, -WALL_THICKNESS-0.1, 0])
                cube([BOX_X,BOX_Y+0.1,BOX_Z]);

            // USB Hole
            usb_y = BOX_Y - WEMOS_USB_CENTER_TO_RIGHT;
            usb_z = BOX_Z - WEMOS_UPPER_HEIGHT - WEMOS_USB_THICKNESS;
            translate([BOX_X, usb_y, usb_z])
                usb_hole();

            // DISPLAY HOLE
            translate([WEMOS_DISPLAY_OFFSET_TOP, BOX_Y - DISPLAY_OFFSET_LR - DISPLAY_WIDTH, BOX_Z - 0.01])
                union() {
                    cube([DISPLAY_HEIGHT, DISPLAY_WIDTH, WALL_THICKNESS + 0.02]);
                    display_hole();
                }
            
            // CAP REMOVAL HOLE
            translate([BOX_X / 2, WALL_THICKNESS / 2 - 2.6, -WALL_THICKNESS*1.1])
                rotate([0, 0, 45])
                    cylinder(h=WALL_THICKNESS+0.02, r1=8 / sqrt(2), r2= 4 / sqrt(2), center=true, $fn=4);
            
        }
        // WIFI-SIDE
        translate([0, 0, BOX_Z - WEMOS_UPPER_HEIGHT])
            wemos_bar_left();

        // USB-SIDE
        translate([BOX_X, 0, BOX_Z - WEMOS_UPPER_HEIGHT - WEMOS_USB_THICKNESS])
            wemos_bar_right();
    }
}

module cap() {
    offset = 0.05;
    difference() {
        union() {
            // BASE
            translate([-WALL_THICKNESS, -WALL_THICKNESS, -WALL_THICKNESS])
                cube([BOX_X_OUTER, WALL_THICKNESS, BOX_Z_OUTER]);
            // INSET
            translate([-offset, 0, -offset])
                cube([BOX_X + 2 * offset, WALL_THICKNESS, BOX_Z + 2 * offset]);
            // HOLDER LEFT
            translate([CAP_PADDING - WALL_THICKNESS, WALL_THICKNESS, WALL_THICKNESS])
                cube([WALL_THICKNESS, CO2_THICKNESS + WALL_THICKNESS, CO2_HEIGHT]);
            
            // HOLDER RIGHT
            translate([CAP_PADDING + CO2_WIDTH, WALL_THICKNESS, WALL_THICKNESS])
                cube([WALL_THICKNESS, CO2_THICKNESS + WALL_THICKNESS, CO2_HEIGHT]);

            // HOLDER BOTTOM
            translate([CAP_PADDING-WALL_THICKNESS, WALL_THICKNESS, 0])
                cube([CO2_WIDTH+2*WALL_THICKNESS, CO2_THICKNESS + WALL_THICKNESS, WALL_THICKNESS]);
            
            // HOLDER TOP
            translate([CAP_PADDING-WALL_THICKNESS, CO2_THICKNESS + WALL_THICKNESS, 0])
                cube([CO2_WIDTH+2*WALL_THICKNESS, WALL_THICKNESS, CO2_HEIGHT + WALL_THICKNESS]);
        }
        // AHT21
        aht_x = CAP_PADDING + CO2_OFFSET_LEFT_AHT21;
        aht_y = -WALL_THICKNESS - 0.01;
        aht_z = WALL_THICKNESS + CO2_OFFSET_BOTTOM_AHT21;
        translate([aht_x,aht_y,aht_z])
            sensor_hole(CO2_AHT21_SIZE );
        
        

        // ENS160        
        ens_x = CAP_PADDING + CO2_OFFSET_LEFT_ENS160;
        ens_y = -WALL_THICKNESS - 0.01;
        ens_z = WALL_THICKNESS + CO2_OFFSET_BOTTOM_ENS160;
        translate([ens_x, ens_y, ens_z])
            sensor_hole(CO2_ENS160_SIZE);

        // SPARE PLACE FOR COMPONENTS
        translate([CAP_PADDING, WALL_THICKNESS - CO2_COMP_HEIGHT, WALL_THICKNESS])
            cube([CO2_WIDTH - CO2_COMP_OFFSET_RIGHT, CO2_COMP_HEIGHT + 0.1, BOX_Z]);

        // REMOVE PART OF CO2 HOLDER TOP
        translate([CAP_PADDING + (SENSOR_SUPPORT_BAR_WIDTH / 2) *WALL_THICKNESS, WALL_THICKNESS, WALL_THICKNESS])
            cube([CO2_WIDTH-SENSOR_SUPPORT_BAR_WIDTH*WALL_THICKNESS, 3*WALL_THICKNESS, CO2_HEIGHT]);
    }
}

// BOX
translate([BOX_X_OUTER + 10, 0, 0]) // translate where you want it
    rotate([270, 0, 0]) // 2: rotate
        translate([WALL_THICKNESS, -BOX_Y_OUTER + WALL_THICKNESS, WALL_THICKNESS]) // 1. bring to origin 
            box();

// CAP
translate([0, BOX_Z_OUTER, 0]) // 3. translate where you want it
    rotate([90, 0, 0]) // 2. rotate
        translate([WALL_THICKNESS,WALL_THICKNESS,WALL_THICKNESS]) // 1. bring to origin
            cap();

//display_hole();
//cap();
//box();
//wemos_bar_right();
//usb_hole();