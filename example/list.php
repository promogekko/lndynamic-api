<?php

require_once('lndynamic.php');
$api_id = 'YOUR API ID';
$api_key = 'YOUR API KEY';
$api = new LNDynamic($api_id, $api_key);
print_r($api->request('vm', 'list'));

?>
