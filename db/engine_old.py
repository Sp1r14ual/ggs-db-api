from sqlalchemy import create_engine


ENGINE = create_engine(
    'mssql+pyodbc://DESKTOP-8F7T81O\\SQLEXPRESS/ggs_stud?driver=SQL+Server+Native+Client+11.0', echo=True)
