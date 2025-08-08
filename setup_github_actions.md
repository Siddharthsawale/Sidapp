# 🚀 GitHub Actions Setup Guide

## **📋 Step-by-Step Instructions**

### **Step 1: Configure GitHub Secrets**

1. **Go to your GitHub repository**: https://github.com/Siddharthsawale/Sidapp
2. **Click Settings** (top navigation)
3. **Click Secrets and variables** → **Actions** (left sidebar)
4. **Click "New repository secret"** for each secret below

### **Step 2: Add Production Publish Profile**

**Secret Name**: `AZURE_WEBAPP_PUBLISH_PROFILE`

**Secret Value** (copy the entire XML content):
```xml
<publishData><publishProfile profileName="nexiqon-portal-jan2025 - Web Deploy" publishMethod="MSDeploy" publishUrl="nexiqon-portal-jan2025.scm.azurewebsites.net:443" msdeploySite="nexiqon-portal-jan2025" userName="$nexiqon-portal-jan2025" userPWD="e347er2fytEyFqN7TYQQcgqD06SRFbBtMHyx0qyMdgg5mDSqQ1dZ6TH1crPy" destinationAppUrl="http://nexiqon-portal-jan2025.azurewebsites.net" SQLServerDBConnectionString="" mySQLDBConnectionString="" hostingProviderForumLink="" controlPanelLink="https://portal.azure.com" webSystem="WebSites"><databases /></publishProfile><publishProfile profileName="nexiqon-portal-jan2025 - FTP" publishMethod="FTP" publishUrl="ftps://waws-prod-bay-241.ftp.azurewebsites.windows.net/site/wwwroot" ftpPassiveMode="True" userName="REDACTED" userPWD="REDACTED" destinationAppUrl="http://nexiqon-portal-jan2025.azurewebsites.net" SQLServerDBConnectionString="REDACTED" mySQLDBConnectionString="" hostingProviderForumLink="" controlPanelLink="https://portal.azure.com" webSystem="WebSites"><databases /></publishProfile><publishProfile profileName="nexiqon-portal-jan2025 - Zip Deploy" publishMethod="ZipDeploy" publishUrl="nexiqon-portal-jan2025.scm.azurewebsites.net:443" userName="$nexiqon-portal-jan2025" userPWD="e347er2fytEyFqN7TYQQcgqD06SRFbBtMHyx0qyMdgg5mDSqQ1dZ6TH1crPy" destinationAppUrl="http://nexiqon-portal-jan2025.azurewebsites.net" SQLServerDBConnectionString="" mySQLDBConnectionString="" hostingProviderForumLink="" controlPanelLink="https://portal.azure.com" webSystem="WebSites"><databases /></publishProfile></publishData>
```

### **Step 3: Add Staging Publish Profile**

**Secret Name**: `AZURE_WEBAPP_PUBLISH_PROFILE_STAGING`

**Secret Value** (copy the entire XML content):
```xml
<publishData><publishProfile profileName="nexiqon-portal-staging - Web Deploy" publishMethod="MSDeploy" publishUrl="nexiqon-portal-staging.scm.azurewebsites.net:443" msdeploySite="nexiqon-portal-staging" userName="REDACTED" userPWD="REDACTED" destinationAppUrl="http://nexiqon-portal-staging.azurewebsites.net" SQLServerDBConnectionString="REDACTED" mySQLDBConnectionString="" hostingProviderForumLink="" controlPanelLink="https://portal.azure.com" webSystem="WebSites"><databases /></publishProfile><publishProfile profileName="nexiqon-portal-staging - FTP" publishMethod="FTP" publishUrl="ftps://waws-prod-bay-241.ftp.azurewebsites.windows.net/site/wwwroot" ftpPassiveMode="True" userName="REDACTED" userPWD="REDACTED" destinationAppUrl="http://nexiqon-portal-staging.azurewebsites.net" SQLServerDBConnectionString="REDACTED" mySQLDBConnectionString="" hostingProviderForumLink="" controlPanelLink="https://portal.azure.com" webSystem="WebSites"><databases /></publishProfile><publishProfile profileName="nexiqon-portal-staging - Zip Deploy" publishMethod="ZipDeploy" publishUrl="nexiqon-portal-staging.scm.azurewebsites.net:443" userName="REDACTED" userPWD="REDACTED" destinationAppUrl="http://nexiqon-portal-staging.azurewebsites.net" SQLServerDBConnectionString="REDACTED" mySQLDBConnectionString="" hostingProviderForumLink="" controlPanelLink="https://portal.azure.com" webSystem="WebSites"><databases /></publishProfile></publishData>
```

### **Step 4: Configure Staging Environment**

1. **Go to Azure Portal**: https://portal.azure.com
2. **Navigate to**: nexiqon-portal-staging Web App
3. **Set startup command**:
   - Go to **Configuration** → **General settings**
   - **Startup Command**: `python startup.py`
   - **Save** and **Restart**

### **Step 5: Test the Pipeline**

1. **Make a small change** to any file in your repository
2. **Commit and push** to GitHub
3. **Check Actions tab** in GitHub to see the pipeline running

## **🔍 What the Pipeline Does**

### **Build Stage:**
- ✅ Install Python 3.11
- ✅ Install dependencies from requirements.txt
- ✅ Run code linting (flake8)
- ✅ Run unit tests (pytest)
- ✅ Generate test reports and coverage
- ✅ Verify app imports successfully

### **Staging Deployment:**
- ✅ Deploy to staging environment
- ✅ Run smoke tests
- ✅ Validate deployment

### **Production Deployment:**
- ✅ Deploy to production environment
- ✅ Run health checks
- ✅ Verify deployment

## **📊 Pipeline Benefits**

### **Automated Testing:**
- **Code Quality**: Linting catches style issues
- **Unit Tests**: Automated testing of functionality
- **Coverage Reports**: Track code quality over time

### **Safe Deployment:**
- **Staging First**: Test in staging before production
- **Rollback Ready**: Quick recovery from issues
- **Health Checks**: Verify deployment success

### **Artifact Management:**
- **Test Results**: Stored for analysis
- **Coverage Reports**: Track code quality
- **Deployment Packages**: Consistent, tested builds

## **🚀 Environment URLs**

- **Staging**: https://nexiqon-portal-staging.azurewebsites.net
- **Production**: https://nexiqon-portal-jan2025.azurewebsites.net

## **📈 Monitoring**

### **GitHub Actions:**
- **Actions tab**: View pipeline runs
- **Workflow logs**: Detailed execution logs
- **Artifacts**: Download test results and reports

### **Azure Monitoring:**
- **Application Insights**: Performance monitoring
- **Log Analytics**: Centralized logging
- **Health checks**: Automated monitoring

## **🔧 Troubleshooting**

### **Common Issues:**

1. **Pipeline fails on test step**:
   - Check if all dependencies are in requirements.txt
   - Verify test files are in the correct location

2. **Deployment fails**:
   - Verify publish profiles are correct
   - Check Azure Web App configuration
   - Ensure startup command is set correctly

3. **Tests fail**:
   - Review test output in Actions logs
   - Update tests to match current app functionality

### **Getting Help:**
- **GitHub Actions**: Check workflow logs for detailed error messages
- **Azure Portal**: Monitor Web App logs and metrics
- **Documentation**: Refer to AZURE_PIPELINES_GUIDE.md for detailed information

---

**🎉 Once configured, your Flask Employee Portal will have enterprise-grade CI/CD with automated testing, staging deployment, and production releases!** 