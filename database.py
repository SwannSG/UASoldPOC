# database stuff
from sqlalchemy import *

sqlite_file = '/home/swannsg/development/UAS/db/UAS.db'
engine = create_engine("sqlite:///%s" % sqlite_file, echo=True)

metadata = MetaData() 

user = Table('asset', metadata,
    Column('id', Integer, primary_key = True),
    Column('label', String(30), nullable = False),
    Column('description', String(60)),
    Column('amount', Numeric, nullable = False)
)

metadata.create_all(engine)
