STRING_LEN_SMALL = 50
STRING_LEN_MEDIUM = 200
STRING_LEN_LARGE = 500


LEN_MOBILE = 15

# Import all models to resolve circular import issues
from .UserType import UserType
from .User import User
from .UserLogin import UserLogin
from .Feedback import Feedback
from .Kid import Kid
from .Journey import Journey
from .Location import Location
from .Attendance import Attendance
from .Bus import Bus
