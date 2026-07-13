# Bugs Found

## BUG-001: Missing Loader During Svan Language Switching on Login Page

### Summary
No loading indicator is displayed when switching the language to Svan on the Login Page.

### Steps to Reproduce
1. Open the Login Page.
2. Switch the language to Svan.
3. Observe the language switching process.

### Expected Result
A loading indicator should be displayed while the translation resources are loading.

### Actual Result
No loader is displayed during the language switch. However, the Svan translation is applied successfully.

### Severity
Minor

### Priority
Low

---

## BUG-002: Megrelian Translation Requires Page Refresh on Login Page

### Summary
Megrelian localization is not applied immediately after switching the language on the Login Page.

### Steps to Reproduce
1. Open the Login Page.
2. Switch the language to Megrelian.
3. Observe the displayed text.

### Expected Result
The Login Page should be translated into Megrelian immediately after switching the language.

### Actual Result
The localization key `LANDING.AUTH.LOGIN_INTO_SYS` is displayed instead of the translated text. After refreshing the page, the correct translation appears.

### Severity
Major

### Priority
High