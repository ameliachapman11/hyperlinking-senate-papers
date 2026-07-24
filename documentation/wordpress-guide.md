# Setting Up the WordPress Site Locally
This file provides instructions for setting up a local copy of the WordPress site on your machine using LocalWP. LocalWP is a local dev environment for WordPress sites. As we are creating a prototype, we do not intend to host the site on a server, so you need to use LocalWP to view/interact with the prototype.

<br/>

## Prerequisites
You will need the following installed before starting:
* A computer running Windows, macOS, or Linux
* [Git](https://git-scm.com/downloads) — to clone the repository
* At least 4GB of free RAM space

<br/>

## Step 1: Install LocalWP
1. Go to [https://localwp.com/](https://localwp.com/) and download the installer for your operating system
2. Run the installer and follow the on-screen instructions
3. Open LocalWP once installation is complete

<br/>

## Step 2: Clone the Repository
Open a terminal and run:
```bash
git clone https://github.com/ameliachapman11/hyperlinking-senate-papers.git
```

This step can also be alternatively done in an IDE such as VS Code.

The only *required* files for running the site are contained in the `wordpress` folder&mdash;all others are related to documentation and the PDF to XML script. You should not need to download any plugins once the site is activated&mdash;they should be contained in the folder.

<br/>

## Step 3: Create a New Site in LocalWP
1. Open LocalWP and click the **+** button in the bottom left corner to create a new site
2. Select **Create a new site** and click **Continue**
3. Give the site a name (e.g. `committee-docs`) and click **Continue**
4. Leave the environment settings as their defaults and click **Continue**
5. Set a WordPress username and password you will remember&mdash;these are for logging into the WordPress admin dashboard. These can be changed at a later time.
6. Click **Add Site** and wait for LocalWP to finish setting up

<br/>

## Step 4: Replace the Site Files with the Repository Files
Once the site is created, LocalWP will have generated a folder structure for it on your machine. You need to replace the generated WordPress files with the ones from the repository.

1. In LocalWP, right-click your site and select **Open Site Folder**&mdash;this opens the folder LocalWP created for your site
2. Navigate into the `app/public` subfolder (this is where the WordPress files live)
3. Delete everything inside `app/public`
4. Copy the entire contents of the `wordpress` folder from the cloned repository into `app/public`

*Note: You are copying the **contents** of the `wordpress` folder, not the folder itself. The files inside `wordpress` should sit directly inside `app/public`.*

<br/>

## Step 5: Import the Database
The database contains all the site's content, settings, and configuration. Without importing it, the site will appear empty.

*Important: Your site must be running in LocalWP before you can access or make any changes to the database. Click the **Start site** button to begin running your site.*

In LocalWP, make sure your site is running (click Start Site in the top-right corner if it is stopped).
1. Click the Database tab in LocalWP
2. Click Open AdminNeo &rarr; this opens the database management interface in your browser
3. In AdminNeo, click **Import** in the left sidebar.
4. Click Choose File and select the `local.sql` file from the `wordpress` folder
5. Click Execute and wait for the import to complete

<br/>

## Step 6: Fix the Site URL
WordPress stores the site URL in the database. After importing, the URL will still point to the original developer's local URL rather than yours, which will cause the site to redirect incorrectly. You need to update it.

1. In Adminer, click **SQL Command** in the left sidebar
2. Run the following two commands, replacing `http://your-site.local` with the URL shown in LocalWP under your site name (visible on the site's overview page):
```sql
UPDATE wp_options SET option_value = 'http://your-site.local' WHERE option_name = 'siteurl';
UPDATE wp_options SET option_value = 'http://your-site.local' WHERE option_name = 'home';
```
3. Click **Execute**

<br/>

## Step 7: Visit the Site
1. In LocalWP, click **Open Site** to view the site in your browser
2. To access the WordPress admin dashboard, go to `http://your-site.local/wp-admin` and log in with the username and password you set in Step 3 (or click the **WP Admin** site button on the LocalWP app)
3. To view the public-facing site, click the **Open Site** button on the LocalWP app
