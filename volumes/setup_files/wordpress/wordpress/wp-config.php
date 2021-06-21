<?php

/**
 * WordPress の基本設定
 *
 * このファイルは、インストール時に wp-config.php 作成ウィザードが利用します。
 * ウィザードを介さずにこのファイルを "wp-config.php" という名前でコピーして
 * 直接編集して値を入力してもかまいません。
 *
 * このファイルは、以下の設定を含みます。
 *
 * * MySQL 設定
 * * 秘密鍵
 * * データベーステーブル接頭辞
 * * ABSPATH
 *
 * @link https://ja.wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// 注意:
// Windows の "メモ帳" でこのファイルを編集しないでください !
// 問題なく使えるテキストエディタ
// (http://wpdocs.osdn.jp/%E7%94%A8%E8%AA%9E%E9%9B%86#.E3.83.86.E3.82.AD.E3.82.B9.E3.83.88.E3.82.A8.E3.83.87.E3.82.A3.E3.82.BF 参照)
// を使用し、必ず UTF-8 の BOM なし (UTF-8N) で保存してください。

// ** MySQL 設定 - この情報はホスティング先から入手してください。 ** //
/** WordPress のためのデータベース名 */
define('DB_NAME', 'database');

/** MySQL データベースのユーザー名 */
define('DB_USER', 'docker');

/** MySQL データベースのパスワード */
define('DB_PASSWORD', 'docker');

/** MySQL のホスト名 */
define('DB_HOST', 'mysql');

/** データベースのテーブルを作成する際のデータベースの文字セット */
define('DB_CHARSET', 'utf8mb4');

/** データベースの照合順序 (ほとんどの場合変更する必要はありません) */
define('DB_COLLATE', '');

/**#@+
 * 認証用ユニークキー
 *
 * それぞれを異なるユニーク (一意) な文字列に変更してください。
 * {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org の秘密鍵サービス} で自動生成することもできます。
 * 後でいつでも変更して、既存のすべての cookie を無効にできます。これにより、すべてのユーザーを強制的に再ログインさせることになります。
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'la;cWIeG&:;e@[t194o2kE@qq{%E3WY{;#}a*vVzPzI8VBak)on8Uq949sp:tV!r');
define('SECURE_AUTH_KEY',  'wy5@z.j^Pysy>X</D09!#~7-;Hhj.M>]0Jk%Ew>J:,wsKONqh>yHk7$0}DV%B%lq');
define('LOGGED_IN_KEY',    ');0;)D0LMu.tF$vQec+UQ3.3>>ERsBn2y.4/g_q3#!8HDv >KZkl^ F<VK-PhDb7');
define('NONCE_KEY',        'g&#t@2F={P;wHJ5K}-|c}#e9ji/hwBGb7&;8vqax(Z,%87iM#v7)Dq`(n@oyJd3.');
define('AUTH_SALT',        '.rxfe!xhsMd#pEJ2+A6C@RdF).($xApC9:Y*/dx+g1N~!QuaqSB<4ct{P#8GqYKn');
define('SECURE_AUTH_SALT', 'gc}C]Pi3,o XAMU)qPu3;Ksai}PE&q##P?{pY}2ZDdPo~uF.p+v))b:] 1Cq_*Ud');
define('LOGGED_IN_SALT',   '3u=`Dic-.Mg&#w(6ESnSr&rs1Z^T3:p&m<6j,=6&F>MKM61C6Ky)-m#gzk*M_yor');
define('NONCE_SALT',       'y&0v_..#.I#I!>Yn.0:/v,Tnd9oPW<lJBoL`2N#S7f5G3=5|v3=W>3_}@J$>>WZX');

/**#@-*/

/**
 * WordPress データベーステーブルの接頭辞
 *
 * それぞれにユニーク (一意) な接頭辞を与えることで一つのデータベースに複数の WordPress を
 * インストールすることができます。半角英数字と下線のみを使用してください。
 */
$table_prefix = 'wp_';

/**
 * 開発者へ: WordPress デバッグモード
 *
 * この値を true にすると、開発中に注意 (notice) を表示します。
 * テーマおよびプラグインの開発者には、その開発環境においてこの WP_DEBUG を使用することを強く推奨します。
 *
 * その他のデバッグに利用できる定数についてはドキュメンテーションをご覧ください。
 *
 * @link https://ja.wordpress.org/support/article/debugging-in-wordpress/
 */
define('WP_DEBUG', true);
define('FS_METHOD', 'direct');

/* 編集が必要なのはここまでです ! WordPress でのパブリッシングをお楽しみください。 */

/** Absolute path to the WordPress directory. */
if (!defined('ABSPATH')) {
	define('ABSPATH', __DIR__ . '/');
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
