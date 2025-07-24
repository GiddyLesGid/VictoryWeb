
# Victory Rehabilitation Centre

**Website for:** Victory Rehabilitation Centre  
**Motto:** Every Life Matters  
**Location:** Along Litein-Kericho Highway, near Chelilis  
**Postal Address:** P.O. Box 36, Litein  
**Primary Contact Person:** Robert Kerich (Director)  
📞 Contacts: +254 722 965180 / +254 768 576590  
🌐 Facebook: [Victory Rehabilitation Centre](https://www.facebook.com/61567699920038/posts/pfbid021oYEHdb78yAXEwDH37Yn9bAcsyLyhxdzVscQSKYwYcsabCf4pKiQWjC74ErqWFf8l/?app=fbl)  
📸 Logo and brand assets included in `favicon.zip`  
🖼️ Director image and other visual assets uploaded  

---

## 🎨 Brand Theme

- **Primary Colors:** Indigo `#4B0082`, Light Green `#90EE90`
- **Fonts:** Poppins (headings), Open Sans (body)
- **Logo:** Transparent and centered with tagline beneath

---

## 🎯 Vision

> To be the center of choice in South Rift in addressing addiction, alcoholism and substance abuse.

## 🧭 Mission

> To help individuals, families and communities achieve freedom from the effects of alcoholism and substance abuse.

## 💡 Core Values

**Respect**  
- Treat people with dignity and kindness  
- Respect client choices and contributions of families  

**Enduring**  
- Never give up; see no one as a lost cause  
- Driven and passionate  

**Holistic**  
- Treat mind, body and soul  
- Support family involvement  

**Action**  
- Do what we promise  
- Remain committed to learning and service  

**Improving**  
- Push limits with professionalism  
- Deliver discreet care  

**Brave**  
- Embrace change and challenge discrimination  
- Remove barriers to recovery  

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3, JavaScript
- **CSS Framework:** Tailwind CSS (CDN)
- **Auth:** Basic account system + Google OAuth
- **Database:** SQLite (for Replit) or PostgreSQL (for Vercel/production)
- **Templating:** Jinja2

---

## 🌐 Features

- Home, About, Services, Admissions, Contact pages
- Gallery page (Image upload, captions, moderation)
- User auth (register, login, Google sign-in)
- Admin panel for moderation (delete/edit images)
- Responsive design
- WhatsApp and Facebook contact buttons
- Favicon and logo from `favicon.zip`
- Facebook integrated; other social media as placeholders

---

## 🧩 Folder Structure

```
victory-rehab/
├── static/
│   ├── css/
│   ├── js/
│   ├── images/   # Extracted from favicon.zip + gallery uploads
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── contact.html
│   └── gallery.html
├── app.py
├── auth.py  # For login and register routes
├── models.py  # For user and gallery models
├── requirements.txt
└── README.md
```

---

## 🔒 Authentication

- Google OAuth login (via Flask-Dance or OAuthlib)
- Basic register/login system with hashed passwords (Flask-Login)
- Admins can moderate gallery content

---

## 📷 Gallery System

- Upload photos with captions
- User interaction (e.g., likes or comments — optional)
- Admin can delete or edit images
- Stored in `/static/uploads` or external store for Vercel

---

## 🚀 Hosting with Vercel

Vercel will be used **only for the static frontend**. The dynamic backend (Flask + DB) should remain on Replit or Render:

### Option A: Full Backend on Replit
- Flask app and DB remain on Replit
- Hosted with domain routing

### Option B: Split Hosting (Vercel + External API)
- Export HTML for Vercel
- Backend hosted on Replit or Render
- Frontend fetches data via API endpoints

---

## ✅ Development Checklist

- [ ] Upload `favicon.zip` and extract assets
- [ ] Add provided director photo and institution branding
- [ ] Implement user login & admin gallery moderation
- [ ] Link Facebook and enable WhatsApp
- [ ] Integrate Google OAuth
- [ ] Configure form for contact page
- [ ] Test responsive design on mobile
- [ ] Push to GitHub & connect to Vercel

---

## 🔐 GitHub & Vercel Integration

When ready, GitHub repo can be used for Vercel deployment.  
If you prefer seamless setup, GitHub credentials may be provided securely to complete automatic deployment setup.

---

## 🙌 Tagline

**"Every Life Matters"**
