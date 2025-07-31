# Victory Rehabilitation Centre - Deployment Guide

## 🚀 Deploy to Vercel (Recommended)

### Step 1: Create Vercel Account
1. Go to **vercel.com**
2. Sign up with GitHub, Google, or email
3. Choose the free plan

### Step 2: Upload Your Project
1. Click **"New Project"** or **"Add New Project"**
2. Choose **"Upload"** option
3. Drag your Victory Rehabilitation Centre folder or select ZIP file
4. Vercel will automatically detect it's a Python Flask application

### Step 3: Configure Environment Variables
Before deploying, add these environment variables in Vercel:

**Required Variables:**
- `DATABASE_URL`: Your PostgreSQL connection string
- `SESSION_SECRET`: `victory-rehab-secure-key-2025`

### Step 4: Get Free PostgreSQL Database

**Option A: Railway.app**
1. Go to railway.app
2. Sign up and create new project
3. Add PostgreSQL service
4. Copy the DATABASE_URL connection string

**Option B: Supabase.com**
1. Go to supabase.com  
2. Create new project
3. Go to Settings > Database
4. Copy the connection string

### Step 5: Deploy
1. Paste the DATABASE_URL in Vercel environment variables
2. Click **"Deploy"**
3. Wait 2-3 minutes for build completion
4. Get your live URL: `your-site-name.vercel.app`

## 🎯 What You'll Have After Deployment

✅ **Live Website**: Professional Victory Rehabilitation Centre website  
✅ **Custom Domain**: Vercel provides `.vercel.app` subdomain  
✅ **HTTPS Security**: Automatic SSL certificate  
✅ **Global CDN**: Fast loading worldwide  
✅ **Admin Panel**: Full content management system  

## 📱 Features Included

- **Homepage**: Logo, mission, and call-to-action
- **About Page**: Story, leadership (Robert Kerich)
- **Services**: Treatment programs and approaches
- **Admissions**: Process and requirements
- **Gallery**: Community images with admin moderation
- **Contact**: Team profiles and contact information
- **User System**: Registration, login, and profiles
- **Admin Panel**: Content moderation and management

## 🔧 Troubleshooting

**Build Errors**: Ensure all files are uploaded correctly  
**Database Issues**: Check DATABASE_URL format  
**Environment Variables**: Make sure all required variables are set  

## 📞 Support

If you need help with deployment:
- Check Vercel documentation
- Verify environment variables are correct
- Ensure database connection string is valid

Your Victory Rehabilitation Centre website will be live and accessible to help people find your services!