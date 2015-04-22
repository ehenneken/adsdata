import os
import sys
import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


# When building metrics, the following collections NEEDS to exist:
#
#     1. citations
#     2. refereed
#     3. references
#     4. citations
#     5. reads
#     6. downloads
#     7. authors


Base = declarative_base()

class Metrics(Base):
  __tablename__='metrics'

  id = Column(Integer,primary_key=True)
  bibcode = Column(String,nullable=False,index=True,unique=True)
  refereed = Column(Boolean)
  rn_citations = Column(postgresql.REAL)
  rn_citation_data = Column(postgresql.JSON)
  downloads = Column(postgresql.ARRAY(Integer))
  reads = Column(postgresql.ARRAY(Integer))
  an_citations = Column(postgresql.REAL)
  refereed_citation_num = Column(Integer)
  citation_num = Column(Integer)
  reference_num = Column(Integer)
  citations = Column(postgresql.ARRAY(String))
  refereed_citations = Column(postgresql.ARRAY(String))
  author_num = Column(Integer)
  an_refereed_citations = Column(postgresql.REAL)
  modtime = Column(DateTime)
