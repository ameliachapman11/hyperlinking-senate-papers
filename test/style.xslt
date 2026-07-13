<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes" encoding="UTF-8"/>

    <xsl:template match="/committeeDoc">
        <html>
            <head>
                <title>Committee Document</title>
                <style>
                    body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; color: #333; }
                    .bold-text { font-weight: bold; margin: 12px 0; display: block; }
                    .body-text { margin: 12px 0; display: block; }
                    .image-container { margin: 20px 0; }
                    .image-container img { max-width: 100%; height: auto; display: block; }
                    
                    /* Table Styles */
                    table { border-collapse: collapse; width: 100%; margin: 20px 0; }
                    table, th, td { border: 1px solid #ccc; }
                    tr:nth-child(even) { background-color: #f9f9f9; }
                    
                    /* UPDATED: Added line-height and padding to fix squished cells */
                    td { padding: 12px 10px; text-align: left; line-height: 1.5; }
                    
                    /* Added link styling */
                    a { color: #0066cc; text-decoration: none; }
                    a:hover { text-decoration: underline; }
                </style>
            </head>
            <body>
                <xsl:apply-templates/>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="metadata"/>

    <xsl:template match="boldText">
        <span class="bold-text">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    <xsl:template match="bodyText">
        <p class="body-text">
            <xsl:apply-templates/>
        </p>
    </xsl:template>

    <xsl:template match="image">
        <div class="image-container">
            <img src="data:image/{@ext};base64,{normalize-space(.)}" alt="Embedded Document Image" />
        </div>
    </xsl:template>

    <xsl:template match="table">
        <table>
            <xsl:apply-templates select="row"/>
        </table>
    </xsl:template>

    <xsl:template match="row">
        <tr>
            <xsl:apply-templates select="cell"/>
        </tr>
    </xsl:template>

    <xsl:template match="cell">
        <td>
            <xsl:apply-templates/>
        </td>
    </xsl:template>

    <xsl:template match="br">
        <br/>
    </xsl:template>

    <xsl:template match="a">
        <a href="{@href}">
            <xsl:apply-templates/>
        </a>
    </xsl:template>

</xsl:stylesheet>