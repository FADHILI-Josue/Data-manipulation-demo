import logging
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User, Product
from faker import Faker
import random

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    level=logging.INFO,
)

fake = Faker()

def seed_database():
    db: Session = SessionLocal()
    batch_size = 10_000  # Number of records per batch
    try:
        users = []
        products = []

        # Generate and insert 500,000 users with random null values
        logging.info("Starting to insert users...")
        for i in range(1, 500_001):
            name = fake.name()
            email = fake.unique.email() if random.random() > 0.1 else None  # 10% chance of null email
            
            # Add user to the list
            users.append(User(name=name, email=email))
            
            if i % batch_size == 0:
                db.bulk_save_objects(users)
                db.commit()
                logging.info(f"Inserted {i} users so far...")
                users = []  # Clear the list after insertion
        
        # Insert any remaining users
        if users:
            db.bulk_save_objects(users)
            db.commit()
            logging.info(f"Inserted all 500,000 users.")

        # Generate and insert 500,000 products with random null values
        logging.info("Starting to insert products...")
        user_ids = db.query(User.id).all()
        user_ids = [uid[0] for uid in user_ids]
        
        for i, user_id in enumerate(user_ids, start=1):
            name = fake.word()
            price = fake.random_int(min=1, max=1000) if random.random() > 0.05 else None  # 5% chance of null price
            
            # Add product to the list
            products.append(Product(
                name=name,
                price=price,
                owner_id=user_id
            ))
            
            if i % batch_size == 0:
                db.bulk_save_objects(products)
                db.commit()
                logging.info(f"Inserted {i} products so far...")
                products = []  # Clear the list after insertion
        
        # Insert any remaining products
        if products:
            db.bulk_save_objects(products)
            db.commit()
            logging.info(f"Inserted all 500,000 products.")

        logging.info("Seeding completed successfully!")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
