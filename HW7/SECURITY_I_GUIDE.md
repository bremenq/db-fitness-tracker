# Security I - Email Encryption Setup Guide

**Assignment:** Databases Project 2025 - Assignment 7 (Security I)  
**Deadline:** 2025-nov-06 23:59  
**Submission:** Email to mitadic@constructor.university

---

## Overview

This guide walks you through completing the Security I assignment, which requires:
1. Installing GPG encryption software (Gpg4win)
2. Generating your own GPG key pair
3. Importing the TA's public key
4. Sending your public key to the TA
5. Sending an encrypted and digitally signed email to the TA

**Why?** Email disclaimers are insufficient for achieving secrecy and integrity. Encryption and digital signatures are the proper way to secure communications.

---

## Step 1: Download and Install Gpg4win

### 1.1 Download Gpg4win

1. Visit: **https://www.gpg4win.org/download.html**
2. Click the **Download Gpg4win** button
3. The installer is free (donation optional)
4. Save the installer file (e.g., `gpg4win-4.x.x.exe`)

### 1.2 Install Gpg4win

1. Run the downloaded installer as Administrator
2. **Important:** During installation, ensure these components are selected:
   - ✅ **GnuPG** - The core encryption engine
   - ✅ **Kleopatra** - Certificate manager (GUI for managing keys)
   - ✅ **GpgOL** - Outlook plugin for email encryption
   - ⬜ GpgEX (optional, for file encryption in Windows Explorer)
3. Complete the installation with default settings
4. Restart Outlook after installation

### 1.3 Verify Installation

1. Open **Kleopatra** (search in Windows Start menu)
2. You should see the Kleopatra certificate manager window
3. In Outlook, go to **File → Options → Add-ins** and verify **GpgOL** is listed as active

---

## Step 2: Generate Your GPG Key Pair

### 2.1 Create Your Key Pair

1. Open **Kleopatra**
2. Click **File → New OpenPGP Key Pair** (or the "New Key Pair" button)
3. Fill in your details:
   - **Name:** Your full name (e.g., "Aleksandr Zinovev")
   - **Email:** Your Constructor University email (e.g., "azinovev@constructor.university")
   - **Protect the generated key with a passphrase:** Check this box
4. Click **Advanced Settings** and configure:
   - **Key Material:** RSA
   - **Key Size:** **4096 bits** (recommended for security, minimum 2048)
   - **Valid until:** Set expiration (e.g., 2 years) or leave unlimited
