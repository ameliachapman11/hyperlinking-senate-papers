<?php
/**
 * Plugin Name: XML/XSLT Upload Fix
 * Description: Allows XML, XSLT, and SVG uploads.
 * Version: 1.0
 */

function custom_allow_xml_uploads($mimes) {
    $mimes['xml']  = 'text/xml';
    $mimes['svg']  = 'image/svg+xml';
    $mimes['xsl']  = 'application/xslt+xml';
    $mimes['xslt'] = 'application/xslt+xml';
    return $mimes;
}
add_filter('upload_mimes', 'custom_allow_xml_uploads');

function custom_fix_xml_filetype_check($data, $file, $filename, $mimes) {
    $filetype = wp_check_filetype($filename, $mimes);

    if (in_array($filetype['ext'], array('xml', 'xsl', 'xslt', 'svg'))) {
        $data['ext']  = $filetype['ext'];
        $data['type'] = $filetype['type'];
    }

    return $data;
}
add_filter('wp_check_filetype_and_ext', 'custom_fix_xml_filetype_check', 10, 4);