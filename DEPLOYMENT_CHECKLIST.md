# 🚀 Azure Deployment Checklist

## **✅ Quick Steps to Deploy from Cursor**

### **1. Install Azure Extension**
```
Extensions → Search "Azure App Service" → Install
```

### **2. Sign In to Azure**
```
Ctrl+Shift+P → "Azure: Sign In" → Follow browser login
```

### **3. Create & Deploy**
```
Ctrl+Shift+P → "Azure App Service: Create New Web App"
→ Choose unique app name
→ Select Python 3.11
→ Choose F1 (Free) tier
→ Right-click project → "Deploy to Web App"
```

### **4. Access Your App**
```
https://your-app-name.azurewebsites.net
```

---

## **📁 Files Ready for Deployment**

✅ `startup.py` - Azure entry point  
✅ `web.config` - IIS configuration  
✅ `.deployment` - Deployment config  
✅ `deploy.cmd` - Custom deployment script  
✅ `requirements.txt` - Python dependencies  
✅ `.gitignore` - Excludes unnecessary files  
✅ `app.py` - Updated with environment variables  

---

## **🔐 Default Login Credentials**

- **Admin**: `admin@nexiqon.com` (any password)
- **Employee**: `employee@nexiqon.com` (any password)
- **HR**: `hr@nexiqon.com` (any password)
- **IT**: `it@nexiqon.com` (any password)

---

## **⚡ Alternative Methods**

### **Git Deployment**
```bash
git init
git add .
git commit -m "Deploy to Azure"
git remote add azure <azure-git-url>
git push azure main
```

### **Azure CLI**
```bash
az login
az webapp create --resource-group myRG --plan myPlan --name myapp --runtime "PYTHON|3.11"
az webapp deployment source config-local-git --name myapp --resource-group myRG
```

---

## **🎯 Features Included**

✅ LSU Color Scheme (Purple & Gold)  
✅ Dark/Light Mode Toggle  
✅ IT Portal in Navigation  
✅ Employee & Admin Dashboards  
✅ Role-based Authentication  
✅ Database Integration  
✅ Responsive Design  

---

**🎉 Your app is ready to deploy!** 