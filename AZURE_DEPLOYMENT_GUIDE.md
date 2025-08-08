# Azure Web App Deployment Guide

## 🚀 **Deploy Your Flask App to Azure from Cursor**

### **📋 Prerequisites**
- Azure account (free tier works fine)
- Cursor IDE with your project open
- Git repository (local or remote)

### **🔧 Method 1: Using Azure Extensions (Recommended)**

#### **Step 1: Install Extensions**
1. Open Cursor
2. Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac)
3. Search for and install:
   - **Azure App Service**
   - **Azure Account**
   - **Azure Resources**

#### **Step 2: Sign in to Azure**
1. Press `Ctrl+Shift+P` / `Cmd+Shift+P` to open Command Palette
2. Type `Azure: Sign In`
3. Follow the browser authentication flow
4. Return to Cursor once authenticated

#### **Step 3: Create Azure Web App**
1. Press `Ctrl+Shift+P` / `Cmd+Shift+P`
2. Type `Azure App Service: Create New Web App`
3. Follow the prompts:
   - **App Name**: Choose a unique name (e.g., `your-app-name-2025`)
   - **Resource Group**: Create new or use existing
   - **Runtime Stack**: Select `Python 3.11` or latest
   - **Region**: Choose closest to your users
   - **Pricing Tier**: F1 (Free) for testing, B1 (Basic) for production

#### **Step 4: Deploy Your App**
1. Right-click on your project folder in Cursor
2. Select `Deploy to Web App...`
3. Choose your newly created Web App
4. Confirm deployment

### **🔧 Method 2: Using Git Deployment**

#### **Step 1: Initialize Git (if not already done)**
```bash
git init
git add .
git commit -m "Initial commit"
```

#### **Step 2: Set up Azure Git Deployment**
1. Go to [Azure Portal](https://portal.azure.com)
2. Create a new **App Service**
3. Go to **Deployment Center**
4. Choose **Local Git** as source
5. Copy the Git URL provided

#### **Step 3: Add Azure as Remote**
```bash
git remote add azure <your-azure-git-url>
git push azure main
```

### **🔧 Method 3: Using Azure CLI**

#### **Step 1: Install Azure CLI**
- Download from [Azure CLI Installation](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

#### **Step 2: Login and Deploy**
```bash
# Login to Azure
az login

# Create resource group
az group create --name myResourceGroup --location "East US"

# Create App Service plan
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku FREE

# Create web app
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name your-app-name --runtime "PYTHON|3.11"

# Deploy from local git
az webapp deployment source config-local-git --name your-app-name --resource-group myResourceGroup

# Push your code
git remote add azure <git-url-from-previous-command>
git push azure main
```

### **⚙️ Configuration for Production**

#### **Environment Variables**
In Azure Portal, go to your Web App → Configuration → Application Settings:

```
WEBSITE_HTTPLOGGING_RETENTION_DAYS = 7
SCM_DO_BUILD_DURING_DEPLOYMENT = true
PYTHONPATH = /home/site/wwwroot
```

#### **Database Configuration**
If you need to configure your database for production:

1. Go to Azure Portal → Your Web App → Configuration
2. Add connection strings or environment variables:
   ```
   DB_HOST = your-production-db-host
   DB_NAME = your-production-db-name
   DB_USER = your-production-db-user
   DB_PASSWORD = your-production-db-password
   ```

### **📁 Files Created for Deployment**

The following files have been created to support Azure deployment:

1. **`startup.py`** - Entry point for Azure Web App
2. **`web.config`** - IIS configuration for Python
3. **`.deployment`** - Deployment configuration
4. **`deploy.cmd`** - Custom deployment script
5. **`requirements.txt`** - Already exists, lists Python dependencies

### **🐛 Troubleshooting**

#### **Common Issues:**

1. **App doesn't start**
   - Check logs in Azure Portal → Log stream
   - Verify `startup.py` is correct
   - Check `requirements.txt` has all dependencies

2. **Static files not loading**
   - Ensure `static/` folder is included in deployment
   - Check web.config has correct paths

3. **Database connection issues**
   - Verify environment variables are set
   - Check firewall settings for Azure SQL
   - Update connection strings for production

#### **View Logs:**
1. Azure Portal → Your Web App → Log stream
2. Or use Azure CLI: `az webapp log tail --name your-app-name --resource-group myResourceGroup`

### **🚀 Quick Deployment Checklist**

- [ ] Install Azure extensions in Cursor
- [ ] Sign in to Azure account
- [ ] Create new Web App
- [ ] Deploy using right-click → "Deploy to Web App"
- [ ] Configure environment variables if needed
- [ ] Test your deployed application
- [ ] Monitor logs for any issues

### **📱 Access Your Deployed App**

Your app will be available at:
`https://your-app-name.azurewebsites.net`

### **💡 Tips for Success**

1. **Start with Free Tier**: Use F1 (Free) for testing, upgrade later
2. **Monitor Costs**: Set up billing alerts in Azure
3. **Use Staging Slots**: For zero-downtime deployments (requires Basic tier+)
4. **Enable HTTPS**: Automatically enabled for `*.azurewebsites.net`
5. **Custom Domain**: Add your own domain in Azure Portal

---

**🎉 Your Flask application with LSU colors and IT Portal is now ready for Azure deployment!** 