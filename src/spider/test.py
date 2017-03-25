from models import logger as log
from models.adminuser import AdminUser
from models.msg import Msg
from models.process import Process
from models.user import User

adminuser = AdminUser({'id':'15527941667', 'password': '52902**Fcs', 'name':'付昌盛'})
adminuser.insert()
# adminuser.delete({}, True)

# user = User({'id':'123', 'name':'123132'})
# user.insert()
# user.delete({}, True)

# msg = Msg({'id':'123456', 'user_id':'456123'})
# msg.insert()
# log.d(msg.select())
# msg.delete({},True)

# pro = Process({'id':'123456546'})
# pro.insert()
# pro.delete({},True)
