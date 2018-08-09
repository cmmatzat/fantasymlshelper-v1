<?php
    include_once($_SERVER["DOCUMENT_ROOT"] . '/resources/config.php');
    $router = new Router();
    $router->route($_SERVER['REQUEST_URI']);

?>