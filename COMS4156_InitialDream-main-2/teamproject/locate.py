from flask import Blueprint
from flask import Flask, jsonify
from flask_simple_geoip import SimpleGeoIP


bp = Blueprint('locate', __name__,url_prefix='/locate')  # 'bp01'第一个参数是唯一标识,整个环境不能重复!  url_prefix='url前缀',当存在多个蓝图url冲突时,在地址栏输入'url前缀',就可以访问指定的蓝图文件


@bp.route('/locate', methods=('GET', 'POST'))
def locate():
    app = Flask(__name__)
    app.config.update(GEOIPIFY_API_KEY='at_FFA6Fj135RhjDUB1lKM0roNxMTAvD')
    simple_geoip = SimpleGeoIP(app)
    geoip_data = simple_geoip.get_geoip_data()
    return jsonify(data=geoip_data)