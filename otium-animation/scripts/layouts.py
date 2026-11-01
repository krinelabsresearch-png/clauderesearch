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
    "reel": dict(
        src="flyer_reel.png", layers="layers_reel", size=(941, 1672), paper=(251, 198, 197),
        out_prefix="OTIUM_reel",
        formats={"9x16": dict(H=1672, out=(1080, 1920))},
        boxes=dict(logo=(30, 90, 915, 345), atv=(40, 340, 480, 410), line=(478, 370, 665, 386),
                   sstar=(660, 335, 745, 418), fir=(740, 355, 915, 402), dom=(45, 1325, 330, 1382),
                   date=(25, 1380, 345, 1520), bstar=(350, 1355, 465, 1480), time=(480, 1328, 910, 1402),
                   genres=(482, 1402, 918, 1435), cta=(482, 1438, 915, 1497)),
        um_cut=(645, 680),
        photo_rows=(392, 1312),
        ball=dict(cx=461.0, cy=744.0, r=114.0, rx=114.0, ry=122.0),
        ball2=dict(cx=461.0, cy=889.0, r=54.0, rx=54.0, ry=58.0),
        lights=[(252, 622), (305, 622), (358, 624), (412, 626), (462, 612), (512, 626), (562, 624),
                (612, 622), (662, 622)],
        depth=dict(crowd=(1050, 1290), side_c=470, side=(320, 150), truss=(230, 430, 700, 640),
                   pillars=[(60, 130), (805, 872)], pill_ymax=1080),
        palmL=[(0, 865), (100, 880), (135, 975), (85, 1050), (0, 1050)],
        palmR=[(800, 890), (941, 875), (941, 1070), (810, 1070), (790, 1000)],
        trunkL=(40, 1050), trunkR=(880, 1065), sway_r=170,
        crowd_y=1065, zoom_c=(461.0, 625.0), spots_ymax=1045,
    ),
}
