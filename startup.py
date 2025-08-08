#!/usr/bin/env python3
"""
Azure Web App startup file for Flask application
"""

import os
import sys

# Set up logging for debugging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    logger.info("Starting Flask application...")
    
    # Import the Flask app
    from app import app
    
    logger.info("Flask app imported successfully")
    
    if __name__ == "__main__":
        # Azure Web App will set the PORT environment variable
        port = int(os.environ.get('PORT', 5000))
        
        logger.info(f"Starting server on port {port}")
        
        # Run the app
        app.run(
            host='0.0.0.0',
            port=port,
            debug=False  # Set to False for production
        )
        
except Exception as e:
    logger.error(f"Failed to start application: {str(e)}")
    logger.error(f"Error type: {type(e).__name__}")
    import traceback
    logger.error(f"Traceback: {traceback.format_exc()}")
    sys.exit(1) 
    