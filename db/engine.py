from sqlalchemy import create_engine


ENGINE = create_engine(
    'mssql+pyodbc://DESKTOP-OE5G1EA\\SQLEXPRESS/ggs_stud?driver=SQL+Server+Native+Client+11.0', echo=True)
