from sqlalchemy import create_engine, text


# Create an Engine
engine = create_engine("sqlite://", echo=True)

# Test the connection
with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.fetchone())
