'''
pip install exifread
pip install itchat
'''

# 使用 exifread 获取图片的元数据
img_exif = exifread.process_file(open(self.img_path, 'rb'))

# 能够读取到属性
if img_exif:
     # 纬度数
     latitude_gps = img_exif['GPS GPSLatitude']

     # N,S 南北纬方向
     latitude_direction = img_exif['GPS GPSLatitudeRef']

     # 经度数
     longitude_gps = img_exif['GPS GPSLongitude']

     # E,W 东西经方向
     longitude_direction = img_exif['GPS GPSLongitudeRef']

     # 拍摄时间
     take_time = img_exif['EXIF DateTimeOriginal']


     def judge_time_met(self, take_time):
         """
         判断拍摄时间是否是在今天
         :param take_time:
         :return:
         """
         # 拍摄时间
         format_time = str(take_time).split(" ")[0].replace(":", "-")

         # 当天日期
         today = str(datetime.date.today())

         if format_time == today:
             return True
         else:
             return False


     if is_lie:
         print('很遗憾的通知你，你的女朋友在撒谎！！！')
         return

     x_pi = 3.14159265358979324 * 3000.0 / 180.0
     pi = 3.1415926535897932384626  # π
     a = 6378245.0  # 长半轴
     ee = 0.00669342162296594323  # 扁率


     def wgs84togcj02(lng, lat):
         """
         WGS84转GCJ02(火星坐标系)
         :param lng:WGS84坐标系的经度
         :param lat:WGS84坐标系的纬度
         :return:
         """
         if out_of_china(lng, lat):  # 判断是否在国内
             return lng, lat
         dlat = transformlat(lng - 105.0, lat - 35.0)
         dlng = transformlng(lng - 105.0, lat - 35.0)
         radlat = lat / 180.0 * pi
         magic = math.sin(radlat)
         magic = 1 - ee * magic * magic
         sqrtmagic = math.sqrt(magic)
         dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
         dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
         mglat = lat + dlat
         mglng = lng + dlng
         return [mglng, mglat]