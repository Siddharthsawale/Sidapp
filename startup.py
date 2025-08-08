#!/usr/bin/env python3
"""
Azure Web App startup file for Flask application
"""

from app import app

if __name__ == "__main__":
    # Azure Web App will set the PORT environment variable
    import os
    port = int(os.environ.get('PORT', 5000))
    
    # Run the app
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False  # Set to False for production
    ) 
    