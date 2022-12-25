from app.database.database import db
from app.stock_comparison import BestStocks
import datetime
from app.config import AppConfig
from bson import ObjectId, json_util
import json

dt = datetime.datetime.now().strftime("%y%m%d")

sample_data = [
  {
    "stock": "NESTLEIND.NS",
    "predictions": {
      "day1": {
        "prediction": 20262.62,
        "profit/loss": "profit",
        "diff": 129.869140625
      },
      "day2": {
        "prediction": 20303.232,
        "profit/loss": "profit",
        "diff": 170.482421875
      },
      "day3": {
        "prediction": 20328.178,
        "profit/loss": "profit",
        "diff": 195.427734375
      },
      "day4": {
        "prediction": 20346.723,
        "profit/loss": "profit",
        "diff": 213.97265625
      },
      "day5": {
        "prediction": 20361.28,
        "profit/loss": "profit",
        "diff": 228.529296875
      },
      "day6": {
        "prediction": 20373.006,
        "profit/loss": "profit",
        "diff": 240.255859375
      },
      "previous_close": 20132.75,
      "date": "221225"
    }
  },
  {
    "stock": "SUNPHARMA.NS",
    "predictions": {
      "day1": {
        "prediction": 1007.34283,
        "profit/loss": "profit",
        "diff": 5.7928466796875
      },
      "day2": {
        "prediction": 1006.25006,
        "profit/loss": "profit",
        "diff": 4.7000732421875
      },
      "day3": {
        "prediction": 1007.94116,
        "profit/loss": "profit",
        "diff": 6.39117431640625
      },
      "day4": {
        "prediction": 1009.3056,
        "profit/loss": "profit",
        "diff": 7.755615234375
      },
      "day5": {
        "prediction": 1009.6665,
        "profit/loss": "profit",
        "diff": 8.11651611328125
      },
      "day6": {
        "prediction": 1009.67725,
        "profit/loss": "profit",
        "diff": 8.12725830078125
      },
      "previous_close": 1001.5499877929688,
      "date": "221225"
    }
  },
  {
    "stock": "ITC.NS",
    "predictions": {
      "day1": {
        "prediction": 334.22867,
        "profit/loss": "profit",
        "diff": 7.528656005859375
      },
      "day2": {
        "prediction": 333.32074,
        "profit/loss": "profit",
        "diff": 6.6207275390625
      },
      "day3": {
        "prediction": 334.25183,
        "profit/loss": "profit",
        "diff": 7.55181884765625
      },
      "day4": {
        "prediction": 335.96204,
        "profit/loss": "profit",
        "diff": 9.26202392578125
      },
      "day5": {
        "prediction": 337.3251,
        "profit/loss": "profit",
        "diff": 10.625091552734375
      },
      "day6": {
        "prediction": 338.24875,
        "profit/loss": "profit",
        "diff": 11.548736572265625
      },
      "previous_close": 326.70001220703125,
      "date": "221225"
    }
  },
  {
    "stock": "DRREDDY.NS",
    "predictions": {
      "day1": {
        "prediction": 4366.8223,
        "profit/loss": "profit",
        "diff": 56.3720703125
      },
      "day2": {
        "prediction": 4367.4937,
        "profit/loss": "profit",
        "diff": 57.04345703125
      },
      "day3": {
        "prediction": 4384.809,
        "profit/loss": "profit",
        "diff": 74.35888671875
      },
      "day4": {
        "prediction": 4400.001,
        "profit/loss": "profit",
        "diff": 89.55078125
      },
      "day5": {
        "prediction": 4413.9062,
        "profit/loss": "profit",
        "diff": 103.4560546875
      },
      "day6": {
        "prediction": 4425.2783,
        "profit/loss": "profit",
        "diff": 114.828125
      },
      "previous_close": 4310.4501953125,
      "date": "221225"
    }
  },
  {
    "stock": "TITAN.NS",
    "predictions": {
      "day1": {
        "prediction": 2489.1135,
        "profit/loss": "profit",
        "diff": 6.0634765625
      },
      "day2": {
        "prediction": 2480.8984,
        "profit/loss": "loss",
        "diff": -2.151611328125
      },
      "day3": {
        "prediction": 2479.1453,
        "profit/loss": "loss",
        "diff": -3.90478515625
      },
      "day4": {
        "prediction": 2479.6924,
        "profit/loss": "loss",
        "diff": -3.357666015625
      },
      "day5": {
        "prediction": 2478.9646,
        "profit/loss": "loss",
        "diff": -4.08544921875
      },
      "day6": {
        "prediction": 2476.2449,
        "profit/loss": "loss",
        "diff": -6.80517578125
      },
      "previous_close": 2483.050048828125,
      "date": "221225"
    }
  },
  {
    "stock": "EICHERMOT.NS",
    "predictions": {
      "day1": {
        "prediction": 3221.9543,
        "profit/loss": "profit",
        "diff": 108.304443359375
      },
      "day2": {
        "prediction": 3208.6016,
        "profit/loss": "profit",
        "diff": 94.95166015625
      },
      "day3": {
        "prediction": 3230.7454,
        "profit/loss": "profit",
        "diff": 117.095458984375
      },
      "day4": {
        "prediction": 3278.1174,
        "profit/loss": "profit",
        "diff": 164.467529296875
      },
      "day5": {
        "prediction": 3337.8176,
        "profit/loss": "profit",
        "diff": 224.167724609375
      },
      "day6": {
        "prediction": 3400.2935,
        "profit/loss": "profit",
        "diff": 286.6435546875
      },
      "previous_close": 3113.64990234375,
      "date": "221225"
    }
  },
  {
    "stock": "SBIN.NS",
    "predictions": {
      "day1": {
        "prediction": 583.5503,
        "profit/loss": "profit",
        "diff": 9.55029296875
      },
      "day2": {
        "prediction": 588.1173,
        "profit/loss": "profit",
        "diff": 14.1173095703125
      },
      "day3": {
        "prediction": 590.59033,
        "profit/loss": "profit",
        "diff": 16.59033203125
      },
      "day4": {
        "prediction": 593.6084,
        "profit/loss": "profit",
        "diff": 19.6083984375
      },
      "day5": {
        "prediction": 596.83795,
        "profit/loss": "profit",
        "diff": 22.83795166015625
      },
      "day6": {
        "prediction": 599.8045,
        "profit/loss": "profit",
        "diff": 25.80450439453125
      },
      "previous_close": 574.0,
      "date": "221225"
    }
  },
  {
    "stock": "BPCL.NS",
    "predictions": {
      "day1": {
        "prediction": 328.81528,
        "profit/loss": "profit",
        "diff": 3.71527099609375
      },
      "day2": {
        "prediction": 329.92545,
        "profit/loss": "profit",
        "diff": 4.825439453125
      },
      "day3": {
        "prediction": 330.59415,
        "profit/loss": "profit",
        "diff": 5.494140625
      },
      "day4": {
        "prediction": 331.34705,
        "profit/loss": "profit",
        "diff": 6.247039794921875
      },
      "day5": {
        "prediction": 332.08295,
        "profit/loss": "profit",
        "diff": 6.982940673828125
      },
      "day6": {
        "prediction": 332.76834,
        "profit/loss": "profit",
        "diff": 7.6683349609375
      },
      "previous_close": 325.1000061035156,
      "date": "221225"
    }
  },
  {
    "stock": "INDUSINDBK.NS",
    "predictions": {
      "day1": {
        "prediction": 1176.9142,
        "profit/loss": "profit",
        "diff": 29.064208984375
      },
      "day2": {
        "prediction": 1169.9224,
        "profit/loss": "profit",
        "diff": 22.0723876953125
      },
      "day3": {
        "prediction": 1170.552,
        "profit/loss": "profit",
        "diff": 22.7020263671875
      },
      "day4": {
        "prediction": 1172.9178,
        "profit/loss": "profit",
        "diff": 25.06787109375
      },
      "day5": {
        "prediction": 1176.2847,
        "profit/loss": "profit",
        "diff": 28.4346923828125
      },
      "day6": {
        "prediction": 1180.0708,
        "profit/loss": "profit",
        "diff": 32.2208251953125
      },
      "previous_close": 1147.8499755859375,
      "date": "221225"
    }
  },
  {
    "stock": "HDFCBANK.NS",
    "predictions": {
      "day1": {
        "prediction": 1623.2689,
        "profit/loss": "profit",
        "diff": 25.618896484375
      },
      "day2": {
        "prediction": 1622.1704,
        "profit/loss": "profit",
        "diff": 24.5203857421875
      },
      "day3": {
        "prediction": 1626.0607,
        "profit/loss": "profit",
        "diff": 28.41064453125
      },
      "day4": {
        "prediction": 1631.765,
        "profit/loss": "profit",
        "diff": 34.114990234375
      },
      "day5": {
        "prediction": 1637.7434,
        "profit/loss": "profit",
        "diff": 40.0933837890625
      },
      "day6": {
        "prediction": 1643.4158,
        "profit/loss": "profit",
        "diff": 45.7657470703125
      },
      "previous_close": 1597.6500244140625,
      "date": "221225"
    }
  },
  {
    "stock": "HINDUNILVR.NS",
    "predictions": {
      "day1": {
        "prediction": 2643.6626,
        "profit/loss": "profit",
        "diff": 22.5625
      },
      "day2": {
        "prediction": 2633.3804,
        "profit/loss": "profit",
        "diff": 12.2802734375
      },
      "day3": {
        "prediction": 2629.9438,
        "profit/loss": "profit",
        "diff": 8.84375
      },
      "day4": {
        "prediction": 2631.1597,
        "profit/loss": "profit",
        "diff": 10.0595703125
      },
      "day5": {
        "prediction": 2634.0928,
        "profit/loss": "profit",
        "diff": 12.99267578125
      },
      "day6": {
        "prediction": 2636.9807,
        "profit/loss": "profit",
        "diff": 15.880615234375
      },
      "previous_close": 2621.10009765625,
      "date": "221225"
    }
  },
  {
    "stock": "HDFCLIFE.NS",
    "predictions": {
      "day1": {
        "prediction": 569.63904,
        "profit/loss": "profit",
        "diff": 4.18902587890625
      },
      "day2": {
        "prediction": 567.92664,
        "profit/loss": "profit",
        "diff": 2.47662353515625
      },
      "day3": {
        "prediction": 567.375,
        "profit/loss": "profit",
        "diff": 1.92498779296875
      },
      "day4": {
        "prediction": 566.89417,
        "profit/loss": "profit",
        "diff": 1.44415283203125
      },
      "day5": {
        "prediction": 566.3355,
        "profit/loss": "profit",
        "diff": 0.885498046875
      },
      "day6": {
        "prediction": 565.71783,
        "profit/loss": "profit",
        "diff": 0.267822265625
      },
      "previous_close": 565.4500122070312,
      "date": "221225"
    }
  },
  {
    "stock": "BRITANNIA.NS",
    "predictions": {
      "day1": {
        "prediction": 4405.3647,
        "profit/loss": "profit",
        "diff": 73.46484375
      },
      "day2": {
        "prediction": 4400.744,
        "profit/loss": "profit",
        "diff": 68.84423828125
      },
      "day3": {
        "prediction": 4400.0386,
        "profit/loss": "profit",
        "diff": 68.138671875
      },
      "day4": {
        "prediction": 4389.7114,
        "profit/loss": "profit",
        "diff": 57.8115234375
      },
      "day5": {
        "prediction": 4379.1523,
        "profit/loss": "profit",
        "diff": 47.25244140625
      },
      "day6": {
        "prediction": 4374.9937,
        "profit/loss": "profit",
        "diff": 43.09375
      },
      "previous_close": 4331.89990234375,
      "date": "221225"
    }
  },
  {
    "stock": "HDFC.NS",
    "predictions": {
      "day1": {
        "prediction": 2659.9197,
        "profit/loss": "profit",
        "diff": 36.86962890625
      },
      "day2": {
        "prediction": 2663.2122,
        "profit/loss": "profit",
        "diff": 40.162109375
      },
      "day3": {
        "prediction": 2668.0996,
        "profit/loss": "profit",
        "diff": 45.049560546875
      },
      "day4": {
        "prediction": 2670.9836,
        "profit/loss": "profit",
        "diff": 47.93359375
      },
      "day5": {
        "prediction": 2673.1685,
        "profit/loss": "profit",
        "diff": 50.118408203125
      },
      "day6": {
        "prediction": 2675.5427,
        "profit/loss": "profit",
        "diff": 52.49267578125
      },
      "previous_close": 2623.050048828125,
      "date": "221225"
    }
  },
  {
    "stock": "BHARTIARTL.NS",
    "predictions": {
      "day1": {
        "prediction": 813.10175,
        "profit/loss": "profit",
        "diff": 4.45172119140625
      },
      "day2": {
        "prediction": 814.5488,
        "profit/loss": "profit",
        "diff": 5.8988037109375
      },
      "day3": {
        "prediction": 815.6956,
        "profit/loss": "profit",
        "diff": 7.04559326171875
      },
      "day4": {
        "prediction": 816.3908,
        "profit/loss": "profit",
        "diff": 7.74078369140625
      },
      "day5": {
        "prediction": 816.7376,
        "profit/loss": "profit",
        "diff": 8.08758544921875
      },
      "day6": {
        "prediction": 816.8671,
        "profit/loss": "profit",
        "diff": 8.21710205078125
      },
      "previous_close": 808.6500244140625,
      "date": "221225"
    }
  },
  {
    "stock": "ASIANPAINT.NS",
    "predictions": {
      "day1": {
        "prediction": 3102.6396,
        "profit/loss": "profit",
        "diff": 44.73974609375
      },
      "day2": {
        "prediction": 3105.369,
        "profit/loss": "profit",
        "diff": 47.468994140625
      },
      "day3": {
        "prediction": 3108.467,
        "profit/loss": "profit",
        "diff": 50.567138671875
      },
      "day4": {
        "prediction": 3110.4233,
        "profit/loss": "profit",
        "diff": 52.5234375
      },
      "day5": {
        "prediction": 3110.525,
        "profit/loss": "profit",
        "diff": 52.625
      },
      "day6": {
        "prediction": 3109.0254,
        "profit/loss": "profit",
        "diff": 51.12548828125
      },
      "previous_close": 3057.89990234375,
      "date": "221225"
    }
  },
  {
    "stock": "SBILIFE.NS",
    "predictions": {
      "day1": {
        "prediction": 1236.361,
        "profit/loss": "profit",
        "diff": 11.760986328125
      },
      "day2": {
        "prediction": 1235.6652,
        "profit/loss": "profit",
        "diff": 11.065185546875
      },
      "day3": {
        "prediction": 1236.8584,
        "profit/loss": "profit",
        "diff": 12.2584228515625
      },
      "day4": {
        "prediction": 1238.2281,
        "profit/loss": "profit",
        "diff": 13.628173828125
      },
      "day5": {
        "prediction": 1239.3142,
        "profit/loss": "profit",
        "diff": 14.7142333984375
      },
      "day6": {
        "prediction": 1240.125,
        "profit/loss": "profit",
        "diff": 15.5250244140625
      },
      "previous_close": 1224.5999755859375,
      "date": "221225"
    }
  },
  {
    "stock": "HEROMOTOCO.NS",
    "predictions": {
      "day1": {
        "prediction": 2674.3882,
        "profit/loss": "profit",
        "diff": 37.5380859375
      },
      "day2": {
        "prediction": 2667.0564,
        "profit/loss": "profit",
        "diff": 30.206298828125
      },
      "day3": {
        "prediction": 2666.9526,
        "profit/loss": "profit",
        "diff": 30.1025390625
      },
      "day4": {
        "prediction": 2666.806,
        "profit/loss": "profit",
        "diff": 29.955810546875
      },
      "day5": {
        "prediction": 2667.1814,
        "profit/loss": "profit",
        "diff": 30.331298828125
      },
      "day6": {
        "prediction": 2668.2263,
        "profit/loss": "profit",
        "diff": 31.376220703125
      },
      "previous_close": 2636.85009765625,
      "date": "221225"
    }
  },
  {
    "stock": "ICICIBANK.NS",
    "predictions": {
      "day1": {
        "prediction": 883.8209,
        "profit/loss": "profit",
        "diff": 4.9208984375
      },
      "day2": {
        "prediction": 883.4835,
        "profit/loss": "profit",
        "diff": 4.58349609375
      },
      "day3": {
        "prediction": 884.79297,
        "profit/loss": "profit",
        "diff": 5.8929443359375
      },
      "day4": {
        "prediction": 886.0768,
        "profit/loss": "profit",
        "diff": 7.1767578125
      },
      "day5": {
        "prediction": 886.75616,
        "profit/loss": "profit",
        "diff": 7.85614013671875
      },
      "day6": {
        "prediction": 886.94244,
        "profit/loss": "profit",
        "diff": 8.04241943359375
      },
      "previous_close": 878.9000244140625,
      "date": "221225"
    }
  },
  {
    "stock": "CIPLA.NS",
    "predictions": {
      "day1": {
        "prediction": 1123.478,
        "profit/loss": "profit",
        "diff": 4.3280029296875
      },
      "day2": {
        "prediction": 1122.6407,
        "profit/loss": "profit",
        "diff": 3.49072265625
      },
      "day3": {
        "prediction": 1121.0869,
        "profit/loss": "profit",
        "diff": 1.9368896484375
      },
      "day4": {
        "prediction": 1119.584,
        "profit/loss": "profit",
        "diff": 0.4339599609375
      },
      "day5": {
        "prediction": 1118.3452,
        "profit/loss": "loss",
        "diff": -0.8048095703125
      },
      "day6": {
        "prediction": 1117.4059,
        "profit/loss": "loss",
        "diff": -1.744140625
      },
      "previous_close": 1119.1500244140625,
      "date": "221225"
    }
  },
  {
    "stock": "TATACONSUM.NS",
    "predictions": {
      "day1": {
        "prediction": 795.2945,
        "profit/loss": "profit",
        "diff": 16.29449462890625
      },
      "day2": {
        "prediction": 793.68976,
        "profit/loss": "profit",
        "diff": 14.68975830078125
      },
      "day3": {
        "prediction": 793.8085,
        "profit/loss": "profit",
        "diff": 14.8084716796875
      },
      "day4": {
        "prediction": 793.74457,
        "profit/loss": "profit",
        "diff": 14.74456787109375
      },
      "day5": {
        "prediction": 792.9791,
        "profit/loss": "profit",
        "diff": 13.9791259765625
      },
      "day6": {
        "prediction": 792.0873,
        "profit/loss": "profit",
        "diff": 13.0872802734375
      },
      "previous_close": 779.0,
      "date": "221225"
    }
  },
  {
    "stock": "POWERGRID.NS",
    "predictions": {
      "day1": {
        "prediction": 213.07951,
        "profit/loss": "profit",
        "diff": 1.8295135498046875
      },
      "day2": {
        "prediction": 213.1502,
        "profit/loss": "profit",
        "diff": 1.90020751953125
      },
      "day3": {
        "prediction": 213.3605,
        "profit/loss": "profit",
        "diff": 2.110504150390625
      },
      "day4": {
        "prediction": 213.5807,
        "profit/loss": "profit",
        "diff": 2.3307037353515625
      },
      "day5": {
        "prediction": 213.69984,
        "profit/loss": "profit",
        "diff": 2.4498443603515625
      },
      "day6": {
        "prediction": 213.72438,
        "profit/loss": "profit",
        "diff": 2.4743804931640625
      },
      "previous_close": 211.25,
      "date": "221225"
    }
  },
  {
    "stock": "DIVISLAB.NS",
    "predictions": {
      "day1": {
        "prediction": 3531.1472,
        "profit/loss": "profit",
        "diff": 32.697265625
      },
      "day2": {
        "prediction": 3556.321,
        "profit/loss": "profit",
        "diff": 57.87109375
      },
      "day3": {
        "prediction": 3565.2444,
        "profit/loss": "profit",
        "diff": 66.79443359375
      },
      "day4": {
        "prediction": 3565.7366,
        "profit/loss": "profit",
        "diff": 67.28662109375
      },
      "day5": {
        "prediction": 3562.654,
        "profit/loss": "profit",
        "diff": 64.2041015625
      },
      "day6": {
        "prediction": 3558.7104,
        "profit/loss": "profit",
        "diff": 60.260498046875
      },
      "previous_close": 3498.449951171875,
      "date": "221225"
    }
  },
  {
    "stock": "ADANIPORTS.NS",
    "predictions": {
      "day1": {
        "prediction": 839.34784,
        "profit/loss": "profit",
        "diff": 45.24786376953125
      },
      "day2": {
        "prediction": 834.9073,
        "profit/loss": "profit",
        "diff": 40.80731201171875
      },
      "day3": {
        "prediction": 840.26263,
        "profit/loss": "profit",
        "diff": 46.16265869140625
      },
      "day4": {
        "prediction": 846.7485,
        "profit/loss": "profit",
        "diff": 52.64849853515625
      },
      "day5": {
        "prediction": 851.3414,
        "profit/loss": "profit",
        "diff": 57.24139404296875
      },
      "day6": {
        "prediction": 853.6538,
        "profit/loss": "profit",
        "diff": 59.5538330078125
      },
      "previous_close": 794.0999755859375,
      "date": "221225"
    }
  },
  {
    "stock": "KOTAKBANK.NS",
    "predictions": {
      "day1": {
        "prediction": 1837.1263,
        "profit/loss": "profit",
        "diff": 15.1763916015625
      },
      "day2": {
        "prediction": 1838.0645,
        "profit/loss": "profit",
        "diff": 16.114501953125
      },
      "day3": {
        "prediction": 1845.7924,
        "profit/loss": "profit",
        "diff": 23.8424072265625
      },
      "day4": {
        "prediction": 1854.8395,
        "profit/loss": "profit",
        "diff": 32.8895263671875
      },
      "day5": {
        "prediction": 1861.98,
        "profit/loss": "profit",
        "diff": 40.030029296875
      },
      "day6": {
        "prediction": 1867.1075,
        "profit/loss": "profit",
        "diff": 45.1575927734375
      },
      "previous_close": 1821.949951171875,
      "date": "221225"
    }
  },
  {
    "stock": "BAJAJ-AUTO.NS",
    "predictions": {
      "day1": {
        "prediction": 3588.6865,
        "profit/loss": "profit",
        "diff": 46.886474609375
      },
      "day2": {
        "prediction": 3576.9058,
        "profit/loss": "profit",
        "diff": 35.105712890625
      },
      "day3": {
        "prediction": 3575.2324,
        "profit/loss": "profit",
        "diff": 33.432373046875
      },
      "day4": {
        "prediction": 3578.0676,
        "profit/loss": "profit",
        "diff": 36.267578125
      },
      "day5": {
        "prediction": 3581.2744,
        "profit/loss": "profit",
        "diff": 39.474365234375
      },
      "day6": {
        "prediction": 3583.7434,
        "profit/loss": "profit",
        "diff": 41.943359375
      },
      "previous_close": 3541.800048828125,
      "date": "221225"
    }
  },
  {
    "stock": "JSWSTEEL.NS",
    "predictions": {
      "day1": {
        "prediction": 742.032,
        "profit/loss": "profit",
        "diff": 14.1820068359375
      },
      "day2": {
        "prediction": 741.98926,
        "profit/loss": "profit",
        "diff": 14.1392822265625
      },
      "day3": {
        "prediction": 743.0303,
        "profit/loss": "profit",
        "diff": 15.1802978515625
      },
      "day4": {
        "prediction": 743.91583,
        "profit/loss": "profit",
        "diff": 16.06585693359375
      },
      "day5": {
        "prediction": 744.4854,
        "profit/loss": "profit",
        "diff": 16.63543701171875
      },
      "day6": {
        "prediction": 744.79364,
        "profit/loss": "profit",
        "diff": 16.94366455078125
      },
      "previous_close": 727.8499755859375,
      "date": "221225"
    }
  },
  {
    "stock": "APOLLOHOSP.NS",
    "predictions": {
      "day1": {
        "prediction": 4717.9443,
        "profit/loss": "profit",
        "diff": 17.79443359375
      },
      "day2": {
        "prediction": 4718.08,
        "profit/loss": "profit",
        "diff": 17.93017578125
      },
      "day3": {
        "prediction": 4716.846,
        "profit/loss": "profit",
        "diff": 16.6962890625
      },
      "day4": {
        "prediction": 4716.099,
        "profit/loss": "profit",
        "diff": 15.94921875
      },
      "day5": {
        "prediction": 4713.597,
        "profit/loss": "profit",
        "diff": 13.447265625
      },
      "day6": {
        "prediction": 4708.6167,
        "profit/loss": "profit",
        "diff": 8.466796875
      },
      "previous_close": 4700.14990234375,
      "date": "221225"
    }
  },
  {
    "stock": "COALINDIA.NS",
    "predictions": {
      "day1": {
        "prediction": 219.47542,
        "profit/loss": "profit",
        "diff": 4.4254150390625
      },
      "day2": {
        "prediction": 219.1408,
        "profit/loss": "profit",
        "diff": 4.090789794921875
      },
      "day3": {
        "prediction": 219.54889,
        "profit/loss": "profit",
        "diff": 4.4988861083984375
      },
      "day4": {
        "prediction": 220.07333,
        "profit/loss": "profit",
        "diff": 5.0233306884765625
      },
      "day5": {
        "prediction": 220.54704,
        "profit/loss": "profit",
        "diff": 5.497039794921875
      },
      "day6": {
        "prediction": 220.93765,
        "profit/loss": "profit",
        "diff": 5.8876495361328125
      },
      "previous_close": 215.0500030517578,
      "date": "221225"
    }
  },
  {
    "stock": "GRASIM.NS",
    "predictions": {
      "day1": {
        "prediction": 1725.3628,
        "profit/loss": "profit",
        "diff": 16.2628173828125
      },
      "day2": {
        "prediction": 1720.4438,
        "profit/loss": "profit",
        "diff": 11.3438720703125
      },
      "day3": {
        "prediction": 1719.2021,
        "profit/loss": "profit",
        "diff": 10.1021728515625
      },
      "day4": {
        "prediction": 1719.3519,
        "profit/loss": "profit",
        "diff": 10.251953125
      },
      "day5": {
        "prediction": 1719.6127,
        "profit/loss": "profit",
        "diff": 10.5126953125
      },
      "day6": {
        "prediction": 1719.339,
        "profit/loss": "profit",
        "diff": 10.239013671875
      },
      "previous_close": 1709.0999755859375,
      "date": "221225"
    }
  },
  {
    "stock": "NTPC.NS",
    "predictions": {
      "day1": {
        "prediction": 164.40274,
        "profit/loss": "profit",
        "diff": 1.402740478515625
      },
      "day2": {
        "prediction": 165.1991,
        "profit/loss": "profit",
        "diff": 2.1990966796875
      },
      "day3": {
        "prediction": 165.58588,
        "profit/loss": "profit",
        "diff": 2.58587646484375
      },
      "day4": {
        "prediction": 165.87321,
        "profit/loss": "profit",
        "diff": 2.8732147216796875
      },
      "day5": {
        "prediction": 166.02771,
        "profit/loss": "profit",
        "diff": 3.0277099609375
      },
      "day6": {
        "prediction": 166.07397,
        "profit/loss": "profit",
        "diff": 3.073974609375
      },
      "previous_close": 163.0,
      "date": "221225"
    }
  },
  {
    "stock": "M&M.NS",
    "predictions": {
      "day1": {
        "prediction": 1248.3481,
        "profit/loss": "profit",
        "diff": 23.7481689453125
      },
      "day2": {
        "prediction": 1243.5885,
        "profit/loss": "profit",
        "diff": 18.988525390625
      },
      "day3": {
        "prediction": 1247.5824,
        "profit/loss": "profit",
        "diff": 22.982421875
      },
      "day4": {
        "prediction": 1255.0248,
        "profit/loss": "profit",
        "diff": 30.4248046875
      },
      "day5": {
        "prediction": 1261.75,
        "profit/loss": "profit",
        "diff": 37.1500244140625
      },
      "day6": {
        "prediction": 1267.0546,
        "profit/loss": "profit",
        "diff": 42.45458984375
      },
      "previous_close": 1224.5999755859375,
      "date": "221225"
    }
  },
  {
    "stock": "ADANIENT.NS",
    "predictions": {
      "day1": {
        "prediction": 4004.7234,
        "profit/loss": "profit",
        "diff": 362.5234375
      },
      "day2": {
        "prediction": 3986.5266,
        "profit/loss": "profit",
        "diff": 344.32666015625
      },
      "day3": {
        "prediction": 3988.631,
        "profit/loss": "profit",
        "diff": 346.43115234375
      },
      "day4": {
        "prediction": 4006.5996,
        "profit/loss": "profit",
        "diff": 364.399658203125
      },
      "day5": {
        "prediction": 4026.389,
        "profit/loss": "profit",
        "diff": 384.18896484375
      },
      "day6": {
        "prediction": 4045.8953,
        "profit/loss": "profit",
        "diff": 403.6953125
      },
      "previous_close": 3642.199951171875,
      "date": "221225"
    }
  },
  {
    "stock": "LT.NS",
    "predictions": {
      "day1": {
        "prediction": 2088.175,
        "profit/loss": "profit",
        "diff": 25.425048828125
      },
      "day2": {
        "prediction": 2094.6738,
        "profit/loss": "profit",
        "diff": 31.923828125
      },
      "day3": {
        "prediction": 2101.868,
        "profit/loss": "profit",
        "diff": 39.117919921875
      },
      "day4": {
        "prediction": 2102.6956,
        "profit/loss": "profit",
        "diff": 39.945556640625
      },
      "day5": {
        "prediction": 2102.4233,
        "profit/loss": "profit",
        "diff": 39.67333984375
      },
      "day6": {
        "prediction": 2102.8157,
        "profit/loss": "profit",
        "diff": 40.065673828125
      },
      "previous_close": 2062.75,
      "date": "221225"
    }
  },
  {
    "stock": "MARUTI.NS",
    "predictions": {
      "day1": {
        "prediction": 8373.89,
        "profit/loss": "profit",
        "diff": 232.28955078125
      },
      "day2": {
        "prediction": 8336.675,
        "profit/loss": "profit",
        "diff": 195.07470703125
      },
      "day3": {
        "prediction": 8345.469,
        "profit/loss": "profit",
        "diff": 203.86865234375
      },
      "day4": {
        "prediction": 8384.612,
        "profit/loss": "profit",
        "diff": 243.01220703125
      },
      "day5": {
        "prediction": 8433.69,
        "profit/loss": "profit",
        "diff": 292.09033203125
      },
      "day6": {
        "prediction": 8478.233,
        "profit/loss": "profit",
        "diff": 336.63330078125
      },
      "previous_close": 8141.60009765625,
      "date": "221225"
    }
  },
  {
    "stock": "AXISBANK.NS",
    "predictions": {
      "day1": {
        "prediction": 921.27673,
        "profit/loss": "profit",
        "diff": 14.6767578125
      },
      "day2": {
        "prediction": 923.8087,
        "profit/loss": "profit",
        "diff": 17.208740234375
      },
      "day3": {
        "prediction": 923.8485,
        "profit/loss": "profit",
        "diff": 17.24853515625
      },
      "day4": {
        "prediction": 923.05,
        "profit/loss": "profit",
        "diff": 16.45001220703125
      },
      "day5": {
        "prediction": 923.9466,
        "profit/loss": "profit",
        "diff": 17.34661865234375
      },
      "day6": {
        "prediction": 925.0982,
        "profit/loss": "profit",
        "diff": 18.49822998046875
      },
      "previous_close": 906.5999755859375,
      "date": "221225"
    }
  },
  {
    "stock": "TATAMOTORS.NS",
    "predictions": {
      "day1": {
        "prediction": 397.85846,
        "profit/loss": "profit",
        "diff": 19.508453369140625
      },
      "day2": {
        "prediction": 399.59222,
        "profit/loss": "profit",
        "diff": 21.242218017578125
      },
      "day3": {
        "prediction": 408.19162,
        "profit/loss": "profit",
        "diff": 29.84161376953125
      },
      "day4": {
        "prediction": 417.9133,
        "profit/loss": "profit",
        "diff": 39.56329345703125
      },
      "day5": {
        "prediction": 425.38852,
        "profit/loss": "profit",
        "diff": 47.03851318359375
      },
      "day6": {
        "prediction": 429.14374,
        "profit/loss": "profit",
        "diff": 50.793731689453125
      },
      "previous_close": 378.3500061035156,
      "date": "221225"
    }
  },
  {
    "stock": "BAJFINANCE.NS",
    "predictions": {
      "day1": {
        "prediction": 6464.471,
        "profit/loss": "profit",
        "diff": 89.87109375
      },
      "day2": {
        "prediction": 6422.8594,
        "profit/loss": "profit",
        "diff": 48.25927734375
      },
      "day3": {
        "prediction": 6413.5703,
        "profit/loss": "profit",
        "diff": 38.97021484375
      },
      "day4": {
        "prediction": 6419.958,
        "profit/loss": "profit",
        "diff": 45.35791015625
      },
      "day5": {
        "prediction": 6428.005,
        "profit/loss": "profit",
        "diff": 53.40478515625
      },
      "day6": {
        "prediction": 6431.0684,
        "profit/loss": "profit",
        "diff": 56.46826171875
      },
      "previous_close": 6374.60009765625,
      "date": "221225"
    }
  },
  {
    "stock": "TATASTEEL.NS",
    "predictions": {
      "day1": {
        "prediction": 105.00694,
        "profit/loss": "profit",
        "diff": 2.7569427490234375
      },
      "day2": {
        "prediction": 104.55525,
        "profit/loss": "profit",
        "diff": 2.3052520751953125
      },
      "day3": {
        "prediction": 104.69176,
        "profit/loss": "profit",
        "diff": 2.4417572021484375
      },
      "day4": {
        "prediction": 105.265015,
        "profit/loss": "profit",
        "diff": 3.0150146484375
      },
      "day5": {
        "prediction": 105.83499,
        "profit/loss": "profit",
        "diff": 3.584991455078125
      },
      "day6": {
        "prediction": 106.36005,
        "profit/loss": "profit",
        "diff": 4.11004638671875
      },
      "previous_close": 102.25,
      "date": "221225"
    }
  },
  {
    "stock": "BAJAJFINSV.NS",
    "predictions": {
      "day1": {
        "prediction": 1517.8296,
        "profit/loss": "profit",
        "diff": 20.779541015625
      },
      "day2": {
        "prediction": 1513.4537,
        "profit/loss": "profit",
        "diff": 16.4036865234375
      },
      "day3": {
        "prediction": 1514.5039,
        "profit/loss": "profit",
        "diff": 17.453857421875
      },
      "day4": {
        "prediction": 1519.0826,
        "profit/loss": "profit",
        "diff": 22.0325927734375
      },
      "day5": {
        "prediction": 1525.7844,
        "profit/loss": "profit",
        "diff": 28.734375
      },
      "day6": {
        "prediction": 1532.4109,
        "profit/loss": "profit",
        "diff": 35.36083984375
      },
      "previous_close": 1497.050048828125,
      "date": "221225"
    }
  },
  {
    "stock": "RELIANCE.NS",
    "predictions": {
      "day1": {
        "prediction": 2551.9253,
        "profit/loss": "profit",
        "diff": 49.725341796875
      },
      "day2": {
        "prediction": 2546.4365,
        "profit/loss": "profit",
        "diff": 44.236572265625
      },
      "day3": {
        "prediction": 2558.3835,
        "profit/loss": "profit",
        "diff": 56.18359375
      },
      "day4": {
        "prediction": 2566.0977,
        "profit/loss": "profit",
        "diff": 63.897705078125
      },
      "day5": {
        "prediction": 2565.4758,
        "profit/loss": "profit",
        "diff": 63.27587890625
      },
      "day6": {
        "prediction": 2563.8794,
        "profit/loss": "profit",
        "diff": 61.679443359375
      },
      "previous_close": 2502.199951171875,
      "date": "221225"
    }
  },
  {
    "stock": "ONGC.NS",
    "predictions": {
      "day1": {
        "prediction": 139.98526,
        "profit/loss": "profit",
        "diff": 0.1852569580078125
      },
      "day2": {
        "prediction": 140.37834,
        "profit/loss": "profit",
        "diff": 0.578338623046875
      },
      "day3": {
        "prediction": 140.57664,
        "profit/loss": "profit",
        "diff": 0.776641845703125
      },
      "day4": {
        "prediction": 140.6507,
        "profit/loss": "profit",
        "diff": 0.8506927490234375
      },
      "day5": {
        "prediction": 140.74362,
        "profit/loss": "profit",
        "diff": 0.9436187744140625
      },
      "day6": {
        "prediction": 140.84416,
        "profit/loss": "profit",
        "diff": 1.044158935546875
      },
      "previous_close": 139.8000030517578,
      "date": "221225"
    }
  },
  {
    "stock": "ULTRACEMCO.NS",
    "predictions": {
      "day1": {
        "prediction": 7028.7925,
        "profit/loss": "profit",
        "diff": 119.392578125
      },
      "day2": {
        "prediction": 7043.481,
        "profit/loss": "profit",
        "diff": 134.0810546875
      },
      "day3": {
        "prediction": 7071.779,
        "profit/loss": "profit",
        "diff": 162.37890625
      },
      "day4": {
        "prediction": 7100.5815,
        "profit/loss": "profit",
        "diff": 191.181640625
      },
      "day5": {
        "prediction": 7126.5938,
        "profit/loss": "profit",
        "diff": 217.19384765625
      },
      "day6": {
        "prediction": 7150.372,
        "profit/loss": "profit",
        "diff": 240.97216796875
      },
      "previous_close": 6909.39990234375,
      "date": "221225"
    }
  },
  {
    "stock": "HINDALCO.NS",
    "predictions": {
      "day1": {
        "prediction": 439.89243,
        "profit/loss": "profit",
        "diff": 10.342437744140625
      },
      "day2": {
        "prediction": 445.32004,
        "profit/loss": "profit",
        "diff": 15.770050048828125
      },
      "day3": {
        "prediction": 445.47775,
        "profit/loss": "profit",
        "diff": 15.927764892578125
      },
      "day4": {
        "prediction": 443.97937,
        "profit/loss": "profit",
        "diff": 14.42938232421875
      },
      "day5": {
        "prediction": 443.46167,
        "profit/loss": "profit",
        "diff": 13.91168212890625
      },
      "day6": {
        "prediction": 443.397,
        "profit/loss": "profit",
        "diff": 13.847015380859375
      },
      "previous_close": 429.54998779296875,
      "date": "221225"
    }
  },
  {
    "stock": "UPL.NS",
    "predictions": {
      "day1": {
        "prediction": 725.5523,
        "profit/loss": "profit",
        "diff": 14.352294921875
      },
      "day2": {
        "prediction": 721.1854,
        "profit/loss": "profit",
        "diff": 9.98541259765625
      },
      "day3": {
        "prediction": 723.0611,
        "profit/loss": "profit",
        "diff": 11.861083984375
      },
      "day4": {
        "prediction": 726.4714,
        "profit/loss": "profit",
        "diff": 15.2713623046875
      },
      "day5": {
        "prediction": 729.9682,
        "profit/loss": "profit",
        "diff": 18.7681884765625
      },
      "day6": {
        "prediction": 733.18085,
        "profit/loss": "profit",
        "diff": 21.9808349609375
      },
      "previous_close": 711.2000122070312,
      "date": "221225"
    }
  },
  {
    "stock": "TCS.NS",
    "predictions": {
      "day1": {
        "prediction": 3250.5107,
        "profit/loss": "profit",
        "diff": 22.16064453125
      },
      "day2": {
        "prediction": 3253.8384,
        "profit/loss": "profit",
        "diff": 25.48828125
      },
      "day3": {
        "prediction": 3256.3674,
        "profit/loss": "profit",
        "diff": 28.017333984375
      },
      "day4": {
        "prediction": 3257.1829,
        "profit/loss": "profit",
        "diff": 28.832763671875
      },
      "day5": {
        "prediction": 3256.053,
        "profit/loss": "profit",
        "diff": 27.702880859375
      },
      "day6": {
        "prediction": 3253.1523,
        "profit/loss": "profit",
        "diff": 24.80224609375
      },
      "previous_close": 3228.35009765625,
      "date": "221225"
    }
  },
  {
    "stock": "WIPRO.NS",
    "predictions": {
      "day1": {
        "prediction": 383.74265,
        "profit/loss": "profit",
        "diff": 6.0926513671875
      },
      "day2": {
        "prediction": 381.98355,
        "profit/loss": "profit",
        "diff": 4.33355712890625
      },
      "day3": {
        "prediction": 382.224,
        "profit/loss": "profit",
        "diff": 4.574005126953125
      },
      "day4": {
        "prediction": 382.97244,
        "profit/loss": "profit",
        "diff": 5.32244873046875
      },
      "day5": {
        "prediction": 383.31415,
        "profit/loss": "profit",
        "diff": 5.664154052734375
      },
      "day6": {
        "prediction": 383.1336,
        "profit/loss": "profit",
        "diff": 5.483612060546875
      },
      "previous_close": 377.6499938964844,
      "date": "221225"
    }
  },
  {
    "stock": "INFY.NS",
    "predictions": {
      "day1": {
        "prediction": 1523.2026,
        "profit/loss": "profit",
        "diff": 26.1026611328125
      },
      "day2": {
        "prediction": 1526.3558,
        "profit/loss": "profit",
        "diff": 29.255859375
      },
      "day3": {
        "prediction": 1530.8994,
        "profit/loss": "profit",
        "diff": 33.7994384765625
      },
      "day4": {
        "prediction": 1535.1332,
        "profit/loss": "profit",
        "diff": 38.033203125
      },
      "day5": {
        "prediction": 1538.3092,
        "profit/loss": "profit",
        "diff": 41.209228515625
      },
      "day6": {
        "prediction": 1540.43,
        "profit/loss": "profit",
        "diff": 43.330078125
      },
      "previous_close": 1497.0999755859375,
      "date": "221225"
    }
  },
  {
    "stock": "TECHM.NS",
    "predictions": {
      "day1": {
        "prediction": 1010.401,
        "profit/loss": "profit",
        "diff": 14.6510009765625
      },
      "day2": {
        "prediction": 1005.6682,
        "profit/loss": "profit",
        "diff": 9.918212890625
      },
      "day3": {
        "prediction": 1003.3079,
        "profit/loss": "profit",
        "diff": 7.55792236328125
      },
      "day4": {
        "prediction": 1002.3208,
        "profit/loss": "profit",
        "diff": 6.57080078125
      },
      "day5": {
        "prediction": 1001.91406,
        "profit/loss": "profit",
        "diff": 6.1640625
      },
      "day6": {
        "prediction": 1001.688,
        "profit/loss": "profit",
        "diff": 5.93798828125
      },
      "previous_close": 995.75,
      "date": "221225"
    }
  },
  {
    "stock": "HCLTECH.NS",
    "predictions": {
      "day1": {
        "prediction": 1039.9806,
        "profit/loss": "profit",
        "diff": 9.380615234375
      },
      "day2": {
        "prediction": 1037.5746,
        "profit/loss": "profit",
        "diff": 6.974609375
      },
      "day3": {
        "prediction": 1036.2446,
        "profit/loss": "profit",
        "diff": 5.6446533203125
      },
      "day4": {
        "prediction": 1035.5042,
        "profit/loss": "profit",
        "diff": 4.9041748046875
      },
      "day5": {
        "prediction": 1034.9563,
        "profit/loss": "profit",
        "diff": 4.3563232421875
      },
      "day6": {
        "prediction": 1034.3495,
        "profit/loss": "profit",
        "diff": 3.74951171875
      },
      "previous_close": 1030.5999755859375,
      "date": "221225"
    }
  }
]



async def get_prediction_data(date: str = dt):
    bs = BestStocks(extended_model_path="models_221211/")
    p = sample_data
    # with open("app/Learningapp/best_stocks.json", "w") as f:
    #     json.dump(str(p), f, indent=4)
    return parse_json(p)


def parse_json(data):
    return json.loads(json_util.dumps(data))


async def insert_prediction_data(data: dict):
    await db["prediction"].insert_one(data)


def get_stock_comparison(config: AppConfig = AppConfig()) -> dict:
    bs = BestStocks(extended_model_path=config.model_path)
    p = bs.generate()
    data = {datetime.datetime.now().strftime("%y%m%d"): p}
    return data
