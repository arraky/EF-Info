BOX_X = 40;
BOX_Y = 40;
BOX_Z = 30;
BOX_WALL = 1.2;

// Interne Parameter
BOX_INNER_X = BOX_X - 2*BOX_WALL;
BOX_INNER_Y = BOX_Y - 2*BOX_WALL;

module txt() {
    translate([BOX_X / 2, 0.25 * BOX_WALL, BOX_Z / 2])
    rotate([90, 0, 0])
        linear_extrude(1)
            text("EF INFO", size=3, halign="center", valign="center");
}

module box() {
    difference() {
        cube([BOX_X, BOX_Y, BOX_Z]);
        translate([BOX_WALL, BOX_WALL, BOX_WALL])
            cube([BOX_INNER_X , BOX_INNER_Y, BOX_Z]);
        txt();
    }
}

module deckel() {
    union() {
        cube([BOX_X, BOX_Y, BOX_WALL]);
        translate([BOX_WALL, BOX_WALL, BOX_WALL])
            cube([BOX_INNER_X, BOX_INNER_Y, BOX_WALL]);
    }
}


box();
translate([BOX_X + 10, 0, 0])
    deckel();