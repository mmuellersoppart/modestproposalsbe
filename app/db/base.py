# Import all the models, so that Base has them before being imported by Alembic

from app.db.base_class import Base  # noqa: F401
from app.db.tables.coupons import Coupon  # noqa: F401
from app.db.tables.user import User  # noqa: F401
from app.db.tables.proposal import Proposal  # noqa: F401
