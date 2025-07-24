# Victory Rehabilitation Centre Website

A professional rehabilitation center website built with Flask and Tailwind CSS.

## Features

- **Professional Design**: Clean, modern interface with Victory Rehabilitation Centre branding
- **User Authentication**: Registration and login system with admin capabilities
- **Image Gallery**: Community gallery with admin moderation system
- **Contact Management**: Professional staff profiles and contact information
- **Responsive Design**: Mobile-friendly layout that works on all devices
- **Admin Panel**: Content moderation and user management tools

## Team

- **Robert Kerich** - Director & Founder
- **Joyce Chebet** - Lead Counselor

## Deployment

This application is configured for deployment on Vercel with PostgreSQL database support.

### Quick Vercel Deployment Steps

1. **Upload to Vercel**:
   - Go to vercel.com and sign up/login
   - Click "New Project" 
   - Upload your project folder or ZIP file
   - Vercel auto-detects Python Flask app

2. **Set Environment Variables** (in Vercel dashboard):
   ```
   DATABASE_URL=postgresql://user:pass@host:5432/dbname
   SESSION_SECRET=victory-rehab-secure-key-2025
   ```

3. **Get Free Database**:
   - Use Railway.app or Supabase.com
   - Create PostgreSQL database
   - Copy connection string to DATABASE_URL

4. **Deploy**: Click "Deploy" - your site will be live in 2-3 minutes!

### Environment Variables Required

```
DATABASE_URL=your_postgresql_connection_string
SESSION_SECRET=your_secure_session_secret
```

### Contact Information

- **Phone**: +254 722 965180 / +254 768 576590
- **Location**: Along Litein-Kericho Highway, Near Chelilis, P.O. Box 36, Litein
- **Mission**: Every Life Matters

## Technology Stack

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Frontend**: Tailwind CSS, Font Awesome, Google Fonts
- **Database**: PostgreSQL
- **Deployment**: Vercel