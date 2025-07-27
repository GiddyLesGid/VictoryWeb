
from app import app, db
from models import User

def make_user_admin(email):
    """Make a user admin by their email address"""
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if user:
            user.is_admin = True
            db.session.commit()
            print(f"User {user.username} ({user.email}) is now an admin!")
            return True
        else:
            print(f"No user found with email: {email}")
            return False

def list_users():
    """List all users in the database"""
    with app.app_context():
        users = User.query.all()
        if not users:
            print("No users found in database")
        else:
            print("Current users:")
            for user in users:
                admin_status = " (ADMIN)" if user.is_admin else ""
                print(f"- {user.username} ({user.email}){admin_status}")

if __name__ == "__main__":
    print("Admin Setup Tool")
    print("-" * 30)
    
    # List current users
    list_users()
    
    # Get email input
    email = input("\nEnter email address to make admin (or press Enter to cancel): ").strip()
    
    if email:
        make_user_admin(email)
    else:
        print("Operation cancelled")
