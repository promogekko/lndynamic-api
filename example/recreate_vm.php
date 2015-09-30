<?php

// deletes and recreates a virtual machine from a new image, retaining the old IP address

require_once('lndynamic.php');
$api_id = 'YOUR API ID';
$api_key = 'YOUR API KEY';
$target_vm_name = 'myvm';
$target_image_name = 'Ubuntu 14.04 64-bit (template)';
$api = new LNDynamic($api_id, $api_key);

// find the target virtual machine ID
$vms = $api->request('vm', 'list');
$target_vm_id = false;

foreach($vms['vms'] as $vm) {
	if(strcasecmp($vm['name'], $target_vm_name) === 0) {
		$target_vm_id = $vm['vm_id'];
		break;
	}
}

//find the target image ID
$images = $api->request('image', 'list');
$target_image_id = false;

foreach($images['images'] as $image) {
	if(strcasecmp($image['name'], $target_image_name) === 0) {
		$target_image_id = $image['image_id'];
		break;
	}
}

if($target_vm_id === false) {
	die('No VM found!');
}

if($target_image_id === false) {
	die('No image found!');
}

// disassociate the IP address
$info = $api->request('vm', 'info', array('vm_id' => $target_vm_id));
if(empty($info['info']['ip'])) {
	die('VM does not have IP!');
}
$api->request('vm', 'floatingip-delete', array('vm_id' => $target_vm_id, 'keep' => 'yes'));
$api->request('vm', 'delete', array('vm_id' => $target_vm_id));
$api->request('vm', 'create', array('hostname' => $info['info']['hostname'], 'plan_id' => $info['extra']['plan_id'], 'image_id' => $target_image_id, 'ip' => $info['info']['ip']));

?>
