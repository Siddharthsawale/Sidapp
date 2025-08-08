#!/bin/bash

echo "🚀 Deploying Flask App to Azure..."

# Set variables
RESOURCE_GROUP="Wellsync"
WEBAPP_NAME="nexiqon-portal-jan2025"
GITHUB_REPO="https://github.com/Siddharthsawale/Sidapp.git"

echo "📋 Current deployment status:"
az webapp deployment source show --resource-group $RESOURCE_GROUP --name $WEBAPP_NAME

echo "🔄 Attempting to set up GitHub deployment..."
az webapp deployment source config --resource-group $RESOURCE_GROUP --name $WEBAPP_NAME --repo-url $GITHUB_REPO --branch main --manual-integration

echo "✅ Deployment configuration complete!"
echo "🌐 Your app should be available at: https://$WEBAPP_NAME.azurewebsites.net"
echo "📝 To trigger deployment, visit: https://portal.azure.com"
echo "   Navigate to: App Services > $WEBAPP_NAME > Deployment Center"
echo "   Click 'Sync' to deploy from GitHub" 