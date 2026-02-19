# Fix for Arabic Text Encoding Issues in PDF Reports

## Problem
Arabic text appears as garbled characters (e.g., "Ø§Ù„Ù…Ù…Ù„ÙƒØ©") in the generated PDF invoices.

## Root Cause
The wkhtmltopdf engine (used by Odoo for PDF generation) doesn't properly render Arabic characters without:
1. Proper Arabic fonts installed on the system
2. Correct font configuration in the report template

## Solution

### Step 1: Install Arabic Fonts on the Server

Run these commands on your Odoo server:

```bash
# Install Arabic fonts
sudo apt-get update
sudo apt-get install -y fonts-arabeyes fonts-farsiweb fonts-kacst fonts-kacst-one

# Or install the comprehensive Arabic font package
sudo apt-get install -y fonts-noto-naskh-arabic fonts-noto-kufi-arabic

# Refresh font cache
fc-cache -f -v

# Verify Arabic fonts are installed
fc-list :lang=ar
```

### Step 2: Restart Odoo

After installing fonts, restart your Odoo service:

```bash
# If using systemd
sudo systemctl restart odoo

# Or if running manually
# Stop and restart your Odoo process
```

### Step 3: Clear Browser Cache and Regenerate Reports

1. Clear your browser cache
2. Log back into Odoo
3. Regenerate the invoice PDF

## Alternative Solution: Use a Different PDF Engine

If the above solution doesn't work, you can switch to a different PDF rendering engine:

### Option 1: Install Better wkhtmltopdf Version

```bash
# Download and install wkhtmltopdf with patched Qt
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo apt-get -f install
```

### Option 2: Configure Odoo to Use System wkhtmltopdf

Update your `odoo.conf`:

```ini
[options]
reportgz = False
```

## Template Changes Already Applied

The following changes have been made to the report template to support Arabic:

1. **Added UTF-8 meta tag**:
   ```xml
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
   ```

2. **Configured fallback fonts**:
   ```css
   font-family: 'DejaVu Sans', 'Arial Unicode MS', sans-serif !important;
   ```

3. **Added RTL direction** to Arabic text sections:
   ```html
   <div style="direction: rtl;">
   ```

## Verification

To verify the fix is working:

1. Generate a new invoice PDF
2. Open the PDF
3. Arabic text should display correctly as: "المملكة العربية السعودية" not "Ø§Ù„Ù…Ù…Ù„ÙƒØ©"

## Troubleshooting

### If Arabic still shows as garbled:

1. **Check if fonts are installed**:
   ```bash
   fc-list :lang=ar | grep -i "kacst\|noto\|arabic"
   ```

2. **Check wkhtmltopdf version**:
   ```bash
   wkhtmltopdf --version
   ```
   Should show version 0.12.5 or higher with Qt patches.

3. **Test wkhtmltopdf directly**:
   Create a test HTML file:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="UTF-8">
       <style>
           body { font-family: 'DejaVu Sans', sans-serif; }
       </style>
   </head>
   <body>
       <h1>مرحبا بك</h1>
       <p>المملكة العربية السعودية</p>
   </body>
   </html>
   ```
   
   Generate PDF:
   ```bash
   wkhtmltopdf test.html test.pdf
   ```
   
   Open `test.pdf` - if Arabic doesn't show, wkhtmltopdf needs to be reinstalled.

4. **Check Odoo logs** for any font-related warnings:
   ```bash
   tail -f /var/log/odoo/odoo-server.log | grep -i font
   ```

## Best Practices for Arabic PDFs in Odoo

1. Always use system fonts like DejaVu Sans or KACST fonts
2. Don't rely on web fonts (@import from Google Fonts) - they won't work in PDF
3. Add `direction: rtl` to containers with Arabic text
4. Use proper UTF-8 encoding in XML files
5. Test PDF generation after any template changes

## Additional Resources

- [Odoo Documentation - Reports](https://www.odoo.com/documentation/19.0/developer/reference/backend/reports.html)
- [wkhtmltopdf Arabic Support](https://wkhtmltopdf.org/)
- [KACST Fonts](http://www.arabeyes.org/Kacst)

