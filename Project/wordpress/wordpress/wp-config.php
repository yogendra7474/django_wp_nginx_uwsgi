<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'pipegenius' );

/** MySQL database username */
define( 'DB_USER', 'yogendra' );

/** MySQL database password */
define( 'DB_PASSWORD', 'Y@gi1310' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */

define('AUTH_KEY',         '3_XO?%D_0gj-n[S/-:n1=8k`9gyz)_Ewt,F_*J?&e^8x{bqPbkh+aGxBw.91*hme');
define('SECURE_AUTH_KEY',  '|{:7OR[q;s^)+C+RX](RaC,C-6?3Yo:]k+|iw4Sk9[(0xiJRzda}`]G+Xj-e1LcM');
define('LOGGED_IN_KEY',    'ZSr,OE?xzY<CKY1x~1h7I!gm9oIrK@uf)-nb/7L>Ux@i%R}NhDb!:Rpff~O-841!');
define('NONCE_KEY',        'NG((_$Gi^V=S,M5T*K d#;k:3N,wXy~e?`:W UYv+|o;Qb4#[MoM}Gwd|z*lb~G)');
define('AUTH_SALT',        ' C [VFt(|aT|b#=*;%ZdfwK*YW}_qeB+Wp|6YF88fAMr*%.8T]hh=j%946jW:+v8');
define('SECURE_AUTH_SALT', '<]C+4uF0)[I`ohfGG#uVwK^B;cT7zd>G5G{k^jv,L!qJ6o APR|%Rc)puQ Wt$J+');
define('LOGGED_IN_SALT',   'RPMXyn)Nkb6hQ<vrG(ytw1+WxmSjPGd0yM6Em/lhq9 r(VOmrTYF=V) LQh=upK8');
define('NONCE_SALT',       'U=^^?4QhMNx7~B8u*^8CBF` F3Tb|l|K)g8Ssui1,~(vHyIsD.=;+59|Q66N| YI');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
