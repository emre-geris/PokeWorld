# 🎮 PokeWorld - A Django Pokémon Data Science Project

[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.1+-38B2AC.svg)](https://tailwindcss.com/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5+-orange.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.11+-pink.svg)](https://seaborn.pydata.org/)

## 🌟 About This Project

**PokeWorld** is my journey into Django web development and data science, combining the power of Python web frameworks with data visualization and analysis. This project represents my first major step into full-stack development, where I learned to build a complete web application from scratch.

### 🎯 Project Goals

-  **Learn Django**: Master Django's MVT (Model-View-Template) architecture
-  **Data Science Integration**: Implement data visualization using Matplotlib and Seaborn
-  **Modern Web Development**: Create responsive, beautiful UIs with Tailwind CSS
-  **Full-Stack Experience**: Build a complete web application with authentication, database management, and API integration

## 🚀 Features

### ✨ Core Features

-  **Pokémon Database**: Browse through a comprehensive collection of Pokémon with detailed stats
-  **Dynamic Type System**: Each Pokémon's type is visually represented with custom colors and badges
-  **Interactive Charts**: Beautiful radar and bar charts generated dynamically for each Pokémon
-  **User Authentication**: Complete registration and login system using Django's built-in forms
-  **Favorites System**: Save and manage your favorite Pokémon with AJAX-powered interactions
-  **Responsive Design**: Mobile-first design that works perfectly on all devices

### 🎨 Visual Features

-  **Type-Based Color Coding**: Every Pokémon type has its own color scheme
-  **Dynamic Chart Colors**: Charts automatically match each Pokémon's primary type
-  **Dual-Type Support**: Special handling for Pokémon with two types (gradient effects, alternating colors)
-  **Modern UI**: Beautiful gradients, animations, and hover effects
-  **Real-Time Search**: Instant search functionality with smooth animations

### 📊 Data Science Features

-  **Statistical Analysis**: Comprehensive stat breakdowns for each Pokémon
-  **Data Visualization**:
   -  **Radar Charts**: Spider/radar charts showing all 6 base stats
   -  **Bar Charts**: Horizontal bar charts for easy stat comparison
-  **Dynamic Chart Generation**: Charts are generated on-demand using Matplotlib and Seaborn
-  **Type-Based Color Mapping**: Charts automatically use colors that match each Pokémon's type

## 🛠️ Technology Stack

### Backend

-  **Django 5.2+**: Web framework for rapid development
-  **SQLite**: Lightweight database for development
-  **Python 3.8+**: Core programming language

### Frontend

-  **Tailwind CSS 4.1+**: Utility-first CSS framework
-  **HTML5**: Semantic markup
-  **JavaScript**: Interactive features and AJAX requests

### Data Science & Visualization

-  **Matplotlib**: Primary charting library
-  **Seaborn**: Statistical data visualization
-  **Pandas**: Data manipulation and analysis
-  **NumPy**: Numerical computing

### Development Tools

-  **Git**: Version control
-  **npm**: Package management for frontend assets
-  **Concurrently**: Run multiple development servers simultaneously

## 📁 Project Structure

```
PokeWorld/
├── PokeApp/                          # Main Django application
│   ├── models.py                     # Database models (Pokemon, Favorite)
│   ├── views.py                      # Business logic and chart generation
│   ├── urls.py                       # URL routing
│   ├── admin.py                      # Django admin configuration
│   ├── tests.py                      # Unit tests
│   ├── management/commands/          # Custom Django commands
│   │   └── fetch_pokemon.py         # Command to populate database from PokeAPI
│   └── templates/                    # HTML templates
│       ├── registration/             # Authentication templates
│       └── PokeApp/                  # App-specific templates
├── PokeWorld/                        # Django project settings
│   ├── settings.py                   # Project configuration
│   └── urls.py                       # Main URL configuration
├── templates/                        # Base templates
├── static/                          # Static files (CSS, JS, images)
├── media/                           # User-uploaded files and generated charts
├── pokemon_charts/                  # Generated chart images
└── manage.py                        # Django management script
```

## 🚀 Getting Started

### Prerequisites

-  Python 3.8 or higher
-  Node.js and npm
-  Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/emre-geris/pokeworld.git
   cd pokeworld
   ```

2. **Set up Python environment**

   ```bash
   # Create virtual environment
   python -m venv .venv

   # Activate virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate

   # Install Python dependencies
   pip install django pandas matplotlib seaborn numpy requests tqdm
   ```

3. **Set up frontend dependencies**

   ```bash
   npm install
   ```

4. **Run database migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Populate the database with Pokémon data**

   ```bash
   python manage.py fetch_pokemon
   ```

6. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development servers**

   ```bash
   # Start both Django and Tailwind CSS in development mode
   npm start

   # Or run them separately:
   npm run django    # Django development server
   npm run dev       # Tailwind CSS watcher
   ```

8. **Open your browser**
   Navigate to `http://127.0.0.1:8000/`

## 🎮 How to Use

### For Users

1. **Browse Pokémon**: View all Pokémon on the home page
2. **Search**: Use the search bar to find specific Pokémon
3. **View Details**: Click on any Pokémon to see detailed stats and charts
4. **Register/Login**: Create an account to save favorites
5. **Save Favorites**: Click the star icon to add Pokémon to your favorites
6. **View Favorites**: Access your saved Pokémon from the navigation menu

### For Developers

-  **Admin Panel**: Access at `/admin/` to manage data
-  **API Endpoint**: `/api/pokemons/` for programmatic access
-  **Chart Generation**: Charts are automatically generated when viewing Pokémon details

## 📊 Data Science Features Explained

### Chart Generation

The project generates two types of charts for each Pokémon:

1. **Radar Chart**: Shows all 6 base stats (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed) in a spider/radar format
2. **Bar Chart**: Displays the same stats as horizontal bars for easy comparison

### Color System

-  **Single-Type Pokémon**: Charts use the primary type's color
-  **Dual-Type Pokémon**:
   -  Radar charts use gradient effects with both type colors
   -  Bar charts alternate between primary and secondary type colors

### Type Color Mapping

Each Pokémon type has its own color scheme:

-  **Fire**: Red (#ef4444)
-  **Water**: Blue (#3b82f6)
-  **Grass**: Green (#10b981)
-  **Electric**: Yellow (#facc15)
-  And many more...

## 🔧 Customization

### Adding New Pokémon Types

1. Update the color constants in `views.py`
2. Add new type colors to `TYPE_COLORS`, `TYPE_BG_COLORS`, and `CHART_COLORS`

### Modifying Chart Styles

1. Edit the chart generation code in the `pokemon_detail` view
2. Adjust figure sizes, colors, and styling parameters

### Styling Changes

1. Modify Tailwind CSS classes in templates
2. Update the `static/src/input.css` file for custom styles

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

The project includes tests for:

-  Model creation and validation
-  User authentication
-  Favorite system functionality

## 📈 Future Enhancements

### Planned Features

-  [ ] **Battle Simulator**: Simulate Pokémon battles using stats
-  [ ] **Evolution Chains**: Show Pokémon evolution relationships
-  [ ] **Advanced Analytics**: More detailed statistical analysis
-  [ ] **User Profiles**: Customizable user profiles and preferences
-  [ ] **Social Features**: Share favorites and compare collections
-  [ ] **API Expansion**: More comprehensive REST API
-  [ ] **Mobile App**: React Native companion app

### Technical Improvements

-  [ ] **Performance Optimization**: Caching for chart generation
-  [ ] **Database Migration**: PostgreSQL for production
-  [ ] **Docker Support**: Containerized deployment
-  [ ] **CI/CD Pipeline**: Automated testing and deployment

## 🤝 Contributing

This is a learning project, but contributions are welcome! Please feel free to:

-  Report bugs
-  Suggest new features
-  Submit pull requests
-  Share your own Django/data science projects

## 📝 Learning Journey

### What I Learned

-  **Django Framework**: MVT architecture, ORM, forms, authentication
-  **Data Visualization**: Matplotlib, Seaborn, chart customization
-  **Frontend Development**: Tailwind CSS, responsive design, JavaScript
-  **Database Design**: Model relationships, migrations, data management
-  **API Integration**: Fetching data from external APIs (PokeAPI)
-  **Full-Stack Development**: Connecting frontend and backend seamlessly

### Challenges Overcome

-  **Chart Generation**: Learning to generate dynamic charts with proper styling
-  **Type System**: Implementing complex color logic for dual-type Pokémon
-  **Responsive Design**: Ensuring the app works perfectly on all devices
-  **Performance**: Optimizing database queries and chart generation
-  **User Experience**: Creating intuitive navigation and interactions

## 🙏 Acknowledgments

-  **PokeAPI**: For providing comprehensive Pokémon data
-  **Django Community**: For excellent documentation and support
-  **AI Assistance**: This project benefited from AI assistance for code optimization and problem-solving
-  **Open Source Community**: For the amazing tools and libraries that made this possible

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

-  **GitHub**:   (https://github.com/emre-geris)
-  **LinkedIn**: (https://linkedin.com/in/emre-geris)

---

**Note**: This README was generated with AI assistance to ensure comprehensive documentation of the project features and technical details. The project itself represents my personal learning journey in Django and data science development.

⭐ **If you find this project helpful, please give it a star!**
