"""Per-artwork layout data (all coordinates in the source image's own pixels).

Pick the artwork with the env var OTIUM_VARIANT ("feed" = 4:5 flyer, "reel" = 9:16 flyer).
Text pieces are found automatically inside each box; these numbers only say where to look
and where the photo elements (balls, lights, palms, crowd) sit.
"""

LAYOUTS = {
    # ------------------------------------------------------------- 4:5 flyer (1122 x 1402)
    "feed": dict(
        src="flyer.png", layers="layers", size=(1122, 1402), paper=(246, 200, 197),
        out_prefix="OTIUM",
        formats={"4x5": dict(H=1402, out=(1080, 1350)), "9x16": dict(H=1995, out=(1080, 1920))},
        boxes=dict(logo=(60, 20, 1062, 300), atv=(50, 296, 562, 368), line=(568, 328, 790, 340),
                   sstar=(782, 288, 880, 385), fir=(878, 310, 1072, 360), dom=(58, 1115, 390, 1178),
                   date=(30, 1176, 412, 1335), bstar=(415, 1145, 555, 1295), time=(570, 1115, 1068, 1202),
                   genres=(572, 1203, 1082, 1238), cta=(572, 1240, 1080, 1306)),
        um_cut=(740, 800),
        photo_rows=(338, 1114),
        ball=dict(cx=546.0, cy=665.0, r=123.0, rx=123.0, ry=123.0),
        ball2=dict(cx=544.0, cy=806.0, r=57.0, rx=57.0, ry=57.0),
        lights=[(318, 548), (382, 545), (435, 548), (494, 552), (547, 535), (602, 552), (656, 548),
                (709, 546), (766, 548)],
        depth=dict(crowd=(905, 1095), side_c=561, side=(380, 180), truss=(280, 380, 820, 570),
                   pillars=[(88, 162), (935, 1005)], pill_ymax=950),
        palmL=[(0, 712), (112, 730), (158, 830), (96, 905), (0, 905)],
        palmR=[(928, 772), (1122, 752), (1122, 936), (936, 936), (920, 880)],
        trunkL=(40, 905), trunkR=(1030, 940), sway_r=190,
        crowd_y=930, zoom_c=(546.0, 540.0), spots_ymax=930,
    ),
    # ------------------------------------------------------------- 9:16 reel flyer (941 x 1672)
    # v2: margins added on the sides, date block aligned with time / genres / CTA
    "reel": dict(
        src="flyer_reel.png", layers="layers_reel", size=(941, 1672), paper=(252, 195, 194),
        out_prefix="OTIUM_reel",
        formats={"9x16": dict(H=1672, out=(1080, 1920))},
        boxes=dict(logo=(95, 150, 850, 370), atv=(105, 362, 478, 420), line=(475, 385, 625, 401),
                   sstar=(622, 358, 695, 430), fir=(690, 372, 835, 418), dom=(85, 1345, 345, 1398),
                   date=(80, 1396, 355, 1500), bstar=(365, 1372, 472, 1485), time=(485, 1342, 860, 1412),
                   genres=(487, 1412, 872, 1444), cta=(487, 1444, 870, 1498)),
        um_cut=(618, 650),
        photo_rows=(424, 1318),
        ball=dict(cx=461.0, cy=772.0, r=114.0, rx=114.0, ry=122.0),
        ball2=dict(cx=461.0, cy=909.0, r=54.0, rx=54.0, ry=58.0),
        lights=[(252, 650), (305, 650), (358, 652), (412, 654), (462, 640), (512, 654), (562, 652),
                (612, 650), (662, 650)],
        depth=dict(crowd=(1065, 1300), side_c=470, side=(320, 150), truss=(230, 455, 700, 665),
                   pillars=[(60, 130), (805, 872)], pill_ymax=1100),
        palmL=[(0, 885), (100, 900), (135, 995), (85, 1072), (0, 1072)],
        palmR=[(800, 912), (941, 897), (941, 1090), (810, 1090), (790, 1020)],
        trunkL=(40, 1072), trunkR=(880, 1088), sway_r=170,
        crowd_y=1085, zoom_c=(461.0, 653.0), spots_ymax=1065,
    ),
}
