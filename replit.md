# Victory Rehabilitation Centre Website

## Overview

This is a Flask-based web application for Victory Rehabilitation Centre, a rehabilitation facility located in Litein, Kenya. The website serves as both an informational portal and a community platform with image gallery functionality. The site emphasizes the center's mission of helping individuals, families, and communities overcome addiction and substance abuse.

## Recent Changes

**July 24, 2025:**
- Added official Victory Rehabilitation Centre logo to navigation and homepage
- Added professional director photo (Robert Kerich) to About and Contact pages
- Created beautiful "Meet Our Team" section with staff contact information
- Enhanced contact page with professional staff profiles and contact details
- Updated leadership section on About page with director's photo
- Fixed all code syntax errors and type issues
- Configured application for Vercel deployment with vercel.json
- Skipped Google OAuth integration as per user preference
- Prepared application for production deployment

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The application follows a traditional Flask monolithic architecture with the following key characteristics:

### Backend Architecture
- **Framework**: Flask with Jinja2 templating
- **Database**: SQLAlchemy ORM with SQLite (default) or PostgreSQL support
- **Authentication**: Flask-Login with password hashing
- **File Handling**: Werkzeug for secure file uploads with PIL for image processing

### Frontend Architecture
- **Styling**: Tailwind CSS framework with custom brand colors
- **Typography**: Google Fonts (Poppins for headings, Open Sans for body)
- **Icons**: Font Awesome 6.0
- **JavaScript**: Vanilla JS for interactive elements

### Design System
- **Brand Colors**: Indigo (#4B0082) primary, Light Green (#90EE90) accent
- **Responsive Design**: Mobile-first approach using Tailwind's grid system
- **Brand Identity**: Centered around "Every Life Matters" motto

## Key Components

### Authentication System
- **Local Authentication**: Username/email and password-based registration and login
- **Google OAuth**: Integrated Google authentication (requires setup)
- **User Roles**: Standard users and administrators with different permissions
- **Session Management**: Flask-Login handles user sessions with remember-me functionality

### Gallery Management
- **Image Upload**: Users can upload images with optional captions
- **Moderation System**: Admin approval required before images appear publicly
- **File Security**: Secure filename handling, file type validation, size limits (16MB)
- **Image Processing**: PIL integration for image handling

### Content Management
- **Static Pages**: About, Services, Admissions, Contact information
- **Dynamic Content**: User-generated gallery content
- **Admin Panel**: Gallery moderation and user management interface

### Page Structure
- **Homepage**: Hero section with mission/vision, call-to-action buttons
- **About**: Organization story, leadership, values
- **Services**: Treatment programs and therapeutic approaches
- **Admissions**: Process information and contact details
- **Gallery**: Community-contributed images with moderation
- **Contact**: Multiple contact methods including WhatsApp integration

## Data Flow

### User Registration/Login Flow
1. User accesses registration/login forms
2. Credentials validated against database
3. Password hashing using Werkzeug security
4. Session established via Flask-Login
5. Redirect to intended page or homepage

### Image Upload Flow
1. Authenticated user selects image and optional caption
2. File validation (type, size, security checks)
3. Secure filename generation using UUID
4. Image stored in static/uploads directory
5. Database record created with approval=False
6. Admin reviews and approves via admin panel
7. Approved images appear in public gallery

### Admin Moderation Flow
1. Admin accesses admin panel (role-based access)
2. Views pending images requiring approval
3. Approves or rejects submissions
4. Statistics dashboard shows approval metrics

## External Dependencies

### Required Python Packages
- Flask: Web framework
- Flask-SQLAlchemy: Database ORM
- Flask-Login: User session management
- Werkzeug: Security utilities and file handling
- PIL/Pillow: Image processing
- requests: HTTP requests for OAuth
- oauthlib: OAuth 2.0 implementation

### External Services
- **Google OAuth**: Requires client ID and secret configuration
- **Database**: SQLite (development) or PostgreSQL (production)
- **Static Assets**: Google Fonts, Font Awesome CDN, Tailwind CSS CDN

### Frontend Dependencies
- Tailwind CSS: Utility-first CSS framework
- Google Fonts API: Typography (Poppins, Open Sans)
- Font Awesome: Icon library
- No frontend build process required (uses CDNs)

## Deployment Strategy

### Environment Configuration
- **Development**: SQLite database, debug mode enabled
- **Production**: Environment variables for database URL, session secrets
- **File Storage**: Local filesystem (static/uploads directory)
- **Proxy Configuration**: ProxyFix middleware for proper request handling

### Required Environment Variables
- `DATABASE_URL`: Database connection string
- `SESSION_SECRET`: Flask session encryption key
- `GOOGLE_OAUTH_CLIENT_ID`: Google authentication client ID
- `GOOGLE_OAUTH_CLIENT_SECRET`: Google authentication secret
- `REPLIT_DEV_DOMAIN`: Domain for OAuth callback URLs

### Security Considerations
- Password hashing with Werkzeug
- Secure file upload validation
- CSRF protection through Flask's built-in mechanisms
- SQL injection prevention through SQLAlchemy ORM
- File upload restrictions (type, size, secure naming)

### Scalability Notes
- Database connection pooling configured
- Static file serving through Flask (suitable for small-medium traffic)
- Image storage on local filesystem (may need cloud storage for larger scale)
- No caching layer implemented (could add Redis/Memcached for performance)