5. Click **OK**, then **Create**
6. Enter a **strong passphrase** (you'll need this to sign emails)
7. Confirm the passphrase
8. Wait for key generation to complete

### 2.2 Backup Your Keys

**CRITICAL:** Back up your private key immediately!

1. In Kleopatra, right-click your newly created key
2. Select **Backup Secret Keys**
3. Save to a secure location (USB drive, encrypted folder)
4. **Never share your private key with anyone!**

---

## Step 3: Import the TA's Public Key

### 3.1 Locate the TA's Public Key File

The TA (Milica Tadic) provided the public key file in MS Teams:
- **Filename:** `milica_publickey.asc`
- **Location:** Check your Downloads folder or Teams chat attachments

### 3.2 Import the Key

1. Open **Kleopatra**
2. Click **File → Import** (or drag and drop the `.asc` file into Kleopatra)
3. Navigate to and select `milica_publickey.asc`
4. Click **Open**
5. You should see a confirmation: "Certificate imported successfully"
6. The TA's key should now appear in your certificate list

### 3.3 Verify the Import

1. In Kleopatra, you should see an entry for **Milica Tadic** (or mitadic@constructor.university)
2. The key should show as valid
3. **Optional but recommended:** Right-click the key → **Certify Certificate** to mark it as trusted

---

## Step 4: Configure Outlook with GpgOL

### 4.1 Verify GpgOL Plugin

1. Open **Outlook**
2. Go to **File → Options → Add-ins**
3. Under **Active Application Add-ins**, verify **GpgOL** is listed
4. If not active, enable it and restart Outlook

### 4.2 Configure GpgOL Settings

1. In Outlook, go to **File → Options → GpgOL**
2. Under **Default Key**, select your key (the one you created in Step 2)
3. Configure preferences:
   - ✅ **Encrypt new messages by default:** Optional (can enable per-email)
   - ✅ **Sign new messages by default:** Optional
4. Click **OK**

### 4.3 Test Encryption Options

1. Compose a new email in Outlook
2. You should see new buttons in the ribbon:
   - **Encrypt** button (lock icon)
   - **Sign** button (pen/signature icon)
3. If you don't see these, restart Outlook

---

## Step 5: Export Your Public Key

### 5.1 Export Your Key

1. Open **Kleopatra**
2. Find your key in the list
3. Right-click your key → **Export**
4. Save the file with a descriptive name:
   - Example: `aleksandr_zinovev_publickey.asc`
   - Or: `azinovev_publickey.asc`
5. Save to a location you can easily find (Desktop or Documents)

This file will be sent to the TA in the next step.

---

## Step 6: Send Email #1 - Your Public Key

### 6.1 Compose the Email

1. Open **Outlook** and create a new email
2. **To:** `mitadic@constructor.university`
3. **Subject:** `Security I - Public Key Submission - Aleksandr Zinovev`
   - Replace with your actual name
4. **Attach:** Your exported public key file (e.g., `aleksandr_zinovev_publickey.asc`)
5. **Body:** Write a brief message, for example:

```
Dear Milica,

Please find attached my public key for the Security I assignment.

I will follow up with an encrypted and signed email shortly.

Best regards,
Aleksandr Zinovev
```

### 6.2 Send the Email

**Important:** This email does NOT need to be encrypted or signed. Just send it normally.

1. Click **Send**
2. Verify the email was sent successfully

---

## Step 7: Send Email #2 - Encrypted & Signed

### 7.1 Compose the Encrypted Email

1. Open **Outlook** and create a new email
2. **To:** `mitadic@constructor.university`
3. **Subject:** `Security I - Encrypted Submission - Aleksandr Zinovev`
4. **Body:** Write a confirmation message, for example:

```
Dear Milica,

This is my encrypted and signed submission for Security I assignment.

If you can read this message and verify my signature, the assignment is complete.

Best regards,
Aleksandr Zinovev
```

### 7.2 Enable Encryption and Signing

1. In the email compose window, locate the GpgOL buttons in the ribbon
2. Click the **Encrypt** button (lock icon)
   - This will encrypt the message using the TA's public key
   - Only the TA can decrypt it with their private key
3. Click the **Sign** button (signature icon)
   - This will digitally sign the message using your private key
   - The TA can verify it came from you
4. Both buttons should appear highlighted/active

### 7.3 Send the Encrypted Email

1. Click **Send**
2. You may be prompted to enter your **passphrase** (the one you created in Step 2)
3. Enter your passphrase and click **OK**
4. The email will be encrypted and sent

**What happens:** 
- The email content is encrypted using the TA's public key
- Only the TA can decrypt it with their private key
- Your digital signature proves the email came from you and wasn't tampered with

---

## Step 8: Verification Checklist

After sending both emails, verify the following:

- ✅ Email #1 sent successfully with your public key attached
- ✅ Email #2 sent successfully (encrypted and signed)
- ✅ You received no bounce-back or error messages
- ✅ Both emails sent before the deadline: **2025-nov-06 23:59**

**Success criteria (from assignment):**
- The TA can import your public key
- The TA can decrypt your encrypted email
- The TA can verify your digital signature

---

## Troubleshooting

### Problem: GpgOL buttons don't appear in Outlook

**Solution:**
1. Restart Outlook
2. Check if GpgOL is enabled: File → Options → Add-ins
3. If disabled, enable it and restart again
4. Try repairing Gpg4win installation

### Problem: "No valid certificate found" when trying to encrypt

**Solution:**
1. Verify you imported the TA's public key (Step 3)
2. In Kleopatra, check that `mitadic@constructor.university` appears in your certificate list
3. Try re-importing `milica_publickey.asc`

### Problem: Can't sign email - passphrase prompt doesn't appear

**Solution:**
1. In Kleopatra, verify your key exists and is valid
2. Try setting your default key: Outlook → File → Options → GpgOL
3. Restart Outlook

### Problem: Email sends but recipient can't decrypt

**Solution:**
1. Verify you encrypted with the correct recipient's public key
2. Check that the "Encrypt" button was active before sending
3. Resend the email, ensuring encryption is enabled

### Problem: Forgot my passphrase

**Solution:**
Unfortunately, if you forget your passphrase, you cannot use your private key. You'll need to:
1. Generate a new key pair (Step 2)
2. Export the new public key (Step 5)
3. Resend both emails with the new keys

### Problem: Key generation is very slow

**Solution:**
- Key generation (especially 4096-bit) can take 1-5 minutes
- Move your mouse and type on keyboard to generate randomness
- Be patient and wait for completion

---

## Additional Resources

### Understanding Public Key Cryptography

- **Public Key:** Can be shared with anyone. Used to encrypt messages TO you.
- **Private Key:** Must be kept secret. Used to decrypt messages and sign emails.
- **Encryption:** Sender uses recipient's public key → only recipient's private key can decrypt
- **Digital Signature:** Sender uses their private key → anyone with sender's public key can verify

### Key Concepts from Lecture (a0_security.pdf)

- **Symmetric Encryption (DES/AES):** Same key for encryption and decryption
- **Public-Key Encryption (RSA):** Two keys - public and private
- **Digital Signatures:** Prove authenticity and integrity
- **SSL/TLS:** Uses certificates and public-key encryption for secure web connections

### GPG Command Line (Alternative)

If you prefer command-line tools instead of Kleopatra:

```bash
# Generate key pair
gpg --full-generate-key

# Import TA's public key
gpg --import milica_publickey.asc

# Export your public key
gpg --armor --export your.email@constructor.university > your_publickey.asc

# Encrypt and sign a file
gpg --encrypt --sign --armor -r mitadic@constructor.university message.txt
```

---

## Summary

**What you accomplished:**
1. ✅ Installed Gpg4win with Kleopatra and GpgOL
2. ✅ Generated a 4096-bit RSA key pair
3. ✅ Imported the TA's public key
4. ✅ Configured Outlook for encryption
5. ✅ Sent your public key to the TA
6. ✅ Sent an encrypted and digitally signed email to the TA

**Assignment complete!** 🎉

The TA will verify:
- They can import your public key
- They can decrypt your encrypted message
- They can verify your digital signature

---

## Files in This Directory

- `SECURITY_I_GUIDE.md` - This guide
- `milica_publickey.asc` - TA's public key (reference copy)

---

**Last Updated:** November 6, 2025  
**Author:** Aleksandr Zinovev  
**Course:** Databases & Web Services (CO-560-B)

