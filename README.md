# Bigo Agency Host Dashboard

A comprehensive web dashboard for managing and monitoring Bigo Live agency hosts, built with Flask and deployed on AWS Elastic Beanstalk.

## Features

- **Dashboard Overview**: Real-time statistics and key metrics
- **Host Management**: Track host performance, revenue, and viewer engagement
- **Analytics & Charts**: Interactive charts and data visualizations
- **Secure Authentication**: Admin login system
- **Responsive Design**: Mobile-friendly interface with Bootstrap
- **Real-time Updates**: Live data updates and notifications

## Screenshots

### Dashboard
- Total hosts, active hosts, monthly revenue, and viewer statistics
- Revenue trend charts
- Top performer rankings

### Analytics
- Revenue trends and growth metrics
- Host performance comparisons
- Viewer engagement analytics
- Detailed host statistics table

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: Bootstrap 5, Chart.js, Font Awesome
- **Deployment**: AWS Elastic Beanstalk
- **CI/CD**: GitHub Actions

## Quick Start

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/TacitBlade/Bigo-Agency-Host-Dashboard.git
   cd Bigo-Agency-Host-Dashboard
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the dashboard**
   - Open http://localhost:5000 in your browser
   - Login with: `admin` / `password`

## Deployment

### AWS Elastic Beanstalk

1. **Prerequisites**
   - AWS CLI installed and configured
   - Elastic Beanstalk CLI (eb cli)

2. **Deploy**
   ```bash
   eb init
   eb create
   eb deploy
   ```

### GitHub Actions CI/CD

The project includes automated deployment via GitHub Actions:

1. **Set up AWS credentials in GitHub Secrets:**
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`

2. **Push to main branch:**
   ```bash
   git push origin main
   ```

The workflow will automatically:
- Run tests and linting
- Deploy to Elastic Beanstalk on successful builds

## Project Structure

```
Bigo-Agency-Host-Dashboard/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── .github/
│   └── workflows/
│       └── deploy.yml       # CI/CD pipeline
├── .ebextensions/
│   └── 01_python.config     # Elastic Beanstalk configuration
├── static/
│   └── css/
│       ├── styles.css       # Custom CSS styles
│       └── js/
│           └── scripts.js   # Custom JavaScript
└── templates/
    ├── base.html           # Base template
    ├── dashboard.html      # Main dashboard
    ├── charts.html         # Analytics page
    └── login.html          # Login page
```

## Configuration

### Environment Variables

Set these environment variables in production:

- `SECRET_KEY`: Flask secret key for sessions
- `FLASK_ENV`: Set to 'production' for production deployment
- `PORT`: Server port (default: 5000)

### AWS Elastic Beanstalk

Configuration is handled via `.ebextensions/01_python.config`:

- WSGI path configuration
- Static file serving
- Environment variables

## API Endpoints

- `GET /` - Dashboard home page
- `GET /login` - Login page
- `POST /login` - Process login
- `GET /charts` - Analytics and charts page
- `GET /api/chart-data` - JSON API for chart data
- `GET /logout` - Logout and clear session

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security

- Change default login credentials in production
- Set strong `SECRET_KEY` environment variable
- Use HTTPS in production
- Implement proper user authentication system
- Validate and sanitize all user inputs

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team

## Roadmap

- [ ] Database integration (PostgreSQL/MySQL)
- [ ] User role management
- [ ] Real-time notifications
- [ ] Export functionality (PDF/Excel)
- [ ] Mobile app API
- [ ] Advanced analytics and reporting
- [ ] Integration with Bigo Live